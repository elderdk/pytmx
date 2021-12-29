from xls_to_tmx.xls_to_tmx import convert
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

        convert(self.filepath, **dict)

if __name__=='__main__':

    filepath = r""
    srclang = "en-us",
    tarlang = "ko-kr"

    pytmx = PYTMX(filepath, srclang, tarlang)

    pytmx.excel_to_tmx()
