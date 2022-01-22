"""Setup the package."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Krijg het versienummer:
import re
VERSIONFILE = "predcontrol_sf/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

requirements = ['pandas',
                'lightgbm'
                ]

setuptools.setup(
    name="predcontrol_sf",
    version=verstr,
    author="Sjoerd Gnodde",
    description="Predict streamflow and divide in an optimal way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SjoerdGn/str-flow-pred-and-control",
    packages=['predcontrol_sf'],
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: All rights reserved",
        "Operating System :: OS Independent",
        'Development Status :: 3 - Alpha'
    ],
    python_requires='>=3.6',
)
