import nmk_rust
from tests.common import TestRustPlugin


class TestRustPluginVersion(TestRustPlugin):
    def test_plugin_version(self):
        self.nmk(self.prepare_project("ref_rust.yml"), extra_args=["version"])
        self.check_logs(f"-  👉 nmk-rust: {nmk_rust.__version__}")

    def test_check_version_tag(self):
        # Check version with tagged version
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["--config", "gitVersion=1.2.3", "--print", "rustVersion"])
        self.check_logs('Config dump: { "rustVersion": "1.2.3" }')

    def test_check_version_increment_a(self):
        # Check version with increment version
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["--config", "gitVersion=1.2.3-3-g1234567", "--config", "rustVersionIncrement=1.0.0", "--print", "rustVersion"])
        self.check_logs('Config dump: { "rustVersion": "2.0.0" }')

    def test_check_version_increment_b(self):
        # Check version with increment version
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["--config", "gitVersion=1.2.3-3-g1234567", "--config", "rustVersionIncrement=0.1.0", "--print", "rustVersion"])
        self.check_logs('Config dump: { "rustVersion": "1.3.0" }')

    def test_check_version_increment_c(self):
        # Check version with increment version
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["--config", "gitVersion=1.2.3-3-g1234567", "--config", "rustVersionIncrement=0.0.1", "--print", "rustVersion"])
        self.check_logs('Config dump: { "rustVersion": "1.2.4" }')
