from stay_detection import stay_detection
from stay_merging import stay_merging
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/skyle/Wadizu/data/gps_test.csv", sep= ',')
gps_trajectory = np.array(data)

clustered_gps = stay_detection(gps_trajectory)

merged_clustered_gps, cluster_cnt = stay_merging(clustered_gps)
print(merged_clustered_gps)
print(cluster_cnt)