"""
To be used to demo 'pp' of pdb.
"""

import json
import pdb
with open('./create_order_payload.json', 'r') as f:
    content = json.load(f)

print(content)
pdb.set_trace()

print("DONE!!")