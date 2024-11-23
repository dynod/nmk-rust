# Tasks

The **`nmk-rust`** plugin defines the tasks described below.

## Setup tasks

All tasks in this chapter are dependencies of the base [**`setup`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#setup-task) task.

(rust.config)=
### **`rust.config`** -- Cargo config file generation

This task generates the **{ref}`${rustConfigFile}<rustConfigFile>`** **`cargo`** [configuration file](https://doc.rust-lang.org/cargo/reference/config.html).

| Property | Value/description |
|-         |-
| builder  | [nmk_base.common.TomlFileBuilder](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TomlFileBuilder)
| input    | {ref}`${rustConfigFileFragments}<rustConfigFileFragments>` files
| output   | {ref}`${rustConfigFile}<rustConfigFile>` file
| if       | {ref}`${rustSrcFiles}<rustSrcFiles>` are found

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| fragment_files | **{ref}`${rustConfigFileFragments}<rustConfigFileFragments>`**
| items | **{ref}`${rustConfigFileItems}<rustConfigFileItems>`**
| plugin_name | "nmk-rust"

(rust.manifest)=
### **`rust.manifest`** -- Cargo manifest file generation

This task generates the **{ref}`${rustManifestFile}<rustManifestFile>`** **`cargo`** package [manifest file](https://doc.rust-lang.org/cargo/reference/manifest.html).

| Property | Value/description |
|-         |-
| builder  | [nmk_base.common.TomlFileBuilder](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TomlFileBuilder)
| input    | {ref}`${rustManifestFileFragments}<rustManifestFileFragments>` files
| output   | {ref}`${rustManifestFile}<rustManifestFile>` file
| if       | {ref}`${rustSrcFiles}<rustSrcFiles>` are found

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| fragment_files | **{ref}`${rustManifestFileFragments}<rustManifestFileFragments>`**
| items | **{ref}`${rustManifestFileItems}<rustManifestFileItems>`**
| plugin_name | "nmk-rust"
