import sys

from . import common


class MathutilsTest(common.FakeBpyModuleTestBase):
    module_name = "mathutils"

    def setUp(self):
        import mathutils

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
