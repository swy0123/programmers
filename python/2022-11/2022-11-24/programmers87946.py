# Lv.2 피로도 : 완전탐색(DFS)

# k	    dungeons	                result
# 80	[[80,20],[50,40],[30,10]]	3


def solution(k, dungeons):
    answer = 0
    arr = [0]

    def dfs(fatigue, dungeon, count2):
        for i in range(len(dungeon)):
            if i<len(dungeon)-1 and fatigue>=dungeon[i][0] and fatigue>=dungeon[i][1]:
                dfs(fatigue-dungeon[i][1], dungeon[:i]+dungeon[i+1:], count2+1)
            elif i==len(dungeon)-1 and fatigue>=dungeon[i][0] and fatigue>=dungeon[i][1]:
                dfs(fatigue-dungeon[i][1], dungeon[:i], count2+1)
        arr.append(count2)

    cnt=0
    for i in range(len(dungeons)):
        if i<len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dfs(k-dungeons[i][1], dungeons[:i]+dungeons[i+1:], cnt+1)
        elif i==len(dungeons)-1 and k>=dungeons[i][0] and k>=dungeons[i][1]:
            dfs(k-dungeons[i][1], dungeons[:i], cnt+1)

    answer = max(arr)
    return answer