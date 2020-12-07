"""Setup file for the 'main_package' python package. Which contains a trick to create
the shortened namespaces.
"""

from collections import OrderedDict
from setuptools import setup, find_namespace_packages, find_packages
import re

# Add extra virtual shortened package for each folder module of namespace_pkgs (NAME_SPACE_VERSION)
# NOTE: This only works if you remove the __init__.py file from the parent folder.
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

# # Add extra virtual shortened package for each folder module of the stand-alone submodule (NORMAL PACKAGE VERSION)
# # NOTE: This only works if you have a __init__.py file in all of the submodule folders.
# PACKAGES = find_packages(include=["main_package*"])
# stand_alone_packages = ["stand_alone_subpackage"]
# exclusions = r"|".join(
#     [r"\." + item + r"\.(?=" + item + r".)" for item in stand_alone_packages]
# )
# PACKAGE_DIR = {}
# for package in PACKAGES:
#     sub_tmp = re.sub(exclusions, ".", package)
#     if sub_tmp is not package:
#         PACKAGE_DIR[sub_tmp] = package.replace(".", "/")
# PACKAGES.extend(PACKAGE_DIR.keys())
# print(PACKAGES)
# print(PACKAGE_DIR)

# Run python setup
setup(
    packages=PACKAGES, package_dir=PACKAGE_DIR,
)
