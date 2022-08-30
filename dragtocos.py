import copy
import json
import sys
with open(sys.argv[1]+'.json') as jfile:
    orig=json.load(jfile)
new=copy.deepcopy(orig)
cos_edge_square={"env_func": "cos_edge_square","paradict": {"ramp_fraction": 0.25}}
for gatename,gate in orig['Gates'].items():
    print(gatename)
    for pulseindex,pulse in enumerate(gate):
        pulsenew=pulse
        if (isinstance(pulse,dict)):
            for propkey,propvalue in pulse.items():
                if propkey=='env':
                    for envindex,envdict in enumerate(propvalue):
                        if 'env_func' in envdict:
                            if envdict['env_func']=='DRAG':
                                new['Gates'][gatename][pulseindex]['env']=cos_edge_square

with open(sys.argv[1]+"_cos.json",'w') as jfile:
    json.dump(new,jfile,indent=4)
