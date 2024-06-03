'''
#기본 블랙박스
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

#여행 모드 지원 블랙박스
class TravelBlackBox:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def set_travel_mode(self, min):
        print(str(min) + '분 동안 여행 모드 ON')

클래스 BlackBox 와 TravelBlackBox 의 메소드가 동일한대 위에 처럼 메소드를 계속 쓰기는 비효율
그래서
class TravelBlackBox(BlackBox):
이렇게 하면 BlackBox에 있는 메소드를 TravelBlackBox로 모두 물려받겠다는 의미
'''
#상속 후 코드
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class TravelBlackBox(BlackBox):
    def set_travel_mode(self, min):
        print(f'{self.name}'+str(min) + '분 동안 여행 모드 ON')
b1 = BlackBox('까망이', 200000)
b2 = TravelBlackBox('하양이', 100000)

#b1.set_travel_mode(20) 사용 불가
b2.set_travel_mode(10)