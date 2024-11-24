from tests.common import TestRustPlugin


class TestRustPluginFiles(TestRustPlugin):
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

    def test_generate_format(self):
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["rust.fmtcfg"])
        assert (self.test_folder / ".rustfmt.toml").is_file()
