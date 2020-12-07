"""A simple example class."""


class ModuleClass2(object):
    def __init__(self):
        print("Creating ModuleClass2 object.")

    def hello(self):
        print("Hello from the ModuleClass2 object contained in the python_module2!")


if __name__ == "__main__":
    stand_alone_obj = ModuleClass2()
    stand_alone_obj.hello()
