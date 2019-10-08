import sys

from . import common


class BmeshTest(common.FakeBpyModuleTestBase):

    module_name = "bmesh"

    def setUp(self):
        import bmesh

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
