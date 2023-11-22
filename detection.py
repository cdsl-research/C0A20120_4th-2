import pandas as pd
import numpy as np

def pullList(Path, targetList):
    df = pd.read_csv(Path)    
    aveCpuList = []
    maxCpuList = []
    minCpuList = []
    aveRamList = []
    maxRamList = []
    minRamList = []
    for dataList in targetList:
        cnt4 = 0
        cnt5 = 0
        while True:
            if df.columns[cnt4].find(dataList[0]) != -1:
                if df.columns[cnt4].find(dataList[0] + "-db") == -1:
                    if df.columns[cnt5].find(dataList[1]) != -1:
                        if df.columns[cnt5].find(dataList[1] + "-db") == -1:
                            xAveCpuList = [df.iloc[1:, cnt4].mean(), df.iloc[1:, cnt5].mean()]
                            xAveRamList = [df.iloc[1:, cnt4+1].mean(), df.iloc[1:, cnt5+1].mean()]
                            xMaxCpuList = [df.iloc[1:, cnt4].max(), df.iloc[1:, cnt5].max()]
                            xMaxRamList = [df.iloc[1:, cnt4+1].max(), df.iloc[1:, cnt5+1].max()]
                            xMinCpuList = [df.iloc[1:, cnt4].min(), df.iloc[1:, cnt5].min()]
                            xMinRamList = [df.iloc[1:, cnt4+1].min(), df.iloc[1:, cnt5+1].min()]
                            aveCpuList.append(xAveCpuList)
                            aveRamList.append(xAveRamList)
                            maxCpuList.append(xMaxCpuList)
                            maxRamList.append(xMaxRamList)
                            minCpuList.append(xMinCpuList)
                            minRamList.append(xMinRamList)
                            break
                        else:
                            cnt5 += 1
                    else:
                        cnt5 += 1
                else:
                    cnt4 += 1
            else:
                cnt4 += 1
    return aveCpuList, aveRamList, maxCpuList, maxRamList, minCpuList, minRamList

