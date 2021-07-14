import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from src.detect_conflicts import (
    read_mod_descriptor_file,
    list_mod_files,
    index_mod_by_files,
    detect_conflicts,
)


class TestDetectConflicts(unittest.TestCase):
    def setUp(self):
        if os.path.exists("data"):
            self.data_dir = "data"
        elif os.path.exists(os.path.join("tests", "data")):
            self.data_dir = os.path.join("tests", "data")
        else:
            self.fail("Test data directory not found")

    def test_read_mod_descriptor_file(self):
        metadata = read_mod_descriptor_file(os.path.join(self.data_dir, "MyMoGIT.mod"))
        self.assertEqual("-My Monastery- GIT", metadata.name)
        self.assertEqual(
            "mod/MyMoGIT",
            metadata.path,
        )

    def test_list_mod_files(self):
        files = list_mod_files(os.path.join(self.data_dir, "MyMoGIT"))
        self.assertEqual(3, len(files))
        self.assertTrue("dummy.txt" in files)
        self.assertTrue("dummy2.txt" in files)
        self.assertTrue("descriptor.mod" in files)

    def test_index_mod_by_files(self):
        mods_by_file = index_mod_by_files(self.data_dir)
        self.assertEqual(4, len(mods_by_file))
        self.assertTrue("dummy.txt" in mods_by_file)
        self.assertEqual(1, len(mods_by_file["dummy.txt"]))
        self.assertEqual("-My Monastery- GIT", mods_by_file["dummy.txt"][0])
        self.assertTrue("dummy1.txt" in mods_by_file)
        self.assertEqual(1, len(mods_by_file["dummy1.txt"]))
        self.assertEqual("My Monastery 2", mods_by_file["dummy1.txt"][0])
        self.assertTrue("dummy2.txt" in mods_by_file)
        self.assertEqual(2, len(mods_by_file["dummy2.txt"]))
        self.assertEqual("My Monastery 2", mods_by_file["dummy2.txt"][0])
        self.assertEqual("-My Monastery- GIT", mods_by_file["dummy2.txt"][1])
        self.assertEqual(2, len(mods_by_file["descriptor.mod"]))
        self.assertEqual("My Monastery 2", mods_by_file["descriptor.mod"][0])
        self.assertEqual("-My Monastery- GIT", mods_by_file["descriptor.mod"][1])

    def test_detect_conflicts(self):
        conflicts = detect_conflicts(self.data_dir)
        self.assertEqual(2, len(conflicts))
        self.assertTrue("My Monastery 2" in conflicts)
        self.assertTrue("-My Monastery- GIT" in conflicts["My Monastery 2"])
        self.assertEqual(1, len(conflicts["My Monastery 2"]["-My Monastery- GIT"]))
        self.assertEqual(
            "dummy2.txt", conflicts["My Monastery 2"]["-My Monastery- GIT"][0]
        )
        self.assertTrue("-My Monastery- GIT" in conflicts)
        self.assertTrue("My Monastery 2" in conflicts["-My Monastery- GIT"])
        self.assertEqual(1, len(conflicts["-My Monastery- GIT"]["My Monastery 2"]))
        self.assertEqual(
            "dummy2.txt", conflicts["-My Monastery- GIT"]["My Monastery 2"][0]
        )


if __name__ == "__main__":
    unittest.main()
