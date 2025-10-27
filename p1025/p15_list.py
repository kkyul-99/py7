# 변수 - 숫자(정수, 실수), 문자열, 불(True, False)
# 리스트, 튜플, 셋

# 리스트 - 배열: 데이터를 여러개 저장하는 공간
# 변수는 1개의 값만 저장
a = 10
a = 5
print(a)

fruit = ["사과", "배", "복숭아", "딸기", "포도"]
print(fruit[0])
numbers = [1,2,3,4,5]
print(numbers)
print(numbers[0])
total = ["사과", 1, 2, True, 1.25]
print(total)
stuscore = ['홍길동', 100, 100]
print(stuscore)

### 리스트 데이터 추가 - append, insert
# appen - 제일 뒤 추가
stuscore.append(100) 
print(stuscore)
# 1번째방에 값 5를 추가
stuscore.insert(1, 5)
print(stuscore)

### 리스트 데이터 삭제 - pop, remove, del
# pop - 리스트 제일 뒤 삭제
stuscore.pop()
print(stuscore)
# remove: 해당 리스트 값 삭제
stuscore.remove("홍길동")
print(stuscore)
# del 해당 번호 삭제
del stuscore[0]
print(stuscore)