def compareUsage(Path, resultList, resultDBList, targetList, targetDBList):
    df = pd.read_csv(Path)
    xValue = 0
    rValue = 0
    dim = np.ndim(resultList[0])
    for dataList in targetList:
        cnt4 = 0
        cnt5 = 0
        while True:
            if df.columns[cnt4].find(dataList[0]) != -1:
                if df.columns[cnt4].find(dataList[0] + "-db") == -1:
                    if df.columns[cnt5].find(dataList[1]) != -1:
                        if df.columns[cnt5].find(dataList[1] + "-db") == -1:
                            break
                        else:
                            cnt5+=1
                    else:
                        cnt5+=1
                else:
                    cnt4+=1
            else:
                cnt4+=1

        for i in range(dim):
            aveCpuRate = resultList[0][i][0] / df.iloc[0, cnt4] * 100
            aveRamRate = resultList[1][i][0] / df.iloc[1, cnt4] * 100
            maxCpuRate = resultList[2][i][0] / df.iloc[0, cnt4] * 100
            maxRamRate = resultList[3][i][0] / df.iloc[1, cnt4] * 100
            minCpuRate = resultList[4][i][0] / df.iloc[0, cnt4] * 100
            minRamRate = resultList[5][i][0] / df.iloc[1, cnt4] * 100
            
            if (maxCpuRate-aveCpuRate) > (aveCpuRate-minCpuRate):
                xValue = maxCpuRate-aveCpuRate
            elif (maxCpuRate-aveCpuRate) < (aveCpuRate-minCpuRate):
                xValue = aveCpuRate-minCpuRate
            elif (maxRamRate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = maxRamRate - aveRamRate
            elif (maxRamRate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = aveRamRate - minRamRate

            if rValue < xValue:
                rValue = xValue
                xPod = df.columns[cnt4]

            aveCpuRate = resultList[0][i][1] / df.iloc[0, cnt5] * 100
            aveRamrate = resultList[1][i][1] / df.iloc[1, cnt5] * 100
            maxCpuRate = resultList[2][i][1] / df.iloc[0, cnt5] * 100
            maxRamrate = resultList[3][i][1] / df.iloc[1, cnt5] * 100
            minCpuRate = resultList[4][i][1] / df.iloc[0, cnt5] * 100
            minRamrate = resultList[5][i][1] / df.iloc[1, cnt5] * 100

            if (maxCpuRate-aveCpuRate) > (aveCpuRate-minCpuRate):
                xValue = maxCpuRate-aveCpuRate
            elif (maxCpuRate-aveCpuRate) < (aveCpuRate-minCpuRate):
                xValue = aveCpuRate-minCpuRate
            elif (maxRamrate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = maxRamrate - aveRamRate
            elif (maxRamrate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = aveRamRate - minRamRate

            if rValue < xValue:
                rValue = xValue
                xPod = df.columns[cnt5]

    for dataList in targetDBList:
        cnt4 = 0
        cnt5 = 0
        while True:
            if df.columns[cnt4].find(dataList[0]) != -1:
                if df.columns[cnt4].find(dataList[0] + "-db") == -1:
                    if df.columns[cnt5].find(dataList[1]) != -1:
                        if df.columns[cnt5].find(dataList[1] + "-db") == -1:
                            break
                        else:
                            cnt5+=1
                    else:
                        cnt5+=1
                else:
                    cnt4+=1
            else:
                cnt4+=1

        for i in range(dim):
            aveCpuRate = resultDBList[0][i][0] / df.iloc[0, cnt4] * 100
            aveRamRate = resultDBList[1][i][0] / df.iloc[1, cnt4] * 100
            maxCpuRate = resultDBList[2][i][0] / df.iloc[0, cnt4] * 100
            maxRamRate = resultDBList[3][i][0] / df.iloc[1, cnt4] * 100
            minCpuRate = resultDBList[4][i][0] / df.iloc[0, cnt4] * 100
            minRamRate = resultDBList[5][i][0] / df.iloc[1, cnt4] * 100
            
            if (maxCpuRate-aveCpuRate) > (aveCpuRate-minCpuRate):
                xValue = maxCpuRate-aveCpuRate
            elif (maxCpuRate-aveCpuRate) < (aveCpuRate-minCpuRate):
                xValue = aveCpuRate-minCpuRate
            elif (maxRamrate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = maxRamrate - aveRamRate
            elif (maxRamrate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = aveRamRate - minRamRate

            if rValue < xValue:
                rValue = xValue
                xPod = df.columns[cnt4]

            aveCpuRate = resultDBList[0][i][1] / df.iloc[0, cnt5] * 100
            aveRamrate = resultDBList[1][i][1] / df.iloc[1, cnt5] * 100
            maxCpuRate = resultDBList[2][i][1] / df.iloc[0, cnt5] * 100
            maxRamrate = resultDBList[3][i][1] / df.iloc[1, cnt5] * 100
            minCpuRate = resultDBList[4][i][1] / df.iloc[0, cnt5] * 100
            minRamrate = resultDBList[5][i][1] / df.iloc[1, cnt5] * 100

            if (maxCpuRate-aveCpuRate) > (aveCpuRate-minCpuRate):
                xValue = maxCpuRate-aveCpuRate
            elif (maxCpuRate-aveCpuRate) < (aveCpuRate-minCpuRate):
                xValue = aveCpuRate-minCpuRate
            elif (maxRamrate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = maxRamrate - aveRamRate
            elif (maxRamrate - aveRamRate) > (aveRamRate - minRamRate):
                xValue = aveRamRate - minRamRate

            if rValue < xValue:
                rValue = xValue
                xPod = df.columns[cnt5]

    return xPod
            
path = "/home/nishijima/test/result/result.csv"
path2 = "/home/nishijima/test/monitor_data/shaped_data.csv"
path3 = "/home/nishijima/test/sockshop_resource.csv"

#実験によって変更
df = pd.read_csv("/home/nishijima/test/test_stats.csv")
cnt1 = 1
cnt2 = 0
cnt3 = 0
suspectList = []
trafficList = []
relationList = []
causeList = []
dbList = ["carts-db", "catalogue-db", "orders-db", "session-db", "user-db"]

for resTime in df.iloc[1:15, 7]:
    if resTime >= 3000.0:
        if df.iloc[cnt1, 1].find("detail") != -1:
            suspectList.append("catalogue")
        elif df.iloc[cnt1, 1].find("addresse") != -1:
            suspectList.append("user")
        elif df.iloc[cnt1, 1].find("cards") != -1:
            suspectList.append("payment")
        elif df.iloc[cnt1, 1].find("register") != -1:
            suspectList.append("user")
        elif df.iloc[cnt1, 1].find("cart") != -1:
            suspectList.append("carts")
        else:
            suspectList.append(df.iloc[cnt1, 1])
    cnt1 += 1

suspectList = [s.lstrip('/') for s in suspectList]

suspectList = list(set(suspectList))

with open(path, "r") as f:
    while True:
        dataList = f.readline()
        if dataList == '':
            break
        else:
            dataList = dataList.replace('\n', '')
            trafficList.append(dataList.split(','))
f.close()

for suspect in suspectList:
    for dataList in trafficList:
        if suspect == dataList[0]:
            while True:
                if cnt2 == len(dataList)-1:
                    if cnt3 == len(suspectList)-1:
                        cnt2 = 0
                        cnt3 = 0
                        break
                    else:
                        cnt2 = 0
                        cnt3 += 1
                else:
                    if dataList[cnt2] == suspectList[cnt3]:
                        cnt2 += 1
                        if dataList[0] != suspectList[cnt3]:
                            relationList.append([dataList[0],suspectList[cnt3]])
                            
                    else:
                        cnt2 += 1

df = pd.read_csv(path2)

print(suspectList)
print(relationList)

relationDBList = []
for dataList in relationList:
    xRelationDBList = []
    for dbData in dbList:
        if dbData.find(dataList[0]) != -1:
            xRelationDBList.append(dbData)
        if dbData.find(dataList[1]) != -1:
            xRelationDBList.append(dbData)
    if dataList[0] == dataList[1]:    
        relationDBList.append(xRelationDBList)
#print(f"dbList:{relationDBList}")

result = pullList(path2, relationList)
#print(f"nomal:{result}")
resultDB = pullList(path2, relationDBList)
#print(f"db:{resultDB}")

all_empty = all(element == "" for element in relationList)

print(f"結果:{compareUsage(path3, result, resultDB, relationList, relationDBList)}")

if all_empty:
    print(f"結果:{suspectList}")
else:
    print(f"結果:{compareUsage(path3, result, resultDB, relationList, relationDBList)}")