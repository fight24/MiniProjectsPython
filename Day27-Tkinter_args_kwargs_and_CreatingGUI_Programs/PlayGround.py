def add(*args):
    s = 0
    for n in args:
        s += n
    print(s)


add(1, 2, 3)
''' *args được sử dụng để truyền một danh sách các đối số không theo tên vào một hàm. Nó cho phép bạn xử lý một số lượng 
 không xác định các đối số được truyền vào hàm như một tuple. '''
# **kwargs: Many Keyworded Arguments
''' **kwargs được sử dụng để truyền một số lượng không xác định các đối số theo tên vào một hàm.
 Nó cho phép bạn xử lý các đối số này như một từ điển (dictionary). '''


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")
        print(kw)


my_car = Car(make="Nissan")
print(my_car)
