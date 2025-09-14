str = '20201231Thursday'
year = str[:4]
print(year)
mmdd = str[4:8]
print(mmdd)
day = str[8:]
print(day)

a = ['쓰', '레', '기', '통']
a.reverse()
print(a)

for i in range(5):
  print('*' * (i+1))

def avg(*args):
  total = 0

  for i in args:
    total += i

  return total / len(args)

print(avg(5,3,12,9))
print(avg(2.4,3.2,7.3))
print(avg(10,5))