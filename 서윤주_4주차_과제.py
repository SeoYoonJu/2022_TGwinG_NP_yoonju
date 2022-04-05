def intervention(queue):
    answer = list()
    answer = queue
    if "성은" in answer:
        if answer.index("성은")>3:
            answer.insert(int(answer.index("성은"))+1,"승호")
            return answer
        elif 0<=answer.index("성은")<=3:
            answer.append("승호")
            return answer
    else: answer.append("승호")
    return answer
print(intervention(["쯔위", "지효", "사나", "나연", "채영", "다현", "성은", "모모", "정연"]))
print(intervention(["쯔위", "지효", "사나", "나연", "채영", "다현", "모모", "정연"]))
print(intervention(["쯔위", "지효", "사나", "성은", "나연", "채영", "다현", "모모", "정연"]))
print(intervention(["쯔위", "지효", "사나", "나연", "성은",  "채영", "다현", "모모", "정연"]))

# 문제 2번
def pascal(n):
    answer = list()
    
# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    for i in searchWords:
        if entry in i:
            answer.append(i)
    return answer
print(auto_complete("강아지",["커피","강아지","강아지무료분양","강아지그림","레드벨벳","강아지입양","트와이스"]))

# 문제 4번
def stock_price(stockChart):
    answer = str()
    
    sum=0
    for i in stockChart:
        sum=sum+i
    '''   
     if sum==stockChart[-1]:
            print("아니야 조금만 더 기다려")
        elif sum<stockChart[-1] and sum==min:
            print(len(stockChart)-stockChart.index(sum)+"일 전에 샀어야지 으이구")
    '''
    com = 0
    min = sum
    cnt = 0
    cntm = 0 
    for i in stockChart:
        com += i
        cnt += 1
        if com > sum:
            pass
        elif com <= min:
            min = com
            cntm = cnt
    if min != sum:
        answer = str(len(stockChart)-cntm)+"일 전에 샀어야지 으이구"
    else:
        answer = "아니야 조금만 더 기다려"
    return answer
print(stock_price([0,0,0,0,0,0,0,0,0,0]))
print(stock_price([-1,-2,+3,-7,+2,+4,-5,+6,0,+1]))
            


# 문제 5번
def decryption(letter):
    answer = str()
    i=["abcdefghijklmnopqrstuvwxyz"]
    for i in letter:
        letter.remove(i)
        letter.index(i)==letter.index(i+3)
        answer.append(i)
    return answer
