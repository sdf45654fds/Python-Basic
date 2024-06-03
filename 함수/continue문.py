#반복문 탈출
drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만보자')
        continue
    print(f'{x}시청')

#문제
for x in range(10):
    if x %2==1:
        continue
    print(x)