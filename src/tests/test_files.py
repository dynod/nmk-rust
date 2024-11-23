import shutil
from pathlib import Path

from nmk.tests.tester import NmkBaseTester


class TestRustPluginVersion(NmkBaseTester):
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

    def test_found_files(self):
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["--print", "rustSrcFiles"])
        self.check_logs(
            f'Config dump: {{ "rustSrcFiles": [ "{self.escape(self.test_folder / "src" / "main.rs")}" ] }}'  # NOQA: B028
        )

    def test_generate_config(self):
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["rust.config"])
        assert (self.test_folder / ".cargo" / "config.toml").is_file()

    def test_generate_manifest(self):
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["rust.manifest"])
        assert (self.test_folder / "Cargo.toml").is_file()
