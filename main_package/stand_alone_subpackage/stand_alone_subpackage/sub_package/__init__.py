import importlib
import sys

# # Import stand_alone_subpackage stand-alone package or name_space package
# if "stand_alone_subpackage" in sys.modules:
#     from stand_alone_subpackage.python_module.sub_package.python_module import (
#         StandAloneClass2,
#     )
# elif importlib.util.find_spec("stand_alone_subpackage") is not None:
#     StandAloneClass2 = getattr(
#         importlib.import_module("stand_alone_subpackage.sub_package.python_module"),
#         "StandAloneClass2",
#     )
# else:
#     StandAloneClass2 = getattr(
#         importlib.import_module(
#             "main_package.stand_alone_subpackage.stand_alone_subpackage.sub_package.python_module"
#         ),
#         "StandAloneClass2",
# )

from main_package.stand_alone_subpackage.stand_alone_subpackage.sub_package.python_module import (
    StandAloneClass2,
)
