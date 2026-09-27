"""Verifica imágenes y referencias locales sin modificar el trabajo de otros agentes."""
from pathlib import Path
from html.parser import HTMLParser
import json
import argparse
from urllib.parse import urlsplit, unquote
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        for name, value in attrs:
            if attributes.get('aria-disabled') == 'true' and name == 'href':
                continue
            if name in ('src', 'data-audio', 'href') and value and not urlsplit(value).scheme and not value.startswith(('#', '//')):
                self.paths.append(value)

cli = argparse.ArgumentParser(description=__doc__)
cli.add_argument('--section', default='01-introduccion', help='Nombre de carpeta de la sección, o «todas» para toda la enciclopedia')
cli.add_argument('--report', action='store_true', help='Guardar informe JSON en assets')
args = cli.parse_args()
if Path(args.section).name != args.section or args.section in ('.', '..', 'portada'):
    cli.error('La sección debe ser un nombre de carpeta')
def verificar(section, pages=None):
    report = {'section': section, 'pages': [], 'references': [], 'images': [], 'audio': [], 'errors': [],
              'scope': 'Referencias de todas las páginas HTML, integridad de imágenes raster y tramas MP3; no es revisión auditiva ni validación científica. Enlaces deshabilitados excluidos; fragmentos internos no comprobados.'}
    pages = pages or sorted((ROOT / 'secciones' / section).rglob('*.html'))
    if not pages:
        raise SystemExit('No hay páginas HTML en ' + section)
    for page in pages:
        parser = References()
        parser.feed(page.read_text(encoding='utf-8'))
        report['pages'].append(str(page.relative_to(ROOT)))
        for reference in parser.paths:
            target = (page.parent / unquote(urlsplit(reference).path)).resolve()
            if target.is_dir():
                target = target / 'index.html'
            exists = target.is_file()
            record = {'page': str(page.relative_to(ROOT)), 'reference': reference, 'exists': exists}
            report['references'].append(record)
            if not exists:
                report['errors'].append(record)
                print('FALTA:', page.name, reference)
        print('Página revisada:', page.name, len(parser.paths), 'referencias')
    for path in sorted((ROOT / 'assets/images' / section).rglob('*')):
        if path.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp', '.gif'):
            continue
        with Image.open(path) as im:
            dimensions = im.size
            im.verify()
        print('OK imagen:', path.name, dimensions)
        report['images'].append({'file': path.name, 'width': dimensions[0], 'height': dimensions[1]})

    # Cuenta tramas MPEG-1 Layer III (MP3 44.1 kHz generado por ElevenLabs).
    for path in sorted((ROOT / 'assets/audio' / section).glob('*.mp3')):
        data = path.read_bytes()
        pos = 0
        if data[:3] == b'ID3':
            pos = 10 + sum((data[6+i] & 127) << (7*(3-i)) for i in range(4))
        seconds = 0
        frames = 0
        rates = [0,32,40,48,56,64,80,96,112,128,160,192,224,256,320,0]
        while pos + 4 <= len(data):
            header = int.from_bytes(data[pos:pos+4], 'big')
            if header >> 21 != 0x7ff or (header >> 19) & 3 != 3 or (header >> 17) & 3 != 1:
                pos += 1
                continue
            bitrate = rates[(header >> 12) & 15] * 1000
            sample_index = (header >> 10) & 3
            if not bitrate or sample_index == 3:
                pos += 1
                continue
            sample_rate = [44100,48000,32000][sample_index]
            size = 144 * bitrate // sample_rate + ((header >> 9) & 1)
            assert pos + size <= len(data), 'Trama truncada'
            pos += size
            seconds += 1152 / sample_rate
            frames += 1
        assert frames > 0 and 0 < seconds <= 45, (path.name, seconds)
        print('OK audio:', path.name, round(seconds, 2), 'segundos;', frames, 'tramas')
        report['audio'].append({'file': path.name, 'seconds': round(seconds, 2), 'frames': frames})

    return report

SECCIONES = sorted(p.name for p in (ROOT / 'secciones').iterdir() if p.is_dir())

def huerfanos(reports):
    """Imágenes y audios que existen pero ninguna página usa."""
    usados = set()
    for r in reports:
        for ref in r['references']:
            usados.add((ROOT / ref['page']).parent.joinpath(unquote(urlsplit(ref['reference']).path)).resolve())
    sobran = []
    for carpeta in ('assets/images', 'assets/audio'):
        for path in (ROOT / carpeta).rglob('*'):
            if path.is_file() and path.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp', '.gif', '.mp3') and path.resolve() not in usados:
                sobran.append(str(path.relative_to(ROOT)))
    return sorted(sobran)

if args.section == 'todas':
    reports = [verificar(s) for s in SECCIONES]
    portada = verificar('portada', [ROOT / 'index.html'])
    reports.append(portada)
    total = {'sections': reports, 'orphans': huerfanos(reports),
             'errors': [e for r in reports for e in r['errors']]}
    for o in total['orphans']:
        print('SIN USO:', o)
    if args.report:
        (ROOT / 'assets' / 'verificacion-completa.json').write_text(json.dumps(total, ensure_ascii=False, indent=2), encoding='utf-8')
    print('TOTAL:', sum(len(r['pages']) for r in reports), 'páginas,', sum(len(r['references']) for r in reports), 'referencias,',
          sum(len(r['audio']) for r in reports), 'MP3,', len(total['orphans']), 'archivos sin uso,', len(total['errors']), 'referencias rotas')
    raise SystemExit(1 if total['errors'] else 0)

report = verificar(args.section)
if args.report:
    output = ROOT / 'assets' / ('verificacion-' + args.section + '.json')
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print('Resumen:', len(report['pages']), 'páginas,', len(report['references']), 'referencias,', len(report['images']), 'imágenes,', len(report['audio']), 'MP3,', len(report['errors']), 'referencias rotas')
raise SystemExit(1 if report['errors'] else 0)
