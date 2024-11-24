import shutil
from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestRustPlugin(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def prepare_rust_project(self) -> Path:
        # Prepare rust project with single source file
        src_dir = self.test_folder / "src"
        src_dir.mkdir(exist_ok=True)
        source_template = self.template("main.rs")
        shutil.copyfile(source_template, src_dir / source_template.name)
        return self.prepare_project("ref_rust.yml")

    def escape(self, to_escape: Path) -> str:
        # Escape backslashes (for Windows paths in json print)
        return str(to_escape).replace("\\", "\\\\")
