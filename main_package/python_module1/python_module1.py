"""A simple example class."""


class ModuleClass1(object):
    def __init__(self):
        print("Creating ModuleClass1 object.")

    def hello(self):
        print("Hello from the ModuleClass2 object contained in the python_module1!")


if __name__ == "__main__":
    stand_alone_obj = ModuleClass1()
    stand_alone_obj.hello()
