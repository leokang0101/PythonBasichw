import random
count = 0 # 이긴 횟수

while True:
  print('')
  player = input()
  if player == '그만':
        @@@
       
  com = random.randint(1, 3)
  if com == 1:
     com = '가위'
  elif com == 2:
     com = '바위'
  elif == 3:
     com = '보'

  print('사용자 ( {} vs {} ) 컴퓨터'.format(player, com))

  if player == '가위' or player == '보' or player == '바위' :
        if (com == '가위' and player == '보') or @@@ or @@@ :
            print('컴퓨터 승')
        elif @@@ or @@@ or @@@ :
            print('플레이어 승')
            count += 1  # count = count + 1 코드와 동일
            if @@@ :
                print("player 3승으로 종료합니다.")
                break
        else:
            print('비겼습니다.')                  
  :
      print("잘못 입력했습니다.")
      continue
  
