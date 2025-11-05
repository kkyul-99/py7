stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
] 

# dict타입 -> 문자열로 변환
stu_str = ""
for i in range(len(stu_list)):
    stu_str += f"{stu_list[i]['stuno']},{stu_list[i]['name']},\
{stu_list[i]['kor']},{stu_list[i]['eng']},{stu_list[i]['math']},\
{stu_list[i]['total']},{stu_list[i]['avg']},{stu_list[i]['rank']}\n"

# 파일쓰기
f = open("c:/down/aaa.txt","w")  # 파일없으면 w:모드는 파일을 생성
f.write(stu_str)
f.close()

# 파일저장

# 파일 다시 읽어와서, dict타입으로 변경해서
# 출력하시오.

# import ast
# ss = "{'stuno':10103,'name':'이순신','kor':100,'eng':100,'math':100,'total':300,'avg':100.00,'rank':0}"
# data = ast.literal_eval(ss)
# print(data)
# print(data['stuno'])

# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\
# \t{stu['eng']}\t{stu['math']}\t{stu['total']}\
# \t{stu['avg']}\t{stu['rank']}\t")
