import math

def calcCircleArea(r):
    result = float()
    result = math.pi*r*r
    return round(result,2)

def calcLog(a, b):
    result = float()
    result = math.log(a,b)
    return round(result,2)

def calcSin(x):
    result = float()
    result = math.sin(x)
    return round(result,2)

def calcFactorial(x):
    result = int()
    result=math.factorial(x)
    return result

def calcCombination(n, r):
    result = int()
    result=math.comb(n,r)
    return result

def calculator(order):
    answer = 0
    a=order.split()
    if a[0]=="원넓이:":
        answer=calcCircleArea(float(a[1]))
    elif a[0]=="로그:":
        if a[1] == "e":
            answer=calcLog(math.e, float(a[2]))
        else:
            answer = calcLog(float(a[1]), float(a[2]))
    elif a[0]=="사인:":
        answer=calcSin(float(a[1]))
    elif a[0]=="팩토리얼:":
        answer=calcFactorial(int(a[1]))
    elif a[0]=="조합:":
        answer=calcCombination(int(a[1]),int(a[2]))
    return answer

print(calculator("원넓이: 10"))
print(calculator("로그: e 10"))
print(calculator("사인: 100"))
print(calculator("팩토리얼: 5"))
print(calculator("조합: 3 2"))
    #명령어: 2 2