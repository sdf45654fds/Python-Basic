#문자열 출력
python = '파이썬'
java = '자바'
print('개발 언어에는 ' + python + ',' + java + ' 등이 있어요')
print('개발 언어에는 ',python,',',java,'등이 있어요')
print()

'''
, , ,이렇게 출력하면 너무 복잡해 보여서
문자열 포맷 사용
'''
# 1. {} + format
print('개발 언어에는 {},{} 등이 있어요'.format(python,java))
# 2. {N} + format
print()
print('개발 언어에는 {0},{1} 등이 있어요'.format(python,java))
print('개발 언어에는 {0},{0},{1},{1} 등이 있어요'.format(python,java))
print()
#f-string (파이썬 3.6이상)
print(f'개발 언어에는 {python},{java} 등이 있어요')