import numpy as np

# gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간)
def stay_detection(gps_trajectory):
    clustered_gps_trajectory = np.copy(gps_trajectory)
    clustered_cnt_list = np.array([[0,0,0,0]], dtype= np.float64)
    eps = 0.000009 * 5
    start_latitude = clustered_gps_trajectory[0][0]
    start_longtitude = clustered_gps_trajectory[0][1]
    cluster_num = 1
    cluster_cnt = 0
    
    # cluster_num column 추가
    clustered_gps_trajectory = np.insert(clustered_gps_trajectory, len(clustered_gps_trajectory[0]), 0, axis=1)
    
    for i in range(0, len(clustered_gps_trajectory), 1):
        # 첫 번째 데이터는 cluster1로 지정
        if i == 0:
            clustered_gps_trajectory[i][-1] = cluster_num
            cluster_cnt += 1
            clustered_cnt_list = np.insert(clustered_cnt_list, len(clustered_cnt_list), [cluster_num, start_latitude, start_longtitude, cluster_cnt], axis= 0)
            clustered_cnt_list = np.delete(clustered_cnt_list, 0, axis= 0)
        else:
            # 위도, 경도가 임계값 범위이면 같은 cluster
            if abs(start_latitude - clustered_gps_trajectory[i][0]) <= eps and \
               abs(start_longtitude - clustered_gps_trajectory[i][1]) <= eps:
                clustered_gps_trajectory[i][-1] = cluster_num
                cluster_cnt += 1
            
            # 다른 cluster로 지정
            else:
                if cluster_num == 1:
                    np.place(clustered_cnt_list, [cluster_num, start_latitude, start_longtitude, cluster_cnt], [cluster_num, start_latitude, start_longtitude, cluster_cnt])
                else:
                    clustered_cnt_list = np.insert(clustered_cnt_list, len(clustered_cnt_list), [cluster_num, start_latitude, start_longtitude, cluster_cnt], axis=0)
                cluster_cnt = 1
                cluster_num += 1
                clustered_gps_trajectory[i][-1] = cluster_num
                start_latitude = clustered_gps_trajectory[i][0]
                start_longtitude = clustered_gps_trajectory[i][1]
                
                # 마지막 데이터 cluster_cnt_list에 삽입
                if i == len(clustered_gps_trajectory) - 1:
                    clustered_cnt_list = np.insert(clustered_cnt_list, len(clustered_cnt_list), [cluster_num, start_latitude, start_longtitude, cluster_cnt], axis=0)
    
    return clustered_gps_trajectory, clustered_cnt_list