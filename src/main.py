from stay_detection import stay_detection
from stay_merging import stay_merging
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/skyle/Wadizu/data/gps_test.csv", sep= ',', header= None)
gps_trajectory = np.array(data)

clustered_gps, cluster_cnt_list = stay_detection(gps_trajectory)

# np.savetxt("C:/Users/skyle/Wadizu/clustered_gps.txt", clustered_gps, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/clustered_cnt_list.txt", cluster_cnt_list, fmt='%s')

# merged_clustered_gps, cluster_cnt = stay_merging(clustered_gps)
# print(merged_clustered_gps)
# print(cluster_cnt)

# a = np.array([[0,0]])
# print(a)
# a = np.insert(a, len(a), [1,2], axis= 0)
# print(a)
# a = np.delete(a, 0, axis= 0)
# print(a)