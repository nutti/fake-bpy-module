import unittest
from pathlib import Path

LOG_DIR = "fake_bpy_module_test.log"


class FakeBpyModuleTestBase(unittest.TestCase):

    name = None
    module_name = None
    log_dir = None
    file_ = None

    @classmethod
    def setUpClass(cls: type['FakeBpyModuleTestBase']) -> None:
        if cls.module_name is None:
            raise ValueError("module_name must set")
        if cls.name is None:
            raise ValueError("name must set")

        cls.log_dir = f"{LOG_DIR}/{cls.module_name}"
        Path(cls.log_dir).mkdir(parents=True, exist_ok=True)

        filename = f"{cls.log_dir}/{cls.name}.log"
        cls.file_ = Path(filename).open("w", encoding="utf-8")   # pylint: disable=R1732  # noqa: SIM115

    @classmethod
    def tearDownClass(cls: type['FakeBpyModuleTestBase']) -> None:
        cls.file_.close()

    def setUp(self) -> None:
        self.maxDiff = None     # pylint: disable=C0103
        self.log(f"========== Test: {self.id()} ==========")

    def tearDown(self) -> None:
        pass

    def log(self, message: str) -> None:
        self.__class__.file_.write(message + "\n")
