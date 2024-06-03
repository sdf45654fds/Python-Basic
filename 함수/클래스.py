'''
어떤 클래스로부터 만들어진 객체는 그 클래스의 인스턴스 입니다
설계도와 설명서를 합친 정도의 개념
여러 변수 포함 o, 기능 정의 o
클래스를 통해 만들어지는 제품을 객체 , 각 객체는 그 클래스의 인스턴스라고 한다

class 클래스명:
    pass
'''
class BlackBox: #변수명은 대문자
    pass
b1 = BlackBox() #b1이라는 객체 생성
b1.name = '까망이' #변수 선언
print(b1.name)
print(isinstance(b1,BlackBox)) #b1 객체가 BlackBox의 인스턴스가 맞는지 확인
