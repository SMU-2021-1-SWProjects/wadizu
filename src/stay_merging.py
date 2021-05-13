import numpy as np

# reclustered_gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간, 클러스터 cluster_num)
# cluster_cnt_list의 column은 (cluster_num, 위도, 경도, cluster_cnt)

def stay_merging(clustered_gps_trajectory, clustered_cnt_list):
    merged_gps_trajectory = np.copy(clustered_gps_trajectory)
    clustered_cnt_list = np.copy(clustered_cnt_list)
    merged_cnt_list = np.array([[0,0,0,0]], dtype= np.float64)
    # merge 여부 식별 변수 추가
    merged_gps_trajectory = np.insert(merged_gps_trajectory, len(merged_gps_trajectory[0]), False, axis= 1)
    eps = 0.000009 * 5
    cluster_num = 1
    cluster_cnt = 0
    sum_latitude  = 0
    sum_longtitude = 0
    
    # 시작 좌표로 클러스터 merge
    for i in range(0, len(clustered_cnt_list), 1):
        for j in range(0, len(merged_gps_trajectory), 1):
            # cluster 되지 않은 좌표에 대해서만 cluster 부여
            if merged_gps_trajectory[j][-1] == False:
                # cluster 되지 않은 좌표는 0으로 cluster_num 지정
                merged_gps_trajectory[j][-2] = 0
                # 위도, 경도가 임계값 범위이면 같은 cluster
                if abs(clustered_cnt_list[i][1] - merged_gps_trajectory[j][0]) <= eps and \
                   abs(clustered_cnt_list[i][2] - merged_gps_trajectory[j][1]) <= eps:
                    merged_gps_trajectory[j][-2] = cluster_num
                    merged_gps_trajectory[j][-1] = True
                    cluster_cnt += 1
                    sum_latitude += merged_gps_trajectory[i][0]
                    sum_longtitude += merged_gps_trajectory[i][1]
                
                # 비교 다하고 reclustered_cnt_list에 삽입
                if j == len(merged_gps_trajectory) - 1:
                    if i == 0:
                        merged_cnt_list = np.insert(merged_cnt_list, len(merged_cnt_list), [cluster_num, sum_latitude/cluster_cnt, sum_longtitude/cluster_cnt, cluster_cnt], axis= 0)
                        merged_cnt_list = np.delete(merged_cnt_list, 0, axis= 0)
                        cluster_num += 1
                    else:
                        if cluster_cnt != 0:
                            merged_cnt_list = np.insert(merged_cnt_list, len(merged_cnt_list), [cluster_num, sum_latitude/cluster_cnt, sum_longtitude/cluster_cnt, cluster_cnt], axis= 0)
                            cluster_num += 1
                            
                    cluster_cnt = 0
                    sum_latitude = 0
                    sum_longtitude = 0
    
    return merged_gps_trajectory, merged_cnt_list