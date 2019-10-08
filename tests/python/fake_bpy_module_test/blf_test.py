import sys

from . import common


class BlfTest(common.FakeBpyModuleTestBase):

    module_name = "blf"

    def setUp(self):
        import blf

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
