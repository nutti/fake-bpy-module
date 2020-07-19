import unittest
import os

LOG_DIR = "fake_bpy_module_test.log"


class FakeBpyModuleTestBase(unittest.TestCase):

    name = None
    module_name = None
    log_dir = None
    file_ = None

    @classmethod
    def setUpClass(cls):
        if cls.module_name is None:
            raise ValueError("module_name must set")
        if cls.name is None:
            raise ValueError("name must set")

        cls.log_dir = "{}/{}".format(LOG_DIR, cls.module_name)
        os.makedirs(cls.log_dir, exist_ok=True)

        filename = "{}/{}.log".format(cls.log_dir, cls.name)
        cls.file_ = open(filename, "w")

    @classmethod
    def tearDownClass(cls):
        cls.file_.close()

    def setUp(self):
        self.maxDiff = None
        self.log("========== Test: {} ==========".format(self.id()))

    def tearDown(self):
        pass

    def log(self, message):
        self.__class__.file_.write(message + "\n")
