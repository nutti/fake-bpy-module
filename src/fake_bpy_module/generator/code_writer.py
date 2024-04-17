import io
import subprocess
from typing import List
from yapf.yapflib.yapf_api import FormatCode


class CodeWriterIndent:
    indent_stack: List[int] = [0]

    def __init__(self, indent: int = 0, append_current_indent: bool = False):
        self._indent: int = indent
        self._append_current_indent = append_current_indent

    def __enter__(self):
        cls = self.__class__
        cls.add_indent(self._indent, self._append_current_indent)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        cls = self.__class__
        cls.remove_indent()

    @classmethod
    def reset_indent(cls):
        cls.indent_stack = [0]

    @classmethod
    def add_indent(cls, indent: int = 0, append_current_indent: bool = False):
        if append_current_indent:
            if len(cls.indent_stack) == 0:
                cls.indent_stack.append(indent)
            else:
                cls.indent_stack.append(cls.indent_stack[-1] + indent)
        else:
            cls.indent_stack.append(indent)

    @classmethod
    def remove_indent(cls):
        cls.indent_stack.pop()

    @classmethod
    def current_indent(cls) -> int:
        return cls.indent_stack[-1]


class CodeWriter:
    INDENT = "    "

    def __init__(self):
        self._code_data: io.StringIO = io.StringIO()
        self._buffer: io.StringIO = io.StringIO()
        CodeWriterIndent.reset_indent()

    def add(self, code: str, new_line: bool = False):
        self._buffer.write(code)
        if new_line:
            indent = CodeWriterIndent.current_indent()
            self._code_data.write(self.INDENT * indent)
            self._code_data.write(self._buffer.getvalue())
            self._code_data.write("\n")
            self._buffer = io.StringIO()

    def addln(self, code: str):
        self.add(code, True)

    def new_line(self, num: int = 1):
        if self._buffer.tell() > 0:
            indent = CodeWriterIndent.current_indent()
            self._code_data.write(self.INDENT * indent)
            self._code_data.write(self._buffer.getvalue())
            self._buffer = io.StringIO()
        self._code_data.write("\n" * num)

    def write(self, file: io.TextIOWrapper):
        file.write(self._code_data.getvalue())

    def get_data_as_string(self) -> str:
        return self._code_data.getvalue()

    def reset(self):
        self._code_data = io.StringIO()
        self._buffer = io.StringIO()
        CodeWriterIndent.reset_indent()

    def format(self, style_config: str, file_format: str):
        if style_config == "yapf":
            self._code_data = io.StringIO(FormatCode(
                self._code_data.getvalue(), style_config="pep8")[0])
        elif style_config == "ruff":
            self._code_data = io.StringIO(subprocess.check_output(
                [
                    "ruff",
                    "format",
                    "--isolated",
                    f"--stdin-filename=_.{file_format}",
                ],
                input=self._code_data.getvalue().encode(),
            ).decode())
        elif style_config == "none":
            pass
        else:
            raise ValueError(f"Invalid style config: {style_config}")
