data = ["조회수 : 1,500","조회수 : 1,002","조회수 : 300","조회수 : 251","조회수 : 13,432","조회수 : 998"]

sum = 0

for d in data:
    print(d)

for d in data:
    data1 = d.replace("조회수 : ","")
    print(data1)

for d in data:
    d = d[5:]
    d = d.replace(",","")
    print(d)

for d in data:
    d = d[5:]
    d = d.replace(",","")
    d = int(d)
    sum = sum +d
    print(sum)

def sumOfList(llist):
  sum = 0
  for n in llist:
    sum = sum + n
  return sum

nList = [1, 20, 5, 6, 39, 20, 68, 30, 68, 93]
print(sumOfList(nList))