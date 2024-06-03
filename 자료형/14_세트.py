'''
튜플과 리스트와 같이 여러가지 값 저장가능
순서 보장 x 인덱스로 접근불가
중복 허용 x
수정 불가 x 단 튜플처럼 읽기전용은 아님 / .add메소드를 이용해 값 추가 가능
중괄호 값 콤파로 구분
'''

A={'돈까스','보쌈','제육덮밥'}
B={'짬뽕','초밥','제육덮밥'}
# 두 친구가 고통으로 좋아하는 음식(교집합) intersection
print(A.intersection(B))
print()

# 두 친구가 좋아하는 음식 전부(합집합) union
print(A.union(B))
print()

# A만 좋아하는 음식(차집합) difference
print(A.difference(B))
print()

# 값 추가 add
my_set={'돈까스','보쌈','제육덮밥'}
print(my_set)
my_set.add('닭갈비')
print(my_set)
print()

# 값 제거 remove
my_set={'돈까스','보쌈','제육덮밥'}
print(my_set)
my_set.remove('제육덮밥')
print(my_set)
print()

# 값 전체제거 clear
my_set={'돈까스','보쌈','제육덮밥'}
print(my_set)
my_set.clear()
print(my_set)
print()

# clear를 쓰면 set가 남는대 set까지 자체를 완전삭제 delete
my_set={'돈까스','보쌈','제육덮밥'}
print(my_set)
del my_set
print(my_set) #완전 삭제해서 존재하지 않으므로 에러 발생
