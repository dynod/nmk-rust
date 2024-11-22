from pathlib import Path

from nmk.tests.tester import NmkBaseTester

import nmk_rust


class TestRustPluginVersion(NmkBaseTester):
    @property
    def templates_root(self) -> Path:
        return Path(__file__).parent / "templates"

    def test_plugin_version(self):
        self.nmk(self.prepare_project("ref_rust.yml"), extra_args=["version"])
        self.check_logs(f"-  👉 nmk-rust: {nmk_rust.__version__}")
