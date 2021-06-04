import numpy as np
import pandas as pd

def sort_descending_cluster_list(cluster_list, index):
    columns=['cluster_num', 'start_timestamp', 'end_timestamp', 'interval_timestamp', 'start_latitude', 'start_longtitude', 'avg_latitude', 'avg_longtitude', 'cluster_cnt', 'farthest_distance']
    data = pd.DataFrame(cluster_list, columns=columns)
    
    data = data.sort_values(columns[index], ascending=False)
    sorted_cluster_list = data.to_numpy()
    
    return sorted_cluster_list