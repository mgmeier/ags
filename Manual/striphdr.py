#!/usr/bin/env python

import sys
import re

# Format actutor.htm files to make it suitable for inclusion in html docs.

TEMPLATE = """\
<html>
  <head>
    <style type="text/css"><!--
      body {{
        font-family: Verdana;
        font-size: 10pt;
      }}
      a {{
        font-weight: bold;
      }}
    --></style>
  </head>
  <body>{body}</body>
</html>
"""

def main():
    with file(sys.argv[1], 'rb') as inp:
        buf = inp.read()

    # startstr = "<td width=\"550\">"
    startstr = "<td class=\"maintext\">"
    start = buf.index(startstr) + len(startstr)
    endre = re.compile(r"\s*</td>\s*</tr>\s*</table>\s*</td>\s*</tr>", re.MULTILINE|re.IGNORECASE)
    end = endre.search(buf, start).start()

    buf = buf[start:end]

    # actutor has been slotted into 29,30
    buf = buf.replace("actutor.htm", "ags29.htm")
    buf = buf.replace("actutor2.htm", "ags30.htm")

    with file(sys.argv[2], 'wb') as oup:
        oup.write(TEMPLATE.format(body=buf))

if __name__ == "__main__":
    main()
