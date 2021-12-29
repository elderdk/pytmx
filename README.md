# pytmx
Python-written tool for handling tmx files.

excel_to_tmx()
--------------
Converts excel file (both .xls and .xlsx) to .tmx that can be imported into Trados Translation Memory.


Example:

Fill in the variables with information accurate to your use case and run pytmx.excel_to_tmx()

    from pytmx import pytmx

        filepath = r""
        srclang = "en-us",
        tarlang = "ko-kr"

        ptx = pytmx(filepath, srclang, tarlang)

        ptx.excel_to_tmx()
