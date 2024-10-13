import os
import numpy as np
from GetFiles import GetFiles

class CalcMPEXP(GetFiles):
    def process_data(self):
        """データ処理のメインロジックを実行するメソッド。"""
        getfile_status = self.getfile_dat()
        
        if getfile_status == -1:
            print("SOME DATA MISSING")
            print(self.missing_list)
            if len(self.missing_list) > 1 and not set(self.missing_list).issubset({"fig_h2", "lhdcxs7_nion"}):
                return -1
        elif getfile_status == 2:
            return -1

        self.calculate_firc()
        if self.calculate_thomson() == -1 or len(self.nel) == 0:
            return -1

        self.calculate_bolo()
        if self.calculate_geom() == -1:
            return -1

        if self.set_time_range() == -1:
            return "MPexp error"

        self.retrieve_ech()
        self.retrieve_nbi()
        self.calculate_wp()
        self.retrieve_imp()
        self.retrieve_Ip()
        self.retrieve_Isat()

        self.calculate_ISS_Wp()
        self.export_data()
        return 1