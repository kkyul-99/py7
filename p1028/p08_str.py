a_list = [3,5,9,10,2]
aa_list = []

for i in a_list:
    print(i)
    print(i+10)

for i in a_list:
    aa_list.append(i*10)

print(a_list)
print(aa_list)

print(list(range(10)))
print(list("0"*10))

b_list = list(range(10))
print(b_list[::2])

b_list = list(range(0,10,2))
print(b_list)

# score = 92
# hak = ""
# if score >= 90:
#     hak = "A"
#     if score >= 96:
#         hak = hak +"+"
#     elif score < 93:
#         hak = hak +"-"
# print(hak)

# if score >= 96:
#     print("A+")
# elif score >= 93:
#     print("A")
# elif score >= 90:
#     print("A-")

# a = "안녕"
# b = '안녕'
# print(type(a))

# c = """
# aaa
# bbb   ccc
#    ddd
# """

# d = "\
# aaa bbb\
# ccc\
# "
# print(d)

# e = "안녕"
# print(e*10)

# student1 = [90,95,85,80]
# print(len(student1))
# print(type(student1))
# print(student1[3])
# print(student1[-1])
# print(student1 * 3) # 리스트 반복
# print(80 in student1)

# name_list = ["홍","유","이","김","강"]
# if "이" in name_list:
#     print("'이'가 있습니다.")
# else:
#     print("'이'가 없습니다.")

# str1 = "안녕하세요. 반갑습니다."
# if "반" in str1:
#     print("'반'이 있습니다.")
# else:
#     print("'반'이 없습니다.")

# num_list = [1,2,3,1,2,3,1,1,1,2,3,2,2,2,2,2]
# print(num_list.count(1))
# n_list = [4,23,2,9,10,5,7,1]
# n_list.sort() # 순차정렬 - 낮은 값으로 정렬
# print(n_list)
# n_list.sort(reverse=True) # 역순정렬 - 높은 값으로 정렬
# print(n_list)
# n_list.reverse() # 정렬이 아닌 순서를 역순으로 출력
# print(n_list)

# a = 95
# if a > 90:
#     pass # 아무 일도 일어나지 않음
