# return: 함수호출로 값을 전달할 때 사용

def cal(a,b):
    return a+b # 함수호출로 값을 전달

sum = cal(1,2) # 함수호출

def func(a,b):
    a+b        # 값 전달 X - return 옆에 있는 값만 호출 함수로 전달됨.
    return     # return값이 없으면 함수종료

def big(a,b):
    if a>b:
        return a
    else:
        return -1
