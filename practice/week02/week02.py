a = 123
a = 12.24
print(a)

s1 = "hello world"
print(s1)

head = "hello"
tail = " world"
print(head + tail)

a = "imjuyongp"
print(a[0])
print (a * 5)
print(a[-1])
print(a.count('i')) # i 문자열의 개수 출력
print(a.find('u')) # u 문자열 인덱스 출력 (없으면 -1 출력)
print(a.index('u')) # 출력할 문자열이 없으면 에러 발생
b = ","
c = b.join("abcd")
print(c)
print(a.upper())
d = "    py   "
print(d.lstrip()) # 앞쪽 공백 제거
print(d.rstrip()) # 뒤쪽 공백 제거
print(d.strip()) # 모든 공백 제거

# a = 'pithon' 
# a[1] = 'y' # 문자열은 원소임으로 변경 불가능 (에러)

a = "python is difficult"
print(a.replace('difficult', 'funny'))
print(a.split()) # 공백 기준 문자열 나누기
# + 이것저것...

# 튜플과 리스트의 차이
# 가변성 -> 리스트는 원소 변경 가능, 튜플은 원소 변경 불가능
# 리스트 표현 : [], 튜플의 표현 : ()