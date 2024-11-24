# Contributions

The **`nmk-rust`** plugin contributes to **`nmk`** features as described below.

## Plugin information

As other plugins, **`nmk-rust`** registers its version and documentation link in [plugin information config items](https://nmk-base.readthedocs.io/en/stable/extend.html#plugin-information).

## System dependencies

**`nmk-rust`** plugin explicitely requires **`cargo`** command to be installed, by contributing to [systemDeps config](https://nmk-base.readthedocs.io/en/stable/extend.html#system-dependencies)

## VSCode extensions

**`nmk-rust`** plugin [recommends](https://nmk-vscode.readthedocs.io/en/stable/extend.html#extensions) usage of following VSCode extensions: 
* [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) for generic rust support
* [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) for toml support

> **Note:** enabled only if [**`nmk-vscode`** plugin](https://nmk-vscode.readthedocs.io/) is used in the nmk project
