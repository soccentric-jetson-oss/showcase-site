"""Validate the showcase website."""
import unittest
import os

class TestSite(unittest.TestCase):
    def test_index_exists(self):
        self.assertTrue(os.path.exists('index.html'))
    
    def test_index_has_content(self):
        with open('index.html') as f:
            content = f.read()
        self.assertIn('Cortex Forge', content)
        self.assertIn('Iris Flow', content)
        self.assertIn('Reel Forge', content)
        self.assertIn('Nexus Bus', content)
        self.assertIn('Volt Guard', content)
    
    def test_all_links_present(self):
        with open('index.html') as f:
            content = f.read()
        for project in ['cortex-forge', 'iris-flow', 'reel-forge', 'nexus-bus', 'volt-guard']:
            for tier in ['driver', 'server', 'gui']:
                self.assertIn(f'{project}-{tier}', content)

if __name__ == "__main__":
    unittest.main()
