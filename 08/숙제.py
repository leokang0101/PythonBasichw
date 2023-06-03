import random
print('임의의 두 자리숫자가 주어집니다.더하기 값을 구하세요.')
num1=random.randint(0,100)
num2=random.randint(0,100)
min=0
max=200
ㄷ=num1+num2
print('숫자 1:{0}, 숫자2:{1}'.format(num1,num2))
ㅊ=0
while True:
    ㅊ=ㅊ+1
    print("{0}번째 도전({1}~{2})".format(ㅊ,min,max))
    u=int(input('당신의 선택은?'))
    if u>ㄷ:
        print('정답보다 크네요')
        max=u
    elif u<ㄷ:
        print('정답보다 작네요')
        min=u
    else:
        print('정답입니다')
        break
import random
min=0
max=100
a=random.randint(0,100)


print('0~100까지의 숫자를 입력하십시요.')
count=0
while True:
    count=count+1
    print("{0}번째 도전({1}~{2})".format(count,min,max))
    u=int(input('당신의 선택은?'))

    if u>a:
        print('정답보다 크네요')
        max=u
    elif u<a:
        print('정답보다 작네요')
        min=u
    else:
        print('정답입니다')
        break




import random
print('임의의 두 자리숫자가 주어집니다.더하기 값을 구하세요.')
num1=random.randint(0,100)
num2=random.randint(0,100)
min=0
max=200
ㄷ=num1+num2
print('숫자 1:{0}, 숫자2:{1}'.format(num1,num2))
ㅊ=0
while True:
    ㅊ=ㅊ+1
    print("{0}번째 도전({1}~{2})".format(ㅊ,min,max))
    u=int(input('당신의 선택은?'))
    if u>ㄷ:
        print('정답보다 크네요')
        max=u
    elif u<ㄷ:
        print('정답보다 작네요')
        min=u
    else:
        print('정답입니다')
        break
import random
min=0
max=100
a=random.randint(0,100)


print('0~100까지의 숫자를 입력하십시요.')
count=0
while True:
    count=count+1
    print("{0}번째 도전({1}~{2})".format(count,min,max))
    u=int(input('당신의 선택은?'))

    if u>a:
        print('정답보다 크네요')
        max=u
    elif u<a:
        print('정답보다 작네요')
        min=u
    else:
        print('정답입니다')
        break




import random
count = 0 # 이긴 횟수

while True:
  print('가위, 바위, 보 중 하나를 입력하세요.')
  player = input('------------------------------------')
  if player == '그만':
        break
       
  com = random.randint(1, 3) # 1 ~ 3 중 하나의 숫자 return
  if com == 1:
     com = '가위'
  elif com==2:
     com = '바위'
  elif com==3:
     com = '보'

  print('사용자 ( {} vs {} ) 컴퓨터'.format(player, com))

  if player == '가위' or player == '보' or player == '바위' :
        if (com == '가위' and player == '보') or(com == '보' and player == '바위')or(com == '바위' and player == '가위'):
            print('컴퓨터 승')
        elif (com == '보' and player == '가위') or (com == '가위' and player == '바위') or (com == '바위' and player == '보') :
            print('플레이어 승')
            count += 1  # count = count + 1 코드와 동일
            if  count==3:
                print("player 3승으로 종료합니다.")
                break
        else:
            print('비겼습니다.')                  
  else:
      print("잘못 입력했습니다.")
      continue
