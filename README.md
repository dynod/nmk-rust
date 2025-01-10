# nmk-rust
Rust plugin for nmk build system

<!-- NMK-BADGES-BEGIN -->
[![License: MIT License](https://img.shields.io/github/license/dynod/nmk-rust)](https://github.com/dynod/nmk-rust/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/nmk-rust/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/nmk-rust/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/dynod/nmk?label=issues&query=is%3Aopen+is%3Aissue+label%3Aplugin%3Arust)](https://github.com/dynod/nmk/issues?q=is%3Aopen+is%3Aissue+label%3Aplugin%3Arust)
[![Supported python versions](https://img.shields.io/badge/python-3.9%20--%203.13-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/nmk-rust)](https://pypi.org/project/nmk-rust/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://astral.sh/ruff)
[![Code coverage](https://img.shields.io/codecov/c/github/dynod/nmk-rust)](https://app.codecov.io/gh/dynod/nmk-rust)
[![Documentation Status](https://readthedocs.org/projects/nmk-rust/badge/?version=stable)](https://nmk-rust.readthedocs.io/)
<!-- NMK-BADGES-END -->

This plugin adds support for [Rust](https://www.rust-lang.org/) development in an **`nmk`** project:
* VSCode settings generation (if [**`nmk-vscode`**](https://github.com/dynod/nmk-vscode) plugin is also used)
* **`cargo`** tool configuration and manifest files generation
* code format

## Usage

To use this plugin in your **`nmk`** project, insert this reference:
```
refs:
    - pip://nmk-rust!plugin.yml
```

## Documentation

This plugin documentation is available [here](https://nmk-rust.readthedocs.io/)

## Issues

Issues for this plugin shall be reported on the [main  **`nmk`** project](https://github.com/dynod/nmk/issues), using the **plugin:rust** label.
