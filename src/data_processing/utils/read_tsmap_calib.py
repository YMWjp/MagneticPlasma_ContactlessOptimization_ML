import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from egdb_class import egdb3d

class EG3DReader:
    def __init__(self, dataname):
        self.eg = egdb3d(dataname)
        self.eg.readFile()

        self.time = self.eg.dims(0)
        self.R = self.eg.dims(1)

        self.data = np.array(self.eg.data).reshape(-1, self.eg.ValNo).T

    def get_time_range_indices(self, time_point):
        """指定した時間点のデータ範囲を取得する。

        Args:
            time_point (float): 時間点。

        Returns:
            tuple: 開始インデックスと終了インデックス。
        """
        start = self.eg.value2idx(time_point, 0) * self.eg.DimSizes[1]
        end = start + self.eg.DimSizes[1]
        return start, end

    def interpolate_data(self, data, timelist):
        """データを指定した時間リストに補間する。

        Args:
            data (np.ndarray): 補間するデータ。
            timelist (np.ndarray): 補間先の時間リスト。

        Returns:
            np.ndarray: 補間済みデータ。
        """
        f = interpolate.interp1d(self.time, data, bounds_error=False, fill_value=0)
        return f(timelist)

    def get_te_position(self, t, target=10):
        """特定の温度位置を取得する。

        Args:
            t (float): 時間点。
            target (float, optional): 目標温度。デフォルトは10。

        Returns:
            float: 目標温度に対応する位置。
        """
        start, end = self.get_time_range_indices(t)
        Te_fit = self.data[self.eg.valname2idx('Te_fit')] * 1000  # eV
        R = np.array(self.R) * 100  # cmからmへの変換など

        Te_t = Te_fit[start:end][R > 400]
        f = interpolate.interp1d(Te_t, R[R > 400], bounds_error=False, fill_value=0)
        return f(target)

    def get_2D_data(self, valname):
        """指定した値名の2Dデータを取得する。

        Args:
            valname (str): 値名。

        Returns:
            np.ndarray: 2Dデータ配列。
        """
        data = self.data[self.eg.valname2idx(valname)]
        return data.reshape(len(self.time), len(self.R))