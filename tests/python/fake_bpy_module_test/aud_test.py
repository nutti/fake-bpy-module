import sys

from . import common


class AudTest(common.FakeBpyModuleTestBase):

    module_name = "aud"

    def setUp(self):
        import aud

    def tearDown(self):
        sys.modules.pop(self.module_name)

    def test_nothing(self):
        print("[Test] Nothing")
