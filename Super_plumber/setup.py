from cx_Freeze import setup, Executable

setup(
    name = "Super_Plumber",
    version = "1.0",
    description = "Super_Plumber",
    executables = [Executable("main.py")]
)