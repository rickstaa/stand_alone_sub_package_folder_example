"""A simple example class."""


class StandAloneClass(object):
    def __init__(self):
        print("Creating stand alone object.")

    def hello(self):
        print(
            "Hello from the stand alone object contained in the "
            "stand_alone_subpackage!"
        )


if __name__ == "__main__":
    stand_alone_obj = StandAloneClass()
    stand_alone_obj.hello()
