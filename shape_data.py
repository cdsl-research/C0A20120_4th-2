import pandas as pd

#成型前のファイルのディレクトリ
df = pd.read_csv("/home/nishijima/test/monitor_data/data.csv")

#成型後のファイルのディレクトリ
path = "/home/nishijima/test/monitor_data/shaped_data.csv"
cnt1 = 0
cnt2 =0

#sock-shop内のPodのリスト
podList = [
    "orders-db-c6897fc87-lmpxx",
    "session-db-9dc55b5b-x95lx",
    "shipping-78db6c6958-zxb5v",
    "user-db-758477f574-rkmtn",
    "catalogue-7c89c4b8b7-777f4",
    "payment-66d9c6c5c8-d49qb",
    "user-5c8d59bcd4-mxpjd",
    "carts-5bb979cb6d-zdvn9",
    "rabbitmq-cbfd4b9db-rsrk7",
    "orders-d5f745cc6-4qnrb",
    "carts-db-98ff4cbc7-qrqpw",
    "catalogue-db-6d76c95d76-zgzr9",
    "queue-master-78b6f85bb7-dbmqf",
    "front-end-5d7b595bcd-4ftwm"
]

with open(path, 'w') as f:
    for pod in podList:
        f.write(',' + pod + ',')
    f.write('\n')
    while True:
        if df.iloc[cnt2+1, 1] == '':
            break
        else:
            f.write(df.iloc[cnt2, 0][-8:])
            for pod in podList:
                for i in range(14):
                    if pod == df.iloc[cnt2+cnt1, 1]:
                        f.write(',' + str(df.iloc[cnt2+cnt1, 2]) + ',' + str(df.iloc[cnt2+cnt1, 3]))
                        cnt1 += 1
                    else:
                        cnt1 += 1
                cnt1 = 0
            cnt2 += 14
            f.write('\n')