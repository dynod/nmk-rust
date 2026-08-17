from pathlib import Path

from buildenv.extension import BuildEnvRenderer
from jinja2 import Environment, PackageLoader
from nmk_base._buildenv.template import NmkBaseProjectTemplate, NmkConfigType, NmkReference

_ENV = Environment(loader=PackageLoader("nmk_rust"))
_SRC_PATH = Path("src")


class NmkRustProjectTemplate(NmkBaseProjectTemplate):
    """
    Template for **nmk-rust** plugin project
    """

    @property
    def weight(self) -> int:
        # Top level plugin weight
        return 300

    @property
    def references(self) -> list[NmkReference]:
        return super().references + [NmkReference("nmk-rust!plugin.yml", ["nmk-base!plugin.yml"])]

    @property
    def description(self) -> str:
        return "rust nmk project"

    @property
    def generated_files(self) -> set[Path]:
        return super().generated_files | set(
            [
                Path("Cargo.toml"),
                Path(".rustfmt.toml"),
                Path(".cargo") / "config.toml",
                _SRC_PATH / "main.rs",
            ]
        )

    @property
    def post_generation_tasks(self) -> list[str]:
        return super().post_generation_tasks + ["rust.config", "rust.fmtcfg", "rust.manifest"]

    @property
    def comments(self) -> dict[str, str]:
        return super().comments | {
            "config.rustDependencies": "\nPackage dependencies (crates, from crates.io)",
            "config.venvPkgDeps": "\nExtra tools dependencies",
            "config.venvArchiveDeps": "\nExtra tools dependencies (from local files)",
        }

    def generate_extra_files(self, renderer: BuildEnvRenderer):
        # Generate source code templates
        renderer.render(_ENV, "src/main.rs.jinja", sub_path=_SRC_PATH)

    @property
    def config_items(self) -> dict[str, NmkConfigType]:
        items = dict(super().config_items)
        items.update(
            {
                "rustDependencies": {},
            }
        )
        return items
