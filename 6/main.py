1, 2, 3, 4, 5, 6, 7, 8, 9
3, 9, 9, 12, 15
5, 6, 7, 8, 9, 10
0, 1, 2, 3, 4
10, 8, 6, 4, 2
number = int(input('숫자를 입력하세요.'))

for i in range(number):
    print("I  love Python")
    
for x in range(2002, 2051, 4):
    print(x)
    
while True:
    score = int(input('점수 : '))
    
    if score == -1:
        break
    if score>=60 :
        print('합격')
    else :
        print('불합격')
        
for i in range(10):    
    if i == 7:
        continue
    print("The Number is :" , i)
    
n = int(input('숫자를 입력해 주세요.'))
for i in range(2, n+1):
    is_prime = True
    for j in range(2, i, 1):
        if i%j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')
