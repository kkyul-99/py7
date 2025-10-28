### list 추가 - append, insert, extend
a_list = [1,2,3]
# 1. append - 제일 뒤에 추가
# 복합변수의 값이 변경이 됨.
a_list.append(10)
print(a_list)
# 2. insert - (위치, 값) 추가
a_list.insert(1,200)
print(a_list)
# 3. extend - list 2개를 합침
a2_list = [5,6,7]
a_list.extend(a2_list)
print(a_list)
a_list = a_list + [10,20,30]
print(a_list)

### list 값 변경 - 위치 값을 입력하면 변경됨.
a_list[2] = 1000
# a_list[100] = 1000 # 없는 주소를 넣으면 에러
print(a_list)

### list 값 삭제 - pop(), del, remove(), clear
aa_list = [1,2,3,4,5,6,7]
# 1. pop() - 제일 뒤 삭제
aa_list.pop()
print(aa_list)
# 2. del - 해당 위치 삭제
del aa_list[0]
print(aa_list)
# 3. remove - 해당 값 삭제(중복 값 있을 시 앞 순번 1개만 지워짐)
aa_list.remove(5)
print(aa_list)
# 4. clear - 모두 삭제
aa_list.clear()
print(aa_list)

a = 10
a + 100
print(a) # 10 - 비파괴적 cf) list - 파괴적  # ****************

# [] 1개: 1차원 리스트
# [[]] 2개: 2차원 리스트
# [[[]]] 3개: 3차원 리스트

# 2차원 리스트
b_list = [
    ["홍길동",100,],["유관순",99],["이순신",80],["김구",89]
    ]
print(b_list[0][0]) # 홍길동
