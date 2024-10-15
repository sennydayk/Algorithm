N = int(input())
cards = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}

for i in range(N) :
    fruit, count = input().split()
    cards[fruit] += int(count)

if 5 in cards.values():
  print('YES')
else:
  print('NO')