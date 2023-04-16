from __future__ import barry_as_FLUFL
import json
d={
    'foo':'barry',
    'alice':1,
    'wonder_d':[1,2,3]
}
with open("varun2.txt",'w') as f:
    json.dump(d,f)
with open("varun2.txt",'r') as f:
    d=json.load(f)