import sys

from . import common


class BpyTest(common.FakeBpyModuleTestBase):

    module_name = "bpy"

    def setUp(self):
        import bpy

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")