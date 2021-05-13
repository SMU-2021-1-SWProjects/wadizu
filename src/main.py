from stay_detection import stay_detection
from stay_merging import stay_merging
import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/skyle/Wadizu/data/gps_test.csv", sep= ',', header= None)
gps_trajectory = np.array(data)

clustered_gps_trajectory, clustered_cnt_list = stay_detection(gps_trajectory)

# np.savetxt("C:/Users/skyle/Wadizu/test_txt/clustered_gps.txt", clustered_gps_trajectory, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/clustered_cnt_list.txt", clustered_cnt_list, fmt='%s')

merged_gps, merged_cnt_list = stay_merging(clustered_gps_trajectory, clustered_cnt_list)
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/merged_gps.txt", merged_gps, fmt='%s')
# np.savetxt("C:/Users/skyle/Wadizu/test_txt/merged_cnt_list.txt", merged_cnt_list, fmt='%s')