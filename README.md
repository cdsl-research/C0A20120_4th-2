# C0A20120_4th-2

アクセスシナリオで負荷試験を実行中，下記のコマンドを実行．Podのリソース利用率を取得．**monitor_data/data.csv**が出力結果．

`python3 cpu_usage.py`

**data.csv**を成型する．**shaped_data.csv**が出力結果．

`python3 shape_data.py`

KialiAPIを使用して各Pod間のトラフィックを取得し，通信経路を取得．**result/result.csv**が出力結果．

`python3 relation_pod.py`

**result.csv**と**shaped_data.csv**を使用し，マイクロサービスの応答時間増加の原因を特定．
`python3 detection.py`
