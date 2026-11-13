"""Validate a portable skill package without external Python dependencies."""
import hashlib
import json
import re
import struct
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


def private_content(text):
    patterns = {
        'local-user-path': r'(?:/Users|/home)/[^/\s]+/',
        'organization-url': r'https?://[\w-]+\.feishu\.cn/',
        'token': r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,})',
        'personal-email': r'[\w.+-]+@(?:gmail|qq|163|outlook)\.com\b',
    }
    return [name for name, pattern in patterns.items() if re.search(pattern, text)]


def local_links(root, doc):
    errors = []
    for target in re.findall(r'\]\(([^)]+)\)', doc.read_text(encoding='utf-8')):
        if '://' in target or target.startswith('#'):
            continue
        path = (doc.parent / unquote(target.split('#')[0])).resolve()
        if not path.is_relative_to(root.resolve()) or not path.exists():
            errors.append('missing or external local link')
    return errors


def png_size(path):
    with path.open('rb') as image:
        header = image.read(24)
    if len(header) != 24 or header[:8] != b'\x89PNG\r\n\x1a\n' or header[12:16] != b'IHDR':
        raise ValueError('invalid PNG header')
    return struct.unpack('>II', header[16:24])


def main():
    errors = []
    skill = ROOT / 'skills/editorial-cover/SKILL.md'
    text = skill.read_text(encoding='utf-8')
    if not re.match(r'^---\nname: editorial-cover\ndescription: .+\n---\n', text):
        errors.append('SKILL.md: missing name/description frontmatter')
    for path in ROOT.rglob('*'):
        if not path.is_file() or any(p in {'.git', '__pycache__'} for p in path.parts):
            continue
        if path.suffix in {'.md', '.json', '.yaml', '.yml', '.py', '.txt'}:
            data = path.read_text(encoding='utf-8')
            errors.extend(f'{path.relative_to(ROOT)}: {kind}' for kind in private_content(data))
            if path.suffix == '.md':
                errors.extend(f'{path.relative_to(ROOT)}: {e}' for e in local_links(ROOT, path))
    for item in json.loads((ROOT / 'examples/manifest.json').read_text())['images']:
        path = (ROOT / item['file']).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            errors.append('manifest: missing or external asset')
            continue
        if list(png_size(path)) != item['pixels']:
            errors.append(f'{path.name}: actual pixel dimensions differ')
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            errors.append(f'{path.name}: hash differs')
    if errors:
        print('\n'.join(errors))
        return 1
    print('PASS: skill metadata, local links, public text, example pixels and hashes')
    return 0


if __name__ == '__main__':
    sys.exit(main())
