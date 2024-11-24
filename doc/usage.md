# Usage

To use this plugin in your **`nmk`** project, insert this reference in your **nmk.yml** main file:
```yaml
refs:
    - pip://nmk-rust!plugin.yml
```

```{note}
Note that **`cargo`** command is expected to be installed on the system to use this plugin.\
See [Install instructions](https://www.rust-lang.org/tools/install) for more information
```

Then you can start adding rust source files in your project **src** sub-folder.\
Once done, **`nmk`** build will:
* generate **`cargo`** tool configuration and manifest files

See [features](features.md) for more information.
