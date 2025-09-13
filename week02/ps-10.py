N = 9 
M = 3

def solution(N, M):
  days = 0
  while(N > 0):
    days += 1
    if(days % M == 0):
      N += 1
    N -= 1
  return days

print("현재 %d개의 재고가 있고, %d일 마다 책상이 1개씩 입고되면, 재고가 0이 되는데 %d일이 걸립니다" %(N,M,solution(N,M)))