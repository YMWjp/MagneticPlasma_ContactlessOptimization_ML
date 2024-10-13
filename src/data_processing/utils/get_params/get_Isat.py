import os
from eg_read import eg_read

def get_Isat(self):
    """Isat パラメータを取得し、クラス変数に設定するメソッド。"""
    filepath = f"egdata/DivLis_tor_sum@{self.shotNO}.dat"
    if os.path.isfile(filepath):
        eg = eg_read(filepath)
        gdn_info = self.get_gdn_info(filepath)
        params = ["2L", "2R", "4L", "4R", "6L", "6R", "7L", "7R", "8L", "8R", "9L", "9R", "10L", "10R"]
        
        for i, param in enumerate(params):
            key = f'Isat_{param}'
            try:
                setattr(
                    self,
                    key,
                    eg.interpolate('Iis_' + param + f'@{gdn_info[i]}', self.time_list),
                )
            except ValueError:
                setattr(self, key, np.nan)

        # Isat_7L のデータ整形
        self.clean_Isat_7L()

def clean_Isat_7L(self):
    """Isat_7L の外れ値を除去し、データを整形するメソッド。"""
    if hasattr(self, 'Isat_7L'):
        for i in range(2, len(self.Isat_7L) - 2):
            if self.Isat_7L[i] < 0.0001:
                self.Isat_7L[i] = (self.Isat_7L[i - 2] + self.Isat_7L[i + 2]) / 2

        isat_copy = self.Isat_7L.copy()
        for i in range(1, len(self.Isat_7L)):
            if isat_copy[i] < isat_copy[i - 1] / 1.5:
                self.Isat_7L[i] = isat_copy[i - 1]