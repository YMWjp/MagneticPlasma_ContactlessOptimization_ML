import os
import requests

def getdata(shotNO, diag, datapath=''):
    """HTTP経由でデータファイルを取得し、指定パスに保存する関数。

    Args:
        shotNO (int): ショット番号。
        diag (str): 診断名。
        datapath (str, optional): 保存先パス。デフォルトは空文字で診断名とショット番号から生成。

    Returns:
        int: HTTPステータスコードまたは1（成功時）。
    """
    subshotNO = 1  # サブショット番号
    url = f'http://exp.lhd.nifs.ac.jp/opendata/LHD/webapi.fcgi?cmd=getfile&diag={diag}&shotno={shotNO}&subno={subshotNO}'

    response = requests.get(url)

    if not datapath:
        datapath = f'{diag}@{shotNO}.dat'

    if response.status_code == 200:
        if os.path.isfile(datapath):
            print(f"{datapath}: 既に存在します")
            return 1
        with open(datapath, 'w') as f:
            f.write(response.text)
        print(f"{datapath}: 作成しました")
    else:
        print(f'HTTPリクエストエラー: ステータスコード {response.status_code}')
        print(f'URL: {url}')
    
    return response.status_code