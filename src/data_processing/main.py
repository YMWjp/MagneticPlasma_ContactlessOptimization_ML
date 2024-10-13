import argparse
from collect_data import main as collect_data_main
from visualize_data import visualize_shot
from detect_anomalies import detect_changes

def parse_arguments():
    parser = argparse.ArgumentParser(description='データ処理用メインスクリプト')
    parser.add_argument('--collect', action='store_true', help='データ収集と前処理を実行')
    parser.add_argument('--visualize', type=int, help='指定ショット番号のデータを可視化')
    parser.add_argument('--detect', type=int, help='指定ショット番号の異常検知を実行')
    parser.add_argument('--savename', type=str, default='dataset_25_7.csv', help='保存するCSVファイル名')
    parser.add_argument('--labelname', type=str, default='labels.csv', help='ラベルファイル名')
    parser.add_argument('--ion', type=str, help='イオン種別（オプション）')
    return parser.parse_args()

def main():
    args = parse_arguments()

    if args.collect:
        collect_data_main(savename=args.savename, labelname=args.labelname, ion=args.ion)

    if args.visualize:
        visualize_shot(args.visualize, datapath=args.savename)

    if args.detect:
        detect_changes(args.detect, datapath=args.savename)

if __name__ == '__main__':
    main()