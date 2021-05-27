from cluster_merging import cluster_merging
from stay_detection import stay_detection
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/skyle/Wadizu/data/1day.csv", sep= ',', header= None)
gps_trajectory = np.array(data)

clustered_gps_trajectory, cluster_list = stay_detection(gps_trajectory)
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/clusterd_gps.txt", clustered_gps_trajectory, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/clusterd_cnt_list1.txt", cluster_list, fmt='%s')

merged_gps, merged_cluster_list = cluster_merging(clustered_gps_trajectory, cluster_list)
clusters = np.sort(merged_cluster_list, axis= 0)[::-1]
clusters = np.flip(clusters)
np.savetxt("C:/Users/skyle/Wadizu/test_txt/test.txt", clusters, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/merged_gps.txt", merged_gps, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/merged_cluster_list1.txt", merged_cluster_list, fmt='%s')