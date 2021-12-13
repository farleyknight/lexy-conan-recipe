from conans import ConanFile, CMake, tools

class LexyConan(ConanFile):
    name = "lexy"
    version = "0.0.0"
    license = "Boost Software License 1.0"
    settings = "os", "compiler", "build_type", "arch"
    url = "http://github.com/farleyknight/lexy-conan-recipe"
    description = "Conan package for lexy project - https://github.com/foonathan/lexy.git"

    def source(self):
        lexy_github_project = "https://github.com/foonathan/lexy.git"
        git = tools.Git(folder="lexy")
        git.clone(lexy_github_project)

    def build(self):
        cmake = CMake(self)
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="lexy/include")
