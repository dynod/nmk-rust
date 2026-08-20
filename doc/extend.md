# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-rust`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

## Cargo configuration

Cargo config and manifest files generation can be configured by rust projects.

Following config items may be extended for that purpose:

- **{ref}`${rustConfigFileFragments}<rustConfigFileFragments>`**: additional cargo configuration file fragments
- **{ref}`${rustConfigFileItems}<rustConfigFileItems>`**: additional cargo configuration items
- **{ref}`${rustManifestFileFragments}<rustManifestFileFragments>`**: additional cargo manifest file fragments
- **{ref}`${rustManifestFileItems}<rustManifestFileItems>`**: additional cargo manifest items

## Rust package

The rust package handled by an **`nmk-rust`** project can be configured using the following items:

- **{ref}`${rustPackage}<rustPackage>`**: rust package name
- **{ref}`${rustVersion}<rustVersion>`**: rust package version (to override automated next version guess from last git tag)
- **{ref}`${rustEdition}<rustEdition>`**: rust edition to be used in generated manifest file
- **{ref}`${rustDependencies}<rustDependencies>`**: rust package operational dependencies (names and versions)
- **{ref}`${rustDevDependencies}<rustDevDependencies>`**: rust package development dependencies (names and versions)
- **{ref}`${rustBuildDependencies}<rustBuildDependencies>`**: rust package build dependencies (names and versions)

## Code format

To fine-tune code format of rust source files, an **`nmk-rust`** project can be configured using the following items:

- **{ref}`${rustLineLength}<rustLineLength>`**: rust code line length
- **{ref}`${rustFormatFileFragments}<rustFormatFileFragments>`**: additional rustfmt config file fragments
- **{ref}`${rustFormatFileItems}<rustFormatFileItems>`**: additional rustfmt config items
- **{ref}`${rustFormatExtraArgs}<rustFormatExtraArgs>`**: extra arguments for **`cargo fmt`** command

## Dependencies fetching

To fine-tune rust package dependencies fetching, an **`nmk-rust`** project can be configured using the following items:

- **{ref}`${rustFetchExtraArgs}<rustFetchExtraArgs>`**: extra arguments for **`cargo fetch`** command

## Compilation

To fine-tune rust code compilation, an **`nmk-rust`** project can be configured using the following items:

- **{ref}`${rustBuildExtraArgs}<rustBuildExtraArgs>`**: extra arguments for **`cargo build`** command
