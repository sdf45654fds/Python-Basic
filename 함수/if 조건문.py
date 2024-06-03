'''
--if조건-- 만약 ~라면
if 조건 다음에 콜론(:)을 적어준다
다음 줄에는 이 조건이 참일 때 실행할 문장을 적는다. !!주의!! 들여쓰기를 꼭 해야함 스페이스4번,탭1번

#True 일시
if조건:
    이문장
다음 문장

#False 일시
if조건:
다음 문장
'''

today = '일요일'
if today == '일요일':
    print('게임 한 판')
print('공부 시작')
print()

'''
--if, else 조건-- 만약 ~라면, 그렇지 않다면
if 조건 :
    이 문장
else 조건 :
    저 문장
다음 문장

#True 일시
if 조건:
    이 문장
다음 문장

#False 일시
else 조건:
    저 문장
다음 문장
'''
#if가 참일때
today = '일요일'
if today == '일요일':
    print('게임 한판')
else :
    print('폰 5분')
print('공부 시작')
print()

#if가 거짓일때
today = '월요일'
if today == '일요일':
    print('게임 한판')
else :
    print('폰 5분')
print('공부 시작')
print()

'''
--elif-- 앞의 조건이 참이 아닌경우 다른조건을 다시 한번 확인하기 위한 용도로 사용
if와 else 사이에 원하는 만큼 넣을 수 있다
마지막 else 생략 가능

if 조건1:
    이 문장
elif 조건2:
    저 문장
else
    그 문장
다음 문장
'''
#if가 참일 때
today = '일요일'
if today == '일요일':
    print('게임 한판')
elif today == '화요일':
    print('폰 5분')
else :
    print('물 한잔')
print('공부 시작')
print()

#if가 거짓 , elif가 참일 때
today = '화요일'
if today == '일요일':
    print('게임 한판')
elif today == '화요일':
    print('폰 5분')
else :
    print('물 한잔')
print('공부 시작')
print()

#if가 거짓 , elif도 거짓일 때
today = '수요일'
if today == '일요일':
    print('게임 한판')
elif today == '화요일':
    print('폰 5분')
else :
    print('물 한잔')
print('공부 시작')
print()
