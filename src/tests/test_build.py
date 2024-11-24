import subprocess

from tests.common import TestRustPlugin


class TestRustPluginBuild(TestRustPlugin):
    def test_format(self, monkeypatch):
        # Patch subprocess
        monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: subprocess.CompletedProcess(args, 0, "", ""))

        # Call format task
        prj = self.prepare_rust_project()
        self.nmk(prj, extra_args=["rust.format"])
        assert (self.test_folder / "out" / ".rustfmt").is_file()
