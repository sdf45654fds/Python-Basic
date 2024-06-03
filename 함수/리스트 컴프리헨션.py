products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [] #리콜 대상 제품 리스트
for p in products:
    if p.startswith('SIRO'): #제품명이 SIRO로 시작하는가?
        recall.append(p)
print(recall)

#위 코드를 한줄만에 해결하는 방법 -> new_list = [변수 활용 for 변수 in 반복대상 if 조건]

'''
my_list = [1,2,3,4,5]
new_list = [x for x in my_list if x > 3]
앞에 x {1,2,3,4,5} / x*3 {3,6,9,12,15} / str(x) + '번째 {'1번째', '2번째', '3번째',...}
뒤에 (if x>3)은 x값이 3보다 큰 경우만 사용해라(if 조건문이 붙어있음)
'''
#위 주석 토대로 변경 한 코드
products = ['JOA-2020', 'JOA-2021', 'SIRO-2021', 'SIRO-2022']
recall = [p for p in products if p.startswith('SIRO')]
print(recall)

#모든 모델명 뒤에 SE(Special Edition)을 붙여줘
prod_se = [p+'SE' for p in products]

#모든 모델명을 소문자로 바꿔줘
prod_lower = [p.lower() for p in products]

#22년 제품만 뽑는데 뒤에 (최신형)이라는 글자를 붙여줘
prod_new = [p+'(최신형)' for p in products if p.endswith('2002')]
