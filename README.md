# pytmx
Python-written tool for handling tmx files.

excel_to_tmx()
--------------
Converts excel file (both .xls and .xlsx) to .tmx that can be imported into Trados Translation Memory.


Example:

In pytmx.py, fill in the variables with information accurate to your use case and run PYTMX.excel_to_tmx()

    filepath = r""
    srclang = "en-us",
    tarlang = "ko-kr"

    pytmx = PYTMX(filepath, srclang, tarlang)

    pytmx.excel_to_tmx()
