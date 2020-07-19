import os

from . import common
from fake_bpy_module.utils import (
    check_os,
    output_log,
    remove_unencodable,
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_INFO,
    LOG_LEVEL_NOTICE,
    LOG_LEVEL_WARN,
    LOG_LEVEL_ERR,
)


class UtilsTest(common.FakeBpyModuleTestBase):

    name = "UtilsTest"
    module_name = __module__

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_check_os(self):
        to_osname = {
            "nt": "Windows",
            "posix": "Linux",
        }

        self.assertEqual(check_os(), to_osname[os.name])

    def test_output_log(self):
        output_log(LOG_LEVEL_DEBUG, "Debug")
        output_log(LOG_LEVEL_INFO, "Info")
        output_log(LOG_LEVEL_NOTICE, "Notice")
        output_log(LOG_LEVEL_WARN, "Warning")
        output_log(LOG_LEVEL_ERR, "Error")

    def test_remove_unencodable(self):
        original_string = "\xb2AAA\u2013BBB\u2019"
        expect = "AAABBB"

        actual = remove_unencodable(original_string)

        self.assertEqual(expect, actual)
