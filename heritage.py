from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def ini(self):
        pass

class B(A):
    def start(self):
        print("start")
        self.ini()
    def ini(self):
        print('ini')


if __name__=="__main__":
    b = B()
    b.start()
    print("b instanceob B : {}".format(isinstance(b,B)))
    print("b instanceob A : {}".format(isinstance(b,A)))
    print("b.__class__ issubclass A : {}".format(issubclass(b.__class__,A)))
    print("B issubclass A : {}".format(issubclass(B,A)))