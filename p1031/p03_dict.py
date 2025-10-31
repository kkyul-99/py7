# stu_list = [name:'홍길동',kor:100,eng:100,math:100]
# stu_list = {키1:값1,키2:값2,키3:값3,...}

# # 딕셔너리 생성
# list1 = [1,2,3]
# dic1 = {1:'a',2:'b',3:'c'}
# dic2 = {"no":1,"name":"홍길동","class":3}
# print(list1)
# print(dic1)

# # 리스트 추가 - append, insert, extend
# stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학"}
# print(stu)
# # 딕셔너리 추가 - 없는 키값 입력하면 추가 됨.
# stu['연락처'] = '010-1111-1111'
# print(stu)
# # 수정
# stu['이름'] = "홍길자" # 키는 수정 불가
# print(stu)
# # print(stu['성명']) # 없는 키를 출력할 때 에러 발생
# stu['성명1'] = '홍'
# print(stu)
# # 딕셔너리 삭제
# del(stu['성명1'])

stu_list = [
    {"no":1,"name":"홍길동","kor":100}
]

print(stu_list[0]['no'])
print(stu_list[0]['name'])

a_dic = {"no":1,"name":"홍길동","kor":100}
# 국어점수를 출력하시오.
print(a_dic['kor'])      # 없는 키값 입력시 에러
# 딕셔너리 get()함수
print(a_dic.get('kor1')) # 없는 키값 입력시 None타입으로 출력됨.

# 딕셔너리 keys()
print(a_dic.keys())
a_list = list(a_dic.keys())
print(a_list[0])
# 딕셔너리 values()
print(a_dic.values())
b_list = list(a_dic.values())
print(b_list)

# 딕셔너리 items() - key,value
print(a_dic.items())
c_list = list(a_dic.items())
print(c_list[1][1])

aa_list = [
    ['no', 1],
    ['name', '홍길동'],
    ['kor', 100]
]
# 홍길동을 출력하시오.
print(aa_list[1][1])

# 키 존재 확인
stu_dic = {"no":1,"name":"홍길동","kor":100}
if 'eng' in stu_dic:
    print("키가 존재합니다.")
else:
    print('키가 존재하지 않습니다.')
