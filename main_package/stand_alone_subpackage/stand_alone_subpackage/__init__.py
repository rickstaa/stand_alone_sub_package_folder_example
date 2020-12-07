import importlib
import sys

# Import stand_alone_subpackage stand-alone package or name_space package
if "stand_alone_subpackage" in sys.modules:
    from stand_alone_subpackage.python_module import StandAloneClass
elif importlib.util.find_spec("stand_alone_subpackage") is not None:
    Oscillator = getattr(
        importlib.import_module("stand_alone_subpackage.python_module"),
        "StandAloneClass",
    )
else:
    Oscillator = getattr(
        importlib.import_module(
            "main_package.stand_alone_subpackage.stand_alone_subpackage.python_module"
        ),
        "StandAloneClass",
    )
