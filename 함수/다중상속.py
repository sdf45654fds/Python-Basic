'''

'''
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')

#메일 발송 기능 구현 클래스
class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox, VideoMaker, MailSender): #상속 클래스 추가 = 다중상속
    def __init__(self, name, price, sd):
        super().__init__(name, price)
        self.sd = sd

    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')

b1 = TravelBlackBox('하양이', 100000, 64) #name, price, sd
b1.make()
b1.send()