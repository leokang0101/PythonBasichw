book['모모', '어린왕자','별', '돈키호테', '마당을 나온 암탉']
book.append('불의 날개')
book.insert(1,'데미안')
del book [2]
book.remove('돈키호테')

family = []
while True:
    name = input("가족 구성원의 이름 : ")
    if name=="끝":
        break
        
    family.append(name)

print(family)

#()를 사용하면 추가하거나 빼는 것을 못하기 때문이다.
