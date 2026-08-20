"""
Resolvers logic for rust plugin
"""

import re
from pathlib import Path

from nmk.model.resolver import NmkListConfigResolver, NmkStrConfigResolver

_INCREMENT_PATTERN = re.compile("[0-9](.[0-9])?(.[0-9])?")
"""
Version increment verification pattern
"""


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


class RustVersionResolver(NmkStrConfigResolver):
    """
    Rust package version resolver
    """

    def get_value(self, name: str, increment: str, base_version: str) -> str:  # pyright: ignore[reportIncompatibleMethodOverride]
        """
        Get resolved version value.
        Behavior of the version resolution is:
          * take base_version (gitVersion config item)
          * if this is a tagged version, simply use it
          * otherwise deduce last tag and increment it with increment

        :param name: config item name to be resolved
        :param increment: version increment to be used
        :param base_version: base version to be used
        :return: resolved version
        """

        # Check version segments
        segments = base_version.split("-")
        rust_version = segments[0]
        if len(segments) == 1:
            # This is a tagged version: use it directly
            return rust_version

        # Not on a tagged version: let's predict the next one with provided increment
        assert _INCREMENT_PATTERN.match(increment) is not None, f"Invalid rustVersionIncrement format: {increment}"

        # Build predicted version
        rust_version_digits = [int(i) for i in rust_version.split(".")]
        increment_digits = [int(i) for i in increment.split(".")]
        assert len(rust_version_digits) == len(increment_digits), (
            f"Not the same digits count between version deduced from gitVersion ({rust_version}) and rustVersionIncrement ({increment})"
        )
        out_string = ""
        increment_found = False
        for d1, d2 in zip(rust_version_digits, increment_digits, strict=True):
            # One more digit
            if len(out_string):
                out_string += "."

            # Increment?
            if d2 > 0:
                # Incremented digit found: do it
                out_string += str(d1 + d2)
                increment_found = True
            elif not increment_found:
                # Incremented digit not found yet: just keep original digit
                out_string += str(d1)
            else:
                # Post-increment digit: set them all to 0
                out_string += "0"

        return out_string
