
import json
import os
import glob.glob as glob
import numpy as np

def write_json(dict, json_filename):
    
    json_object = json.dumps(dict, indent=4)

    with open(json_filename, "w") as outfile:
        outfile.write(json_object)
        
def rename_files(filepath):
    
    files = glob.glob(filepath + '/*.png')
    files.sort()
    
    """
    Rename files from 1-indexed to 0-indexed
    """
    
    for file in files:
        src = file.split('/')[-1].split('.')[0]
        new_file = file.replace(src, str(int(src)-1).zfill(5))
        os.rename(file, new_file)

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)
