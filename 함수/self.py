'''
함수를 정의할 때 전달값이 두개면 함수 호출할 때도 전달값이 두개여야 하는데
클래스의 메소드는 self를 포함해서 전달값이 두 개라고 해도 호출할때는
self를 제외하고 나머지 전달값만 전달 됐었다
self = '객체 자기 자신'을 의미
self
1. 메소드를 정의할 때 처음 전달값은 반드시 self
2. 메소드 내에서는 self.name과 같은 형태로 멤버변수를 사용
3. 객체를 통해 메소드를 호출할 때 self 부분에 해당하는 전달값은 따로 명시하지 않는다
'''

'''
class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def set_travel_mode(self, min): #여행 모드 시간(분)
        print(str(min)+'분 동안 여행모드 ON')
b1 = BlackBox('까망이', 200000)
b1.set_travel_mode(20)
'''
# 위 코드에 set_travel_mode 메소드의 print부분을
# print(f'{self.name} {min}+'분 동안 여행모드 ON') 으로 변경

class BlackBox:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def set_travel_mode(self, min): #여행 모드 시간(분)
        print(f'{self.name}{min}분 동안 여행모드 ON')
b1 = BlackBox('까망이', 200000)
b2 = BlackBox('하양이', 100000)

#1번 코드
b1.set_travel_mode(20)
b2.set_travel_mode(10)
#2번 코드
BlackBox.set_travel_mode(b1,20)
BlackBox.set_travel_mode(b2,10)
#위 2개 코드 결과값 같음