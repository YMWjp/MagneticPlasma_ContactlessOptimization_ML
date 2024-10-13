import datetime
import json
import numpy as np
import matplotlib.pyplot as plt
from classes.CalcMPEXP import CalcMPEXP
from classes.DetachData import DetachData

def main(savename="dataset_25_7.csv", labelname="labels.csv", ion=None):
    """データ収集および前処理を行うメイン関数。
    各ショット番号に対して必要なデータを取得し、CSVファイルに保存する。
    """
    with open("configs/config.json", "r") as config_file:
        config = json.load(config_file)

    shotNOs = np.genfromtxt(
        labelname, delimiter=",", skip_header=1, usecols=0, dtype=int
    )
    
    # 必要な事前ラベルを格納
    types = np.genfromtxt(labelname, delimiter=',', skip_header=1, usecols=1, dtype=str) if config.get("use_types", False) else []
    remarks = np.genfromtxt(labelname, delimiter=',', skip_header=1, usecols=3, dtype=str) if config.get("use_remarks", False) else []
    about = np.genfromtxt(labelname, delimiter=',', skip_header=1, usecols=4, dtype=float) if config.get("use_about", False) else []

    print("Shot Numbers:", shotNOs)
    
    with open(savename, "w") as f_handle:
        header = config.get("header", [])
        f_handle.write(", ".join(header) + "\n")

    # エラー記録
    with open("errorshot.txt", mode="a") as f:
        f.write(datetime.datetime.today().strftime("\n%Y/%m/%d"))

    for i, shotNO in enumerate(shotNOs):
        print(f"Processing Shot Number: {shotNO}")
        nel_data = DetachData(
            shotNO=shotNO,
            type=types[i] if config.get("use_types", False) else "",
            remark=remarks[i] if config.get("use_remarks", False) else "",
            about=about[i] if config.get("use_about", False) else 4,
            savename=savename,
        )
        nel_data.remove_files()  # 古いデータを削除
        main_return = nel_data.process_shot()

        if main_return == -1:
            nel_data.remove_files()
            continue
        elif main_return == "MPexp error":
            with open("errorshot.txt", mode="a") as f:
                f.write(f"\n{shotNO}")
            nel_data.remove_files()
            continue

        nel_data.save_dataset(header)    # CSVへ出力
        nel_data.plot_labels(save=True)  # 画像として保存
        nel_data.remove_files()