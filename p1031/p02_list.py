stu_list = [
    # 이름,합계,등수
    ['홍길동',288,0],
    ['유관순',299,0],
    ['이순신',300,0],
    ['김구',295,0],
    ['강감찬',298,0]
]

for i in stu_list:
    r_count = 1 # 등수카운트
    for j in stu_list:
        if i[1] < j[1]:
            r_count += 1
    #비교가 완료되는 시점
    i[2] = r_count

print(stu_list)

# # 복합변수
# a = 10
# aa = a
# b = [1,2,3,4]
# bb = b   # 얕은복사 - 주소값복사
# # bb[0] = 100
# bbb = b[:] # 깊은 복사 - 값복사: 1,2,3,4 값을 떼와서 복사(주소값을 복사하는 게 아님.)
# # bbb = [1,2,3,4]
# ccc = [*b]

# print(a)
# print(b)
# print(ccc)

# # 단일변수, 단순변수
# a = 10 # 변수 -> 1개 값만 저장가능
# b = a
# b = 20

# print(a) # 10
# print(b) # 20
