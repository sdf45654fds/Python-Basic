lang = 'PYHTON'
#--인덱스
# 0 = 첫 번째 값 P
print((lang[0]))
# 5 = 다섯 번째 값 N
print((lang[5]))
# -1 = 마지막 값 N
print((lang[-1]))

# --슬라이싱 = 어디부터 : 어디까지 lang[start : end]
# 인덱스 1부터 6 직전까지
print(lang[1:6]) #5까지
# 인덱스 1부터 끝까지
print((lang[1:]))
# 처음부터 인덱스 4직전까지
print(lang[:4])
# 처음부터 끝까지
print(lang[:])
