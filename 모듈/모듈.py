'''
모듈 = 코드들이 작성되어 있는 하나의 파이썬 파일 , 예) 모듈.py
다른 파일을 가져다 쓰기 위해서는 두 가지 방법
1. import 모듈명 - 모듈 전체를 가져와서 모든 기능을 사용
2. from 모듈 import 변수, 함수, 클래스 - 모듈 필요한거 일부 기능만 가져와서 사용
'''
#1번 방법
import goodjob
goodjob.say()

#2번 방법
from goodjob import say
say()

# 구글에 list of python modules 검색
# 파이썬에서 기본으로 제공되는 수 많은 모듈 중 대표적인 하나 random으로 가위바위보 만들기
import random
my_list = ['가위','바위','보']
print(random.choice(my_list))
