a_list = [1,1,2,3,4,2,3,1,5,4]
a_dic = {}
# 1: 2:
# 딕셔너리에 저장하시오.

for i in a_list:
    if i not in a_dic:
        a_dic[i] = 1
    else:
        a_dic[i] += 1

# a_dic['홍길동'] = 100
# print(a_dic) # {'홍길동':100}

# b_dic = {}
# b_dic[1] = 1
# b_dic[2] = 1
# b_dic[1] = 10
# print(b_dic) # {1:10,2:1}

print(a_dic)

b_dic = {}
# 딕셔너리 추가, 수정
# "홍길동":100
# 없는 키 입력시 추가
b_dic['홍길동'] = 100
# 있는 키 입력시 수정
b_dic['홍길동'] = 50
