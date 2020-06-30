import json
import pandas as pd
import os
from joblib import Parallel, delayed

res = {1: [], 2: [], 3: [], 4: [], 5: []}

def run_access(i):
    Parallel(n_jobs=2)(delayed(run_script)(i,k) for k in range(1,6))				
        
def run_script(i,k):
    command = "python scripts/generate.py ./headlines/headlines_{}.txt {}".format(i,k)
    print("executing "+command)
    os.system(command)
    with open('headlines_simplified/headlines_{}.txt_config_{}.txt'.format(i,k), 'r') as f:
        for line in f:        
            res[k].append(line)
    
	

with open('headlines-05022020.json', 'r', encoding="utf8") as json_file:
    id_ = 245
    data = {'id': [], 'title': [], 'source': []}
    id_list = []
    title_list = []
    source_list = []
    for line in json_file:
        h = json.loads(line)
        id_ = id_ + 1
        id_list.append(id_)
        title_list.append(h['title'])
        source_list.append(h['source'])
    data['id'] = id_list
    data['title'] = title_list
    data['source'] = source_list
    counter = 0
    for t in title_list:
        i = int(counter/50) + 1
        with open('headlines/headlines_{}.txt'.format(i), 'a') as f:
            f.write(t + "\n")
        counter = counter + 1
        if counter % 50 == 0:
            run_access(i)
    run_access(i) 
    
    data['config_1'] = res[1]
    data['config_2'] = res[2]    
    data['config_3'] = res[3]
    data['config_4'] = res[4]
    data['config_5'] = res[5]    

    df = pd.DataFrame(data)
    df.to_csv('headlines.csv', index=False)
        
