import sys
import unittest
import os


LOG_DIR = "import_module_test.log"

class <%% CLASS_NAME %%>(unittest.TestCase):

    module_name = "<%% MODULE_NAME %%>"

    @classmethod
    def setUpClass(cls):
        if cls.module_name is None:
            raise ValueError("module_name must set")

        cls.log_dir = "{}/{}".format(LOG_DIR, cls.module_name)
        os.makedirs(cls.log_dir, exist_ok=True)

        filename = "{}/<%% CLASS_NAME %%>.log".format(cls.log_dir)
        cls.file_ = open(filename, "w")

    @classmethod
    def tearDownClass(cls):
        cls.file_.close()

    def setUp(self):
        self.log("========== Test: {} ==========".format(self.id()))

        import <%% MODULE_NAME %%>

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def log(self, message):
        self.__class__.file_.write(message + "\n")

    def test_nothing(self):
        self.log("Test nothing")
