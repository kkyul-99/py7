import os

fname = input("검색하려는 파일이름을 입력하세요.")

# 파일이 존재하는지 확인
if os.path.exists("c:/down/"+fname):
    print("존재")
else:
    print("없음")    

# 현재위치에 존재하는 모든 파일을 출력 - list
print(os.listdir("c:/down/"))
