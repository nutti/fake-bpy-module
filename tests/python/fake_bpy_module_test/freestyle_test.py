import sys

from . import common


class FreestyleTest(common.FakeBpyModuleTestBase):

    module_name = "freestyle"

    def setUp(self):
        import freestyle

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
