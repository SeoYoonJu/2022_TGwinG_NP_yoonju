# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    string = "I'm on the next level"
    if "tgwing" in string:
        print("TGWinG")
    elif "KHU" in string:
        print("Idol")
    elif "next" in string:
        print("next")
    elif "Suwon" not in string:
        print("Suwon city")
    else: print("none")
    return
question1()

# 문제 2번
def leapYear(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return "윤년입니다."
    else: return "윤년이 아닙니다."
print(leapYear(2008))
print(leapYear(2022))
print(leapYear(2017))

# 문제 3번
def alarm(time):
    if time//100>=12:
        a="오후"
        if time%100>=45:
            b=time//100
            c=time%100-45
            d="%s %d시 %d분"%(a,b,c)
            return d
        else:
            b=time//100-1
            c=60-(45-(time%100))
            d="%s %d시 %d분"%(a,b,c)
            return d
    elif time//100<12:
        a="오전"
        if time%100>=45:
            b=time//100
            c=time%100-45
            d="%s %d시 %d분"%(a,b,c)
            return d
        else:
            b=time//100-1
            c=60-(45-(time%100))
            d="%s %d시 %d분"%(a,b,c)
            return d
print(alarm(1610))
print(alarm(1000))
print(alarm(930))

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):    
    if int(r1)+int(r2)==((x1-x2)**2+(y1-y2)**2)**0.5>0:
        return int(1)
    elif int(r1)+int(r2)>((x1-x2)**2+(y1-y2)**2)**0.5>0:
        if int(r1)-int(r2)==((x1-x2)**2+(y1-y2)**2)**0.5 or int(r2)-int(r1)==((x1-x2)**2+(y1-y2)**2)**0.5:
            return int(1)
        else: return(int(2))
    elif int(r1)+int(r2)<((x1-x2)**2+(y1-y2)**2)**0.5:
        return int(0)
    elif ((x1-x2)**2+(y1-y2)**2)**0.5==0 and int(r1)==int(r2):
        return "어딘지 모르겠다 오바"
    else: return int(0)
print(findDaesun(0,0,1,0,0,1))
print(findDaesun(0,0,4,0,0,1))
print(findDaesun(0,0,1,2,0,1))
print(findDaesun(1,23,23,6,5,5))
print(findDaesun(0,0,4,3,0,1))