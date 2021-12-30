from pytmx import pytmx

if __name__=='__main__':
    filepath = r"C:\Users\elder\Desktop\KRAFTON Glossary-JOEL_edited - 복사본.xlsx"
    srclang = "en-us",
    tarlang = "ko-kr"

    ptx = pytmx(filepath, srclang, tarlang)

    ptx.excel_to_tmx()