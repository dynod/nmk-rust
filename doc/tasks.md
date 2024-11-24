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

(rust.fmtcfg)=
### **`rust.fmtcfg`** -- rustfmt config file generation

This task generates the **{ref}`${rustFormatFile}<rustFormatFile>`** **`rustfmt`** [configuration file](https://rust-lang.github.io/rustfmt/).

| Property | Value/description |
|-         |-
| builder  | [nmk_base.common.TomlFileBuilder](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.TomlFileBuilder)
| input    | {ref}`${rustFormatFileFragments}<rustFormatFileFragments>` files
| output   | {ref}`${rustFormatFile}<rustFormatFile>` file
| if       | {ref}`${rustSrcFiles}<rustSrcFiles>` are found

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| fragment_files | **{ref}`${rustFormatFileFragments}<rustFormatFileFragments>`**
| items | **{ref}`${rustFormatFileItems}<rustFormatFileItems>`**
| plugin_name | "nmk-rust"

## Build tasks

All tasks in this chapter are dependencies of the base [**`build`**](https://nmk-base.readthedocs.io/en/stable/tasks.html#build-task) task.

(rust.format)=
### **`rust.format`** -- Format rust code files

This task calls the **`cargo fmt`** command (alias to [**`rustfmt tool`**](https://github.com/rust-lang/rustfmt)) to format rust code files.

| Property | Value/description |
|-         |-
| builder  | [nmk_base.common.ProcessBuilder](https://nmk-base.readthedocs.io/en/stable/autoapi/nmk_base/common/index.html#nmk_base.common.ProcessBuilder)
| input    | {ref}`${rustSrcFiles}<rustSrcFiles>` files
| output   | {ref}`${rustFormatStampFile}<rustFormatStampFile>` file
| if       | {ref}`${rustSrcFiles}<rustSrcFiles>` are found

The builder is called with the following parameters mapping:

| Name | Value |
|- |-
| cmd | ["cargo", "fmt", **{ref}`${rustFormatExtraArgs}<rustFormatExtraArgs>`**]
