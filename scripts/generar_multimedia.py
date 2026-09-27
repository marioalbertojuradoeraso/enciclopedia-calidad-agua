"""Generación reanudable de los pedidos de sección 1; claves solo en memoria."""
import argparse
import base64
import html
import json
from pathlib import Path
import re
import time
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / 'Enciclopedia'
STATE = PROJECT / 'assets' / 'multimedia-manifest.json'

def request(url, key=None, payload=None, provider='bfl'):
    headers = {}
    if key:
        headers['x-key' if provider == 'bfl' else 'xi-api-key'] = key
    if payload is not None:
        headers['Content-Type'] = 'application/json'
    req = urllib.request.Request(url, data=None if payload is None else json.dumps(payload).encode(), headers=headers)
    with urllib.request.urlopen(req, timeout=120) as response:
        data = response.read()
        return json.loads(data) if 'json' in response.headers.get('Content-Type', '') else data

def key(name):
    return (ROOT / name).read_text(encoding='utf-8-sig').strip()

def save(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')

STYLE = ('Use case: illustration-story. Single educational comic illustration, polished hand-painted cartoon, clean outlines, harmonious turquoise blue, orange and green, soft daylight. No text, letters, numbers, labels or watermarks. ')
GOTITA = ('Gotita is a bright blue teardrop character with a pointed head, large black eyes, orange-rimmed safety goggles, small white laboratory coat, orange backpack and orange shoes. Keep this exact character design. ')
SCENES = [
    ('comic-1.png', 1024, 1024, GOTITA + 'Gotita falls with raindrops from a white cloud toward a green mountain, mountain landscape and river below. Clear downward motion, cheerful expression.'),
    ('comic-2.png', 1024, 1024, GOTITA + 'Gotita travels downhill in a small rivulet over brown soil toward a river. A few tiny brown sediment grains and pale mineral specks are carried by flowing water around the character. Water transports materials naturally; no hands gathering objects. Clear close view of runoff.'),
    ('comic-3.png', 1024, 1024, GOTITA + 'An adult woman scientist with brown hair tied back, white coat, clear safety goggles and blue gloves carefully collects river water in an unlabelled sampling bottle at the river bank. Gotita is visible in the river nearby. Natural green mountain landscape. No drinking.'),
    ('comic-4.png', 1024, 1024, GOTITA + 'Gotita is inside a transparent beaker of water on a clean laboratory bench. An adult woman scientist with brown hair tied back, white coat, clear safety goggles and blue gloves examines the sample with laboratory equipment beside her. Friendly educational laboratory scene, no drinking, no symbols claiming the water is safe.'),
    ('vaso-lupa.png', 1024, 768, 'A transparent glass of clear water beside a large magnifying glass showing a schematic enlarged inset of tiny suspended particles and abstract microbe shapes. This is a conceptual educational magnification, not a realistic optical claim. White and pale turquoise background, clean spacious composition. No character, no scary faces, no safety checkmark.')
]

def images(state):
    secret = key('api_bfl.txt')
    for filename, width, height, scene in SCENES:
        relative = 'assets/images/01-introduccion/' + filename
        destination = PROJECT / relative
        if destination.exists():
            print('Existe: ' + relative, flush=True)
            continue
        model = 'flux-kontext-pro' if filename.startswith('comic-') else 'flux-pro-1.1'
        entry = state.setdefault(relative, {'prompt': STYLE + scene, 'provider': 'BFL', 'model': model})
        if 'polling_url' not in entry:
            payload = {'prompt': entry['prompt'], 'output_format': 'png', 'prompt_upsampling': False}
            if model == 'flux-kontext-pro':
                reference = PROJECT / 'assets/images/01-introduccion/gotita-lupa.png'
                payload.update(input_image=base64.b64encode(reference.read_bytes()).decode(), aspect_ratio='1:1')
            else:
                payload.update(width=width, height=height)
            job = request('https://api.bfl.ai/v1/' + model, secret, payload)
            entry.update(id=job['id'], polling_url=job['polling_url'], status='submitted')
            save(state)
            print('Solicitado: ' + filename, flush=True)
        for _ in range(120):
            result = request(entry['polling_url'], secret)
            if result['status'] == 'Ready':
                data = request(result['result']['sample'])
                if not data.startswith(b'\x89PNG\r\n\x1a\n'):
                    raise ValueError('La respuesta no es PNG')
                destination.parent.mkdir(parents=True, exist_ok=True)
                with destination.open('xb') as output:
                    output.write(data)
                entry['status'] = 'delivered'
                entry.pop('polling_url', None)
                save(state)
                print('Entregado: ' + relative, flush=True)
                break
            if result['status'] in ('Error', 'Failed', 'Request Moderated', 'Content Moderated'):
                entry['status'] = result['status']
                save(state)
                raise RuntimeError('BFL: ' + result['status'])
            time.sleep(3)
        else:
            raise TimeoutError('Generación pendiente; ejecutar nuevamente para recuperar')

def audio(state, voice, section_folder):
    source = (PROJECT / 'secciones' / section_folder / 'index.html').read_text(encoding='utf-8')
    blocks = re.findall(r'<div\s+class="parrafo"[^>]*>(.*?)</div>', source, re.S)
    for block in blocks:
        audio_link = re.search(r'data-audio="([^"]+)"', block)
        if not audio_link:
            continue
        filename = Path(audio_link.group(1)).name
        relative = 'assets/audio/' + section_folder + '/' + filename
        destination = PROJECT / relative
        if destination.exists():
            print('Existe: ' + relative, flush=True)
            continue
        script = html.unescape(re.sub('<[^>]+>', '', re.search(r'<p>(.*?)</p>', block, re.S).group(1)))
        if len(script.split()) > 95:
            raise ValueError('Guion demasiado largo')
        narration = re.sub(r'(^|[.!?] )(Para empezar|Es decir|Por ejemplo|De esta manera|Además|Por esta razón|Sin embargo|Así),', r'\1\2, <break time="0.4s" />', script)
        data = request('https://api.elevenlabs.io/v1/text-to-speech/' + voice + '?output_format=mp3_44100_128', key('api_ElevenLabs.txt'), {'text': narration, 'model_id': 'eleven_multilingual_v2', 'voice_settings': {'stability': 0.6, 'similarity_boost': 0.75, 'style': 0.15, 'use_speaker_boost': True, 'speed': 0.95}}, 'eleven')
        if not isinstance(data, bytes) or len(data) < 1000:
            raise ValueError('Audio inválido')
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('xb') as output:
            output.write(data)
        state[relative] = {'provider': 'ElevenLabs', 'model': 'eleven_multilingual_v2', 'voice_id': voice, 'text': script, 'status': 'delivered'}
        save(state)
        print('Entregado: ' + relative, flush=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['voices', 'images', 'audio'])
    parser.add_argument('--voice')
    parser.add_argument('--section', choices=['01-introduccion', '02-hidrosfera-ciclos', '03-cantidad-calidad', '04-parametros', '05-otros-parametros', '06-normatividad'], default='01-introduccion')
    args = parser.parse_args()
    state = json.loads(STATE.read_text(encoding='utf-8')) if STATE.exists() else {}
    try:
        if args.action == 'voices':
            voices = request('https://api.elevenlabs.io/v1/voices', key('api_ElevenLabs.txt'), provider='eleven')
            for voice in voices['voices']:
                print(json.dumps({k: voice.get(k) for k in ('voice_id', 'name', 'labels', 'category')}, ensure_ascii=True))
        elif args.action == 'images':
            images(state)
        elif args.voice:
            audio(state, args.voice, args.section)
        else:
            parser.error('--voice es obligatorio para audio')
    except urllib.error.HTTPError as error:
        print('Error HTTP ' + str(error.code) + '; credenciales y respuesta omitidas.')
        raise SystemExit(1)
    except urllib.error.URLError:
        print('Error de red; revisar permisos de conexión.')
        raise SystemExit(2)
