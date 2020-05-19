import os
import pandas as pd
from random import random

def read_data(folder='Dataset/', dataset_portion=0.1):
    """
    Searches for dataset files in the given folder.
    """
    
    pmd     = pd.DataFrame();
    metrics = pd.DataFrame();

    # List files in the given directory    
    files = []
    for file in os.listdir(folder):
        if file.endswith('MethodMetrics.csv'):
            files.append(file.replace('MethodMetrics.csv', ''))
    
    for file in files:
        if random() < dataset_portion:
            # Read data
            metrics_data = pd.read_csv(folder + file + 'MethodMetrics.csv', delimiter=';')
            pmd_data = pd.read_csv(folder + file + 'PMDViolations.csv', delimiter=';')
            
            # Append dataset
            metrics = pd.concat([metrics, metrics_data])
            pmd = pd.concat([pmd, pmd_data]);

    return metrics, pmd
