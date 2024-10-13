import pandas as pd
import matplotlib.pyplot as plt

def visualize_shot(shot_no, datapath='dataset_25_7.csv'):
    """指定されたショット番号のデータを可視化し、グラフを保存する。

    Args:
        shot_no (int): 対象のショット番号。
        datapath (str): データファイルへのパス。
    """
    # フォントサイズを設定
    plt.rcParams.update({'font.size': 14})

    # CSVファイルからデータを読み込む
    data = pd.read_csv(datapath)

    # 指定されたショット番号のデータをフィルタリング
    filtered_data = data[data['shotNO'] == shot_no]
    
    if filtered_data.empty:
        print(f"No data found for Shot Number: {shot_no}")
        return

    # プロットの設定
    fig, axs = plt.subplots(3, 1, figsize=(8, 5.5), sharex=True)
    plt.subplots_adjust(hspace=0.1)

    # 一番上のグラフ: Wpとnel
    ax1 = axs[0]
    ax2 = ax1.twinx()
    ax1.plot(filtered_data['times'], filtered_data['nel'], label='Nel')
    ax2.plot(filtered_data['times'], filtered_data['Wp'] * 1000, 'orange', label='Wp')
    ax1.set_ylabel(r'$N_{e}\ [10^{19}\ \mathrm{m}^{-3}]$')
    ax2.set_ylabel('$W_{p}$[kJ]')
    ax1.grid(True)

    # 中央のグラフ: PinputとPrad
    axs[1].plot(filtered_data['times'], filtered_data['Pinput'], 'orange', label='Pinput')
    axs[1].plot(filtered_data['times'], filtered_data['Prad'], label='Prad')
    axs[1].set_ylabel('$P_{rad},P_{in}$[MW]')
    axs[1].grid(True)

    # 一番下のグラフ: Isat@7L
    axs[2].plot(filtered_data['times'], filtered_data['Isat@7L'], label='Isat@7L')
    axs[2].set_xlabel('Time[s]')
    axs[2].set_ylabel('$I_{sat}$[A]')
    axs[2].grid(True)

    # 横軸の範囲を設定
    for ax in axs:
        ax.set_xlim(left=3.0, right=8.7)

    # 時間範囲を淡い青色で塗りつぶす
    for ax in axs:
        ax.axvspan(4.86, 7.4, color='lightblue', alpha=0.4)

    # グラフを保存
    plt.savefig(f'./results/visualizations/shot_{shot_no}_overview.png')
    plt.close()
    print(f"Visualization saved for Shot Number: {shot_no}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='データの可視化スクリプト')
    parser.add_argument('--shot', type=int, required=True, help='対象ショット番号')
    parser.add_argument('--data', type=str, default='dataset_25_7.csv', help='データファイルのパス')
    args = parser.parse_args()

    visualize_shot(args.shot, args.data)