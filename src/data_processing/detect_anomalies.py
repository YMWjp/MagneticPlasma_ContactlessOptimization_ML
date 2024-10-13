import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def detect_changes(shot_no, datapath='dataset_25_7.csv'):
    """指定されたショット番号に対して変化点検出を行い、異常なデータポイントを特定・可視化する。

    Args:
        shot_no (int): 対象のショット番号。
        datapath (str): データファイルへのパス。
    """
    # データの読み込み
    data = pd.read_csv(datapath)

    # 指定ショットのデータをフィルタリング
    filtered_data = data[data['shotNO'] == shot_no]
    if filtered_data.empty:
        print(f"No data found for Shot Number: {shot_no}")
        return

    times = filtered_data['times'].values

    # 時間範囲のフィルタリング
    start_time = 3.5
    end_time = 9.0
    mask = (times > start_time) & (times < end_time)
    df = filtered_data[mask]
    times = times[mask]

    # プロットの設定
    indices = [2, 3, 7, 8, 9, 10]
    plt.rcParams.update({'font.size': 10, 'lines.linewidth': 2})
    fig, axes = plt.subplots(len(indices), 1, figsize=(6, 10), sharex=True)

    for j, i in enumerate(indices):
        # ここで change_detection 関数を適切に実装する必要があります
        # 例としてダミーデータを使用
        ab = df.iloc[:, i].values
        label = f'Parameter {i}'
        if i == 3:
            axes[j].set_ylim(0, 0.000008)
        axes[j].plot(times, ab, label=label)
        axes[j].set_ylabel(label)
        axes[j].legend()

    for ax in axes:
        ax.set_xlim(3.5, 9)
        ax.grid(True)
        ax.axvspan(4.86, 7.4, color='lightblue', alpha=0.4)

    axes[-1].set_xlabel("Time[s]")
    fig.suptitle(f'Shot Number: {shot_no} Anomaly Detection')
    plt.subplots_adjust(left=0.25, right=0.85, bottom=0.15, top=0.90, hspace=0.4)

    # グラフを保存
    plt.savefig(f'./results/anomalies/shot_{shot_no}_anomaly_detection.png')
    plt.close()
    print(f"Anomaly detection visualization saved for Shot Number: {shot_no}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='変化点検出スクリプト')
    parser.add_argument('--shot', type=int, required=True, help='対象ショット番号')
    parser.add_argument('--data', type=str, default='dataset_25_7.csv', help='データファイルのパス')
    args = parser.parse_args()

    detect_changes(args.shot, args.data)