# # for 변수 in 범위:
# for i in range(5): # [0,1,2,3,4]
#     print(i,end="\t") # 한줄로 출력(end 생략 시 한 줄씩 띄어서 출력)

# # 1~100까지 합을 구하시오.
# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print("합계: ",sum)

# # 100을 넘는 위치는 얼마를 더할 때 일까요?
# sum = 0
for i in range(1,101):
    sum = sum + i
    print(i,sum)
    if sum > 100:
        break
print(f"{i} 번째 : {sum}") # print(f"{i-1} 번째 : {sum-i}") - 이전 값

# 1*2*3*4*...*10 결과값 출력하시오.
result = 1
for i in range(1,11):
    result = result * i
    print(i,result)
    if result > 100:
        break
print(f"{i} 번째 : {result}") # print(f"{i-1} 번째 : {result/i}") - 이전 값
