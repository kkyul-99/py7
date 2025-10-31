# {키:값}
stu_dic = {"no":1,"name":"홍길동","kor":100}

# dict 추가
stu_dic['eng'] = 90
# dict 수정
stu_dic['kor'] = 10
# dict 삭제
# del stu_dic['name']
print(stu_dic)

# keys() 출력
print(stu_dic.keys())
print(list(stu_dic.keys()))
for k in stu_dic.keys():
    print("{}:{}".format(k,stu_dic[k]))

# values() 출력
print(stu_dic.values())
print(list(stu_dic.values()))
for i,v in enumerate(stu_dic.values()):
    print("{}, {}".format(i,v))

# items() 출력 - k,v
print(stu_dic.items()) # 튜플 형태로 출력
print(list(stu_dic.items()))
for k,v in stu_dic.items():
    print("{}:{}".format(k,v))

# 딕셔너리 출력
print(stu_dic['no'])
print(stu_dic['name'])
print(stu_dic['kor'])
# print(stu_dic['math']) # 없는 key 출력 시 에러 발생
print(stu_dic.get('kor'))
print(stu_dic.get('math')) # 없는 key 출력해도 실행됨. - None 출력

# 딕셔너리 정렬
import operator
names = {"홍길동":100,"유관순":80,"이순신":90,"김구":99,"강감찬":95}
# reverse = True: 역순정렬, reverse = False: 순차정렬
# itemgetter(0): 키, itemgetter(1): 값
names2 = sorted(names.items(),key=operator.itemgetter(1),reverse=True)
print(names)
print(names2)

# 리스트 정렬
a_list = [1,5,9,4,3]
# sort(): 해당 리스트 자체를 정렬, 원본 변경.
# a_list.sort()
a_list.reverse() # 1,5,9,4,3 -> 3,4,9,5,1
# sorted(): 다른 변수에 저장 가능, 원본은 변경 안됨.
b_list = sorted(a_list,reverse=True)
print(a_list)
print(b_list)

print(max(a_list)) # 리스트 최대값
print(min(a_list)) # 리스트 최소값
