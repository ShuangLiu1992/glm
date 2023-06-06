from conan import ConanFile
import conan.tools.files
from conan.tools.cmake import CMake, CMakeToolchain


class GLMConan(ConanFile):
    name = "glm"
    settings = "os", "compiler", "build_type", "arch"

    def export_sources(self):
        conan.tools.files.copy(self, "*", self.recipe_folder, self.export_sources_folder)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables['BUILD_TESTING'] = False
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.defines = ["GLM_ENABLE_EXPERIMENTAL"]
        if self.settings.os == "Macos":
            self.cpp_info.defines.append("GL_SILENCE_DEPRECATION")
