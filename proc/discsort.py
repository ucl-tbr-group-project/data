'''
Sorts run data into labelled subsets for each combination of discrete variable, combining all batches in runX directory.
'''

import os
import pandas as pd
import numpy as np
from ATE import data_utils

def disctrans(values):
    param_dict = [{'tungsten':0},
                  {'SiC':     0, 'eurofer':1},
                  {'H2O':     0, 'He':     1, 'D2O':2},
                  {'SiC':     0, 'eurofer':1},
                  {'Li4SiO4': 0, 'Li2TiO3':1},
                  {'Be':      0, 'Be12Ti': 1},
                  {'H2O':     0, 'He':     1, 'D2O':2}]
    
    it = np.nditer(values, flags=['f_index','refs_ok'])
    trans = ''
    while not it.finished:
        char = str(param_dict[it.index][it[0].item(0)])
        trans += char
        it.iternext()
    return trans


def discsort(numrun, data_dir='../'):

    indir = data_dir + 'run' + str(numrun)
    outdir = indir + 'dsort'
    if not os.path.exists(outdir): os.mkdir(outdir) 
    
    for filename in os.listdir(indir):
        if filename.endswith("out.csv"):
            inpath = os.path.join(indir,filename)
            tempdata = pd.read_csv(inpath)
            datakeys = tempdata.keys()
            break
    
    disc_cats = np.empty((1,2,3,2,2,2,3), dtype=np.dtype('<U7'))
    
    it = np.nditer(disc_cats, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        it[0] = ''.join(str(e) for e in it.multi_index)
        it.iternext()
        
    for save_discid in np.nditer(disc_cats):  
    
        print(save_discid)
        save_data = pd.DataFrame(columns = datakeys.values) 
      
        for filename in os.listdir(indir):
            if filename.endswith("out.csv"):
                inpath = os.path.join(indir,filename)
                thisdata = pd.read_csv(inpath)
                c, d, y = data_utils.c_d_y_split(thisdata)
       
                for i in range(d.index.size):
                    data_discid = disctrans(d.values[i])
                    if (data_discid == save_discid.item(0)):
                        save_data = save_data.append(thisdata.loc[i], ignore_index=True)
                        #print(thisdata.loc[i])
                        #print(save_data)
        
        outname = save_discid.item(0) + '.csv'
        outpath = os.path.join(outdir,outname)
        save_data.to_csv(outpath)
        print(save_data.index.size)
    #print(disc_cats)
        
        
if __name__ == '__main__':
    discsort(0)

