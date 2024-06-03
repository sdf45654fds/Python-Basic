'''
set_travel_mode() 메소드의 동작 요구사항
주어진 시간동안 여행모드로 설정하는 것 여행용 영상을 따로 관리하는 건 좋은데
시간이 지나면 자동으로 추억용 영상을 제작하고 메일까지 보내기를 원함
개선버전 AdvancedTravelBlackBox(): 을 만들기
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
        print(str(min)+'분 동안 여행모드 ON') #이름 추가하려면 (f'{self.name}' + str(min)+'분 동안 여행모드 ON')
'''
set_travel_mode가 실행 되었을 때 단순히 여행 모드만 지원하는게 아니라 영상 제작 및 메일 발송까지
부모 클래스의 
def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON')
이 메소드를 자식클래스(AdvanceTrabelBlackBox)에서 재정의 할 수 있다

자식 클래스에서 같은 메소드를 새로 정의하지 않으면? 부모 클래스의 메소드를, 쓰게 되고
자식 클래스에서 같은 메소드를 새로 정의하면? 자식 클래스의 메소드를 쓰게 됨
= 이것을 메소드 오버라이딩이라고 한다! 메소드를 새로 정의하는 것
'''
class AdvanceTrabelBlackBox(TravelBlackBox): #개선 버전 메소드 생성
    def set_travel_mode(self, min):
        print(str(min)+'분 동안 여행모드 ON') #이름 추가하려면 (f'{self.name}' + str(min)+'분 동안 여행모드 ON')
        self.make() #추억용 여행 영상 제작
        self.send() #메일 발송

b1 = TravelBlackBox('하양이', 100000, 64)
b1.set_travel_mode(20)

b2 = AdvanceTrabelBlackBox('초록이', 120000, 64)
b2.set_travel_mode(15)