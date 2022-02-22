from pytmx import pytmx

if __name__=='__main__':
    filepath = r""
    srclang = "en-us"
    tarlang = "ko-kr"

    ptx = pytmx(filepath, srclang, tarlang)

    ptx.excel_to_tmx()