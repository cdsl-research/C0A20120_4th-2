import subprocess
import os

def run_monitor(duration_seconds):
    # 出力ファイルパス
    output_file = "/home/nishijima/test/monitor_data/data.csv"

    # シェルスクリプトを実行するコマンド
    command = f'''
        #!/bin/bash
        # CSVファイルのヘッダを作成
        echo "timestamp,pod,cpu_usage(m),memory_usage(Mi)" > {output_file}

        # 開始時刻
        start_time=$(date +%s)

        while :
        do
            current_time=$(date +%s)
            elapsed_time=$((current_time - start_time))

            # 指定した時間を超えたら終了
            if [ "$elapsed_time" -ge "{duration_seconds}" ]; then
                break
            fi

            timestamp=$(date '+%Y-%m-%d %H:%M:%S')

            # すべてのPodのリソース使用量を取得し、単位を取り除く
            kubectl top pod -n sock-shop --no-headers 2>/dev/null | while read -r pod cpu_usage memory_usage; do
                cpu_usage=$(echo "$cpu_usage" | tr -d 'm')
                memory_usage=$(echo "$memory_usage" | tr -d 'Mi')
                echo "$timestamp,$pod,$cpu_usage,$memory_usage" >> {output_file}
            done &  # バックグラウンドで実行

            sleep 1
        done
    '''

    # スクリプトを一時ファイルに書き込む
    script_file = "temp_script.sh"
    with open(script_file, "w") as f:
        f.write(command)

    # シェルスクリプトを実行
    subprocess.run(f"bash {script_file}", shell=True)

    # 一時ファイルを削除
    os.remove(script_file)
#追加
run_monitor(420)