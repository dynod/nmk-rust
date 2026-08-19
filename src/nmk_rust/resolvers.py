"""
Resolvers logic for rust plugin
"""

from pathlib import Path

from nmk.model.resolver import NmkListConfigResolver


class RustSourcesResolver(NmkListConfigResolver):
    """
    Rust source files finder
    """

    def get_value(self, name: str, folder: str) -> list[Path]:  # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Find all rust source files in specified source folder

        :param name: config item name
        :param folder: root rust source folder
        :return: list of input rust files
        """

        # Iterate on source paths, and find all rust files
        return list(filter(lambda f: f.is_file(), Path(folder).rglob("*.rs")))


class RustIgnoredLockfileResolver(NmkListConfigResolver):
    """
    Rust ignored lockfile resolver
    """

    def get_value(self, name: str) -> list[str]:  # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Return the list of lockfiles to be ignored, depending if the project is locked or not
        """

        # Ignore Cargo.lock file if project is not locked
        if not self.model.env_backend.is_locked:
            return ["Cargo.lock"]
        return []  # pragma: no cover
