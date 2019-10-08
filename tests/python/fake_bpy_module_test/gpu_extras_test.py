import sys

from . import common


class GpuExtrasTest(common.FakeBpyModuleTestBase):

    module_name = "gpu_extras"

    def setUp(self):
        import gpu_extras

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
