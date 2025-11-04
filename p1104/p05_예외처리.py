# # 예외처리 - 오류(에러)가 나도 프로그램을 종료하지 않고 계속 실행

# # 오류 - 구문오류, 런타임오류
# a = 10
# print(a)
# # prin(a) # 구문오류(오타) - 실행하기 전에 에러가 남.

# a_list = [1,2,3]
# print(a_list[0])
# # 예외처리 - 외부연결: 파일 입출력, 파일 읽기/쓰기, 프린터기 연결, db 연결
# try:
#     print(a_list[100]) # 런타임오류 - 실행을 해야 알 수 있음.
# except Exception as e: print("에러:",e)

# print("프로그램을 종료합니다.")

print(1)
print(2)
try:
    print(3)
    # 에러
    raise SyntaxError # 강제로 에러 발생하는 명령어
    print(4)
    print(5)
except:  # 에러 발생시에만 실행
    print(6)
finally: # 에러 발생 여부와 상관없이 무조건 실행
    print(7)
print(8)
