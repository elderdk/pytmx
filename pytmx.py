from xls_to_tmx.xls_to_tmx import convert
from pathlib import Path


if __name__=='__main__':
    excel_file = r""

    dict = {
    'tmname': Path(excel_file).stem + ' TM',
    'srclang': 'ko-kr',
    'tarlang': 'en-us',
    }

    convert(excel_file, **dict)