# lexy-conan-recipe

This `conanfile.py` builds a local package for the `lexy` project:

https://github.com/foonathan/lexy

The author suggests using CMake to package `lexy`, but I prefer `conan`. 

## Usage 

1) Clone this repo.

```bash
$ git clone https://github.com/farleyknight/lexy-conan-recipe
```

2) Change into the newly cloned repo, and run `conan source .` inside this repo. 
This step should clone the latest `lexy` GitHub repo into the current directory.

```bash
$ cd lexy-conan-recipe
$ conan source .
```

3) Build the local package.

```bash
$ conan build .
$ conan export-pkg .
```

4) Use `lexy/0.0.0` as a local package for other projects:

```python
from conans import ConanFile, CMake, tools

class MyParserProject(ConanFile):
    requires = "lexy/0.0.0", ...
    ...
```

## Potential Issue

One potential issue is that `lexy` has no versioning. All development of `lexy` leaves it at `0.0.0`. 

Because of that, any effort to add versioning would need to be supported by the author. Be ready to run step 3 with `conan export-pkg . --force` to force an update with the same version number.
