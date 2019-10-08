import unittest


class FakeBpyModuleTestBase(unittest.TestCase):

    module_name = ""

    @classmethod
    def setUpClass(cls):
        print("\n======== Module Test: {} ========".format(cls.module_name))

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass
