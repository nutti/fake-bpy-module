import sys

from . import common


class BglTest(common.FakeBpyModuleTestBase):

    module_name = "bgl"

    def setUp(self):
        import bgl

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
