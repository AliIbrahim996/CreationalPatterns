from conans import ConanFile, CMake, tools

class CreationalPatternsConan(ConanFile):
    name = "CreationalPatterns"
    version = "develop"

    # Optional metadata
    license = "(c) ALi Ibrahim"
    author = "Ali Ibrahim allosheribraheem38@gmail.com"
    url = "https://github.com/AliIbrahim996/CreationalPatterns.git"
    description = ""

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake", "visual_studio"
    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    scm = {
        "type": "git",
        "subfolder": "CreationalPatterns",
        "url": "https://github.com/AliIbrahim996/CreationalPatterns.git",
        "revision": "develop"
     }

    def build_requirements(self):
        self.build_requires("cmake/3.23.2")
        self.build_requires("doxygen/1.9.4")
        self.build_requires("gtest/cci.20210126")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["CreationalPatterns"]
