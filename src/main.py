from cluster_merging import cluster_merging
from stay_detection import stay_detection
from sort_descending_cluster_list import sort_descending_cluster_list
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/skyle/Wadizu/data/1day.csv", sep= ',', header= None)
gps_trajectory = np.array(data)

clustered_gps_trajectory, cluster_list = stay_detection(gps_trajectory)
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/clusterd_gps2.txt", clustered_gps_trajectory, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/clusterd_list2.txt", cluster_list, fmt='%s')

merged_gps, merged_cluster_list = cluster_merging(clustered_gps_trajectory, cluster_list)
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/merged_gps2.txt", merged_gps, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/merged_cluster_list2.txt", merged_cluster_list, fmt='%s')

# clusters_cnt = sort_descending_cluster_list(merged_cluster_list, 8)
# clusters_time = sort_descending_cluster_list(merged_cluster_list, 3)
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/test1.txt", clusters_cnt, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/test2.txt", clusters_time, fmt='%s')