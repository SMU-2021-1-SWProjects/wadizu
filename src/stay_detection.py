import numpy as np

# gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간)
def stay_detection(gps_trajectory):
    clustered_gps_trajectory = np.copy(gps_trajectory)
    cluster_cnt_list = np.array([])
    eps = 0.000009
    start_latitude = clustered_gps_trajectory[0][0]
    start_longtitude = clustered_gps_trajectory[0][1]
    cluster_num = 1
    cluster_cnt = 0
    
    # cluster_num column 추가
    clustered_gps_trajectory = np.insert(clustered_gps_trajectory, len(clustered_gps_trajectory[0]), 0, axis=1)
    
    for i in range(0, len(clustered_gps_trajectory), 1):
        # 위도, 경도가 임계값 범위이면 같은 cluster
        if abs(start_latitude - clustered_gps_trajectory[i][0]) < eps and \
           abs(start_longtitude - clustered_gps_trajectory[i][1]) < eps:
            clustered_gps_trajectory[i][-1] = cluster_num
            cluster_cnt += 1
        
        # 다른 cluster로 지정
        else:
            cluster_cnt_list = np.insert(cluster_cnt_list, len(cluster_cnt_list), cluster_cnt, axis=0)
            cluster_cnt = 1
            cluster_num += 1
            clustered_gps_trajectory[i][-1] = cluster_num
            start_latitude = clustered_gps_trajectory[i][0]
            start_longtitude = clustered_gps_trajectory[i][1]
    
    return clustered_gps_trajectory, cluster_cnt_list