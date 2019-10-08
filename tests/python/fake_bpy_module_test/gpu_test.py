import sys

from . import common


class GpuTest(common.FakeBpyModuleTestBase):

    module_name = "gpu"

    def setUp(self):
        import gpu

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
