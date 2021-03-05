#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/Users/niconi/venv/bin/python3
# -*- coding: utf-8 -*-
import re
import sys
from mitmproxy.tools.main import mitmweb
from mitmproxy.tools.main import mitmdump
if __name__ == '__main__':
    print(sys.argv)
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.argv.append('-s')
    sys.argv.append('../addons/addon.py')
    sys.argv.append('tls_passthrough1.py')
    print(sys.argv)
    sys.exit(mitmdump())