import xls_to_tmx
from pathlib import Path


class PYTMX:

    def __init__(self,filepath, srclang, tarlang):
        self.filepath = filepath
        self.srclang = srclang
        self.tarlang = tarlang

    def excel_to_tmx(self):

        dict = {
        'tmname': Path(self.filepath).stem + ' TM',
        'srclang': self.srclang,
        'tarlang': self.tarlang,
        }

        xls_to_tmx.convert(self.filepath, **dict)

if __name__=='__main__':
    ptx = PYTMX(r"C:\Users\elder\Desktop\windless_glossary\WINDLESS_Glossary_20220221 (1).xlsx", 'kr', 'en')
    ptx.excel_to_tmx()
