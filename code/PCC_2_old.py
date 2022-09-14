

class Circle:

    def __init__(self, radius):

        self.r = radius  # Radius of circle
        self._t = 10
        self.__y = 100

    def area(self):

        return self.r ** 2 * 3.14

    def perimeter(self):

        return 2 * 3.14 * self.r




class ComparableCircle(Circle):

    def __init__(self, r):
        Circle.__init__(self, r)

    def dummyfunction(self, type_):
        """
        Function to print type of circles
        :param type: Type of circle
        :return: Print
        """
        print(type_)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.r == other.r

    def __le__(self, other):
        return isinstance(other, self.__class__) and self.r <= other.r



