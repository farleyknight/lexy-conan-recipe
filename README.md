# lexy-conan-recipe

This `conanfile.py` builds a local package for the `lexy` project:

https://github.com/foonathan/lexy

The author suggests using CMake to package `lexy`, but I prefer `conan`. 

## Usage

1) Clone this repo.

```bash
▶ git clone https://github.com/farleyknight/lexy-conan-recipe
```

2) Change into the newly cloned repo, and run `conan source .` inside this repo. 
This step should clone the latest `lexy` GitHub repo into the current directory.

```bash
▶ cd lexy-conan-recipe
▶ conan source .
▶ conan install .
```

Verify:

```bash
▶ ls -1A
README.md
conanfile.py
lexy
```

3) Build the local package.

```bash
▶ conan install .
▶ conan build .
▶ conan export-pkg .
```

4) Use `lexy/0.0.0` as a local package for other projects:

```python
from conans import ConanFile, CMake, tools

class MyParserProject(ConanFile):
    requires = "lexy/0.0.0", ...
    ...
```

5) Verify the package was locally installed:

```bash 
▶ conan search
Existing package recipes:

...
lexy/0.0.0
...
```

6) Run `conan install .` from within your other project:

```bash
▶ cd my_parser_project
▶ conan install .
```

## Potential Issue

One potential issue is that `lexy` has no versioning. All development of `lexy` leaves it at `0.0.0`. This seems to prefer by the author.

Because of that, any effort to add versioning at the `conan` package won't worth.

Therefore, anyone using this recipe should be ready to (re-)run step 3 with `conan export-pkg . --force`. This will repackage `lexy` with the latest code but still stay at the `0.0.0` version number.
