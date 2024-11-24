import nmk_rust
from tests.common import TestRustPlugin


class TestRustPluginVersion(TestRustPlugin):
    def test_plugin_version(self):
        self.nmk(self.prepare_project("ref_rust.yml"), extra_args=["version"])
        self.check_logs(f"-  👉 nmk-rust: {nmk_rust.__version__}")
