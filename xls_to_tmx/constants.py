from pathlib import Path
from datetime import datetime

HEADER="""<?xml version="1.0" encoding="utf-8"?>
<tmx version="1.4">
  <header creationtool="{creationtool}" creationtoolversion="8.1" o-tmf="SDL TM8 Format" datatype="xml" segtype="sentence" adminlang="{srclang}" srclang="{srclang}" creationdate="{now}" creationid="{creationid}">
    <prop type="x-Recognizers">RecognizeAll</prop>
    <prop type="x-IncludesContextContent">True</prop>
    <prop type="x-TMName">{tmname}</prop>
    <prop type="x-TokenizerFlags">DefaultFlags</prop>
    <prop type="x-WordCountFlags">DefaultFlags</prop>
  </header>
  <body>"""

TU = """<tu creationdate="{now}" creationid="{creationid}" changedate="{now}" changeid="{creationid}" lastusagedate="{now}">
      <prop type="x-LastUsedBy">{creationid}</prop>
      <prop type="x-Origin">{origin}</prop>
      <prop type="x-ConfirmationLevel">ApprovedSignOff</prop>
      <tuv xml:lang="{srclang}">
        <seg>{source_seg}</seg>
      </tuv>
      <tuv xml:lang="{tarlang}">
        <seg>{target_seg}</seg>
      </tuv>
    </tu>"""

FOOTER = """
  </body>
</tmx>"""

BASE_DIR = Path(__file__).parent.parent
DEFAULT_KWARGS = {
  'creationtool': 'pytmx',
  'creationid': 'pytmx',
  'origin': 'pytmx',
  'now': datetime.now().strftime("%Y%m%dT%H%M%SZ")
  }