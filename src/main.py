from stay_detection import stay_detection
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/skyle/Wadizu/data/gps_test.csv", sep= ',')
gps_trajectory = np.array(data)

clustered_gps, cluster_cnt = stay_detection(gps_trajectory)
print(clustered_gps)
print(cluster_cnt)