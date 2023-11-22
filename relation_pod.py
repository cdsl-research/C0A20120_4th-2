import subprocess

cnt = 0

#引数はKialiAPIから取得した文章と各Podの名前が記入されたリスト，返り値として
def relationChecks(origntxt, sList, xservice):

    #返り値であるにどのPodのトラフィックかを判別するため，先頭に該当するPodの名前を格納
    relationList = [xservice]

    #KialiAPIから取得したトラフィックに関する文章からつながりのあるPodを取得
    for service in sList:
        if origntxt.find(service) != -1:
            relationList.append(service)

    return relationList


#各Podの名前
serviceList = ["carts", "carts-db", "catalogue", "catalogue-db", "front-end", "orders", "orders-db", "payment", "queue-master", "rabbitmq", "session-db", "shipping", "user", "user-db"]
serviceTrafficList = []

#各PodのトラフィックをKialiAPIを用いて取得
for service in serviceList: 
    cnt = 0
    command = ["curl", "http://192.168.100.35:30652/kiali/api/namespaces/sock-shop/workloads/" + service + "/graph"]
    APIresult = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    APIresult = str(APIresult)

    trafficList = relationChecks(APIresult, serviceList, service)
    serviceTrafficList.append(trafficList)

#今回の出力結果を/home/nishijima/test/resultにresult.csvとして保存
path = "/home/nishijima/test/result/result.csv"
with open(path, mode='w') as f:
    for resultList in serviceTrafficList:
        for result in resultList:
            if cnt < len(resultList)-1:
                f.write(result + ',')
                cnt += 1
            else:
                f.write(result + '\n')
                cnt = 0
f.close()