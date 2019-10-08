import sys

from . import common


class BpyExtrasTest(common.FakeBpyModuleTestBase):

    module_name = "bpy_extras"

    def setUp(self):
        import bpy_extras

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
