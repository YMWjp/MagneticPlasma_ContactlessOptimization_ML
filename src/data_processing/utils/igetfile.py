import os
import zipfile
from ftplib import FTP
import requests

def ftp_list(targetpath):
    """指定パスのファイルリストを取得するFTP関数。

    Args:
        targetpath (str): 対象パス。

    Returns:
        list: ファイル名のリスト。
    """
    ftp = FTP('egftp1.lhd.nifs.ac.jp')
    ftp.login()
    file_list = ftp.nlst(targetpath)
    ftp.quit()
    return file_list

def unzip_file(targetfile):
    """ZIPファイルを解凍し、内容を保存する関数。

    Args:
        targetfile (str): 解凍するZIPファイルのパス。

    Returns:
        list: 解凍されたファイル名のリスト。
    """
    with zipfile.ZipFile(targetfile, 'r') as zf:
        extracted_files = zf.namelist()
        zf.extractall()
    os.remove(targetfile)
    return extracted_files

def igetfile(diagname, shotno, subshot, outputname):
    """指定された診断名とショット番号からデータファイルを取得する関数。

    Args:
        diagname (str): 診断名。
        shotno (int): ショット番号。
        subshot (int): サブショット番号。
        outputname (str): 保存先ファイル名。

    Returns:
        str or None: 保存先ファイル名またはNone（失敗時）。
    """
    return ftp_get_from_http(shotno, diagname, subshot, outputname)

def ftp_get_from_http(shotNO, diagname, subshotNO=1, savename=''):
    """HTTP経由でFTPデータを取得する関数。

    Args:
        shotNO (int): ショット番号。
        diagname (str): 診断名。
        subshotNO (int, optional): サブショット番号。デフォルトは1。
        savename (str, optional): 保存先ファイル名。デフォルトは診断名とショット番号から生成。

    Returns:
        int: HTTPステータスコード。
    """
    url = f'http://exp.lhd.nifs.ac.jp/opendata/LHD/webapi.fcgi?cmd=getfile&diag={diagname}&shotno={shotNO}&subno={subshotNO}'
    response = requests.get(url)

    if response.status_code == 200:
        if not savename:
            savename = f'{diagname}@{shotNO}.dat'
        with open(savename, 'w') as f:
            f.write(response.text)
        print(f"{savename}: データを保存しました")
    else:
        print(f'HTTPリクエストエラー: ステータスコード {response.status_code} for URL {url}')
    
    return response.status_code