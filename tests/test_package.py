import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package_check', ROOT / 'scripts/check_package.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class PackageChecks(unittest.TestCase):
    def test_public_text_accepts_relative_paths(self):
        self.assertEqual(check.private_content('See assets/reference.png and $HOME/.agents/skills'), [])

    def test_public_text_rejects_local_user_paths(self):
        text = '/' + 'Users' + '/' + 'someone' + '/private/file'
        self.assertTrue(check.private_content(text))

    def test_public_text_rejects_live_token_shape(self):
        self.assertTrue(check.private_content('gh' + 'p_' + 'a' * 36))

    def test_missing_local_link_is_reported(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            doc = root / 'SKILL.md'
            doc.write_text('[missing](references/missing.md)')
            self.assertTrue(check.local_links(root, doc))

    def test_actual_image_dimensions_match_manifest(self):
        image = ROOT / 'skills/cover-design/assets/reference-4x3.png'
        self.assertEqual(check.png_size(image), (1448, 1086))


if __name__ == '__main__':
    unittest.main()
