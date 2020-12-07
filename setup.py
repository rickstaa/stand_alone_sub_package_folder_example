"""Setup file for the 'main_package' python package. Which contains a trick to create
the shortened namespaces.
"""

from setuptools import setup, find_namespace_packages
import re

# Add extra virtual shortened package for each of namespace_pkgs
PACKAGES = find_namespace_packages(include=["main_package*"])
namespace_pkgs = ["stand_alone_subpackage"]
exclusions = r"|".join(
    [r"\." + item + r"\.(?=" + item + r".)" for item in namespace_pkgs]
)
PACKAGE_DIR = {}
for package in PACKAGES:
    sub_tmp = re.sub(exclusions, ".", package)
    if sub_tmp is not package:
        PACKAGE_DIR[sub_tmp] = package.replace(".", "/")
PACKAGES.extend(PACKAGE_DIR.keys())

# Run python setup
setup(
    packages=PACKAGES, package_dir=PACKAGE_DIR,
)
