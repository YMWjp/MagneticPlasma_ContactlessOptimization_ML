import glob
import os
import numpy as np
from utils.igetfile import igetfile

class GetFiles:
    def __init__(self, shotNO, diag_list='diagnames.csv'):
        self.shotNO = shotNO
        self.diag_list = np.genfromtxt(diag_list, dtype=str, usecols=0, delimiter=',')
        self.missing_list = []

    def getfile_dat(self):
        """サーバから必要なデータファイルを取得するメソッド。"""
        status = 1
        for diag in self.diag_list:
            outputname = f'egdata/{diag}@{self.shotNO}.dat'
            if os.path.isfile(outputname):
                print(f"{outputname}: 存在します")
                continue
            print(f"{outputname}: 存在しません")

            # データ取得試行
            try:
                if igetfile(diag, self.shotNO, 1, outputname) is None:
                    print(f'shot:{self.shotNO} diag:{diag} は存在しません')
                    self.missing_list.append(diag)
                    status = -1
            except ValueError:
                print('ZIPファイルの読み込みエラー')
                return 2
        return status

    def remove_files(self):
        """特定のショット番号に関連するファイルを削除するメソッド。"""
        print("*****ファイル削除開始*****")
        zip_patterns = f'*_{self.shotNO}*.zip'
        dat_patterns = f'*@{self.shotNO}.dat'

        zip_files = glob.glob(zip_patterns)
        dat_files = glob.glob(dat_patterns)

        for file in zip_files + dat_files:
            os.remove(file)
            print(f"{file} を削除しました")

        return 1