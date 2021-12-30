import pytmx.xls_to_tmx
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

        pytmx.xls_to_tmx.convert(self.filepath, **dict)

if __name__=='__main__':
    pass
