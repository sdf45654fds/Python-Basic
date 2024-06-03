'''
class BlackBox:
    def __init__(self,name,price):
        self.name = name 
        self.price = price 
b1 = BlackBox('까망이', 200000)
b2 = BlackBox('하양이', 100000)

self.name , self.price 는 멤버 변수다
pass 대신 def__init__(self,변수,변수): 를 적는다 
객체가 생성될 때 자동으로 실행됨

'''
class BlackBox: #변수명은 대문자
    def __init__(self,name,price):
        self.name = name 
        self.price = price 
b1 = BlackBox('까망이', 200000)
print(b1.name, b1.price)
b2 = BlackBox('하양이', 100000)
print(b2.name,b2.price)
