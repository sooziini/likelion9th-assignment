# 문자열 (내장함수)

# 덧셈

str = "Xonmin"

# slicing [x:y]  = x부터 y-1 인덱스 까지




print(str[0])

# 문자열 길이 : len(문자열 변수)

print(len(str))

# 문자열 내에서 특정 문자의 등장 횟수 : count('x')

print(str.count('n'))

# 문자열을 (특정 기준으로) 나누기  : 문자열 변수.split() default : 공백기준

print(str.split())

# 특정 문자 인덱스 찾기  : find('x') or index('x')   찾고자 하는 문자가 없을 때

print(str.find('x'))


# 리스트 내장 함수

li = [3, 1, 'X', 4, '하이', 3]

# 리스트 길이 : len
# 오름차순 정렬 : sort
print(li.sort())
