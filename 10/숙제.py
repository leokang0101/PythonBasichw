scores = [0] * 5
for i in range(5):
    scores[i] = int(input('{}번 학생의 성적 입력: '.format(i+1)))
print('--- 입력된 값 ---')
for i in range(5):
    print('{}번 학생의 성적: {}'.format(i+1,scores )
