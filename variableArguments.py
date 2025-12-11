class Point:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0]
            self.y = 0
        elif len(args) == 2:
            self.x, self.y = args
        else:
            raise TypeError("Expected 1 or 2 arguments")


Point(5)
Point(3, 4)