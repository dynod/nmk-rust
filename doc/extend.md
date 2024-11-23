# Configuration Extension

As for all **`nmk`** projects config items, [**`nmk-rust`** ones](config.md) are all overridable by other plug-ins and project files. But the ones described on this page are specifically designed to be extended.

## Cargo configuration

Cargo config and manifest files generation can be configured by rust projects.

Following config items may be extended for that purpose:

* **{ref}`${rustConfigFileFragments}<rustConfigFileFragments>`**: additional cargo configuration file fragments
* **{ref}`${rustConfigFileItems}<rustConfigFileItems>`**: additional cargo configuration items
* **{ref}`${rustManifestFileFragments}<rustManifestFileFragments>`**: additional cargo manifest file fragments
* **{ref}`${rustManifestFileItems}<rustManifestFileItems>`**: additional cargo manifest items
