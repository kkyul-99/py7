# 3개 출력하시오.
# 3개를 a_list 리스트 추가하시오.
# [['안녕','hello'],['사랑','love'],['감사','thank']]

a_list = []
f = open("C:/down/aaa.txt","r")
while True:
    txt = f.readline()  
    if txt == "": break
    a_list.append(txt.strip().split(",")) # 리스트추가
f.close()    

print(a_list)

# f = open("C:/down/aaa.txt","r")
# # readline() : 1줄씩 가져오기
# txt = f.readline()  
# # txt = "1,홍길동,100,100,100,300,100.00,0"
# print(txt.strip())  # 문자열타입 - strip : 공백제거
# print(txt.strip().split(","))  # 리스트타입 - strip:공백제거,split():분리
# print(txt.strip().split(",")[5])  # 합계
# f.close()
