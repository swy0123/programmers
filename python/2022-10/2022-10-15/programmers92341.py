# 주차 요금 계산

# 소감
# 입력받은 문자열을 구하는 것과 시간을 계산하는 것이 상당히 귀찮은 작업이었지만 재미있게 풀었다.
# 반복되는 코드가 많아 더 간략하게 짤 수 있을 것 같다. 또 차량 번호로 정렬하는 과정을 다른 방식으로 최적화 할 수 있을 것 같다는 생각이 들었다.

# 기본 시간(분)     기본 요금(원)   단위 시간(분)   단위 요금(원)
# 180              5000           10             600
import math

def timeCal(start, end):
    startH = int(start[:2])
    startM = int(start[3:])
    endH = int(end[:2])
    endM = int(end[3:])

    if startM > endM:
        endM += 60
        endH -= 1
    
    return (endH-startH)*60 + (endM-startM)

def solution(fees, records):
    answer = []
    arr = []
    dic = {}
    for i in records:
        time, num, rec = i.split()
        if num not in dic:
            dic[num] = [rec, time, 0]
        elif rec == 'IN':
            dic[num][0] = rec
            dic[num][1] = time
        elif rec == 'OUT':
            dic[num][0] = rec
            tmp = timeCal(dic[num][1], time)
            dic[num][2] += tmp
            dic[num][1] = time
    for i in dic:
        if dic[i][0] == 'IN':
            dic[i][0] = 'OUT'
            tmp = timeCal(dic[i][1], '23:59')
            dic[i][2] += tmp
            dic[i][1] = '23:59'

    for i in dic:
        if dic[i][2] < fees[0]:
            arr.append((i, fees[1]))
        else:
            arr.append((i, fees[1] + math.ceil((dic[i][2]-fees[0])/fees[2])*fees[3]))
    
    arr.sort()

    for i in arr:
        answer.append(i[1])
    
    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))