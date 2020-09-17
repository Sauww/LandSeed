import setuptools
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for dir in directories:
            paths.append(os.path.join(path.replace('LandSeed/', ''),dir, "*"))
    return paths

extra_files = package_files('LandSeed/data')
print(extra_files)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LandSeed", # Replace with your own username
    version="1.0.0",
    author="Bastien Zigmann",
    author_email="bastien@zigmann.org",
    description="Procedural terrain shader generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sauww/LandSeed",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.0',
    install_requires=[
        'numpy>=1.18.1',
        'glfw>=1.11.1',
        'PyOpenGL>=3.1.5'
    ],
    entry_points = {
        "console_scripts": [
            "LandSeed=LandSeed.LandSeed:generate"
            #"LandSeed_UpdateDoc=LandSeed.UpdateDoc:main" # laisser ça? Comment faire pour pouvoir executer en local pour les devs?
        ]
    },
    include_package_data=True,
    package_data={'':extra_files+["input/demo*.frag"],},
)

# TODO :
#  - check classifier
