# 문제 1번
def sum(a,b):
    sum = a+b
    return sum
    
# 문제 2번
def sub(a,b):
    sub = a-b
    return sub

# 문제 3번
def mul(a,b):
    mul = a*b
    return mul

# 문제 4번
def div(a,b):
    div = a/b
    return div

# 문제 5번
def distance(x1,y1,x2,y2):
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    return distance

# 문제 6번
def short():
    lylic="life is short art is long"
    return lylic[8:13]
print(short())

# 문제 7번
def myReverse(string):
    string=input()
    return string[::-1]
print(myReverse('string'))

# 문제 8번
def letMeIntroduceMyself():
    a=input("이름을 입력하시요:")
    b=input("취미를 입력하시요:")
    c=input("재학 중인 대학을 입력하시요:")
    d=input("생일을 입력하시요:")
    e="제 이름은 %s입니다. 제 취미는 %s이구요, 저는 %s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다"%(a,b,c,d[2:4],d[4:6])
    return e
print(letMeIntroduceMyself())


# 문제 9번
def calcAI():
    a=int(input("첫 번째 숫자를 입력하시오:"))
    b=int(input("두 번째 숫자를 입력하시요:"))
    c="두 수의 합은 %d입니다"%(a+b)
    return c
print(calcAI())

