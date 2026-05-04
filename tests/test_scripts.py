import unittest
import os
import shutil
import tempfile
import sys
from pathlib import Path
from io import StringIO

workspace_root = Path(__file__).parent.parent
sys.path.insert(0, str(workspace_root / ".agents" / "skills" / "lint" / "scripts"))
sys.path.insert(0, str(workspace_root / ".agents" / "skills" / "ingest" / "scripts"))
sys.path.insert(0, str(workspace_root / ".agents" / "skills" / "search" / "scripts"))

import lint_wiki
import generate_index
import search_wiki

class TestScripts(unittest.TestCase):
    def setUp(self):
        # Create a temporary workspace root
        self.test_dir = tempfile.mkdtemp()
        self.root_path = Path(self.test_dir)
        self.wiki_dir = self.root_path / "wiki"
        self.wiki_dir.mkdir()
        
        # Create subdirectories
        for d in ["characters", "locations", "plot", "worldbuilding"]:
            (self.wiki_dir / d).mkdir()

    def tearDown(self):
        shutil.rmtree(self.test_dir)
        
    def test_lint_wiki(self):
        # Create a valid character
        char_file = self.wiki_dir / "characters" / "john.md"
        char_file.write_text("---\nname: John\naliases: []\nage: 30\nrole: protagonist\nstatus: alive\nfirst_appearance: Chapter 1\n---\nHello [link](john.md)")
        
        # Create a broken link in a location
        loc_file = self.wiki_dir / "locations" / "city.md"
        loc_file.write_text("---\nregion: North\ncontrol_faction: None\n---\n[broken](nowhere.md)")
        
        # Add index to prevent orphans
        index_file = self.wiki_dir / "index.md"
        index_file.write_text("[john](characters/john.md)\n[city](locations/city.md)")
        
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        lint_wiki.main(root_dir=self.root_path)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("Broken link to 'nowhere.md'", output)
        self.assertIn("Found 1 issues", output)

    def test_generate_index(self):
        # Create a dummy character
        char_file = self.wiki_dir / "characters" / "john_doe.md"
        char_file.write_text("dummy content")
        
        generate_index.generate_index(root_dir=self.root_path)
        
        index_file = self.wiki_dir / "index.md"
        self.assertTrue(index_file.exists())
        
        content = index_file.read_text()
        self.assertIn("## Characters", content)
        self.assertIn("[John Doe](characters/john_doe.md)", content)
        self.assertIn("## Locations\n*(Empty)*", content)

    def test_search_wiki_python_fallback(self):
        # Test the pure Python search (bypassing git grep by providing a dummy path where git isn't repo)
        char_file = self.wiki_dir / "characters" / "secret.md"
        char_file.write_text("This is a HIDDEN_KEYWORD test.")
        
        captured_output = StringIO()
        sys.stdout = captured_output
        search_wiki.search_wiki("HIDDEN_KEYWORD", root_dir=self.root_path)
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue()
        self.assertIn("characters/secret.md:1: This is a HIDDEN_KEYWORD test.", output)
        self.assertIn("Found 1 matching lines", output)

if __name__ == '__main__':
    unittest.main()
