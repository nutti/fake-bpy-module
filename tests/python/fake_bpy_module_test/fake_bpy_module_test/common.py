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

        cls.log_dir = f"{LOG_DIR}/{cls.module_name}"
        os.makedirs(cls.log_dir, exist_ok=True)

        filename = f"{cls.log_dir}/{cls.name}.log"
        cls.file_ = open(filename, "w", encoding="utf-8")  # noqa # pylint: disable=R1732

    @classmethod
    def tearDownClass(cls):
        cls.file_.close()

    def setUp(self):
        self.maxDiff = None  # pylint: disable=C0103
        self.log(f"========== Test: {self.id()} ==========")

    def tearDown(self):
        pass

    def log(self, message):
        self.__class__.file_.write(message + "\n")
