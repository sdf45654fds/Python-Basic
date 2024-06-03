'''
기본 블랙박스
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

여행 모드 지원 블랙박스(저장공간 변수 추가)
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        self.name = name
        self.price = price
        self.sd = sd #sd 카드 (64 or 128)

    def set_travel_mode(self, min): #여행 모드 시간(분)
        print(str(min)+'분 동안 여행모드 ON')
상속을 이용하고 추가로 확장 가능
'''
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
#추가
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        BlackBox.__init__(self, name, price) #추가
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')

#super() 사용  super()는 부모객체란 뜻
class TravelBlackBox(BlackBox):
    def __init__(self, name, price, sd):
        super().__init__(name, price) # self 사용 x
        self.sd = sd
    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')