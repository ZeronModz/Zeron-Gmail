import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "api"))
from aliases import generate


class AliasTests(unittest.TestCase):
    def test_dot_alias(self):
        value = generate("first.last@gmail.com", "dot")
        self.assertEqual(value.split("@", 1)[0].replace(".", ""), "firstlast")

    def test_plus_alias(self):
        self.assertTrue(generate("first.last@gmail.com", "dotplus").startswith("firstlast+"))


if __name__ == "__main__":
    unittest.main()
