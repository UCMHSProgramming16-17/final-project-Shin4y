import requests as re
import json
import time
url = 'http://api.fixer.io/latest?symbols=USD,GBP'
info = json.loads(re.get(url).text)
print (json.dumps(info, indent=2, sort_keys=Tru
