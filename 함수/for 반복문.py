'''
for 변수 in 반복 범위:
    반복 수행 문장
'''
# )예
for x in range(10):
    print("팔 벌려 뛰기")

# 횟수 반복 추가
for x in range(10):
    print(f'팔 벌려 뛰기 {x+1}회')

'''
range(10) ->  0이상 10미만 (10이란 값은 stop을 의미)
range(start,stop) ->  start이상 stop미만
range(start,stop,step) -> start이상 stop미만에서 step만큼 증가 
'''
# 0부터 9까지
for x in range(10):
    print(x)

#range(start,stop) ->  start이상 stop미만
for x in range(1,10):
    print(x)

#range(start,stop,step) -> start이상 stop미만에서 step만큼 증가
for x in range(1,20,2):
    print(x)

#문제
for n in range(1,31,10):
    print(f'{n}번은 {n}번부터 {n+9}번까지 모아줘')

'''
for 변수 in 반복 대상:
    반복 수행 문장
리스트, 튜플, 딕셔너리 사용 가능
'''
#for문 리스트 활용
my_list=[1,2,3]
for x in my_list:
    print(x)

#튜플도 리스트와 동일

#for문 딕셔너리 활용
person = {
    '이름':'나도',
    '나이':7,
    '키':120,
    '몸무게':23
}
#values값 사용
for v in person.values():
    print(v)
#key값 사용
for k in person.keys():
    print(k)
#key와 values를 items를 사용하여 함께 출력
for k,v in person.items():
    print(k,v)

#for 문자열
fruit = 'apple'
for x in fruit:
    print(x)