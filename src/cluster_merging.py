import numpy as np

# clustered_gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간, 클러스터 cluster_num)
# cluster_cnt_list의 column은 (cluster_num, 시작 시간, 끝 시간, 위도, 경도, cluster_cnt)

def cluster_merging(clustered_gps_trajectory, cluster_cnt_list):
    merged_gps_trajectory = np.copy(clustered_gps_trajectory)
    merged_cluster_cnt_list = np.copy(cluster_cnt_list)
    merged_cluster_nums = np.empty(shape=(0, 2), dtype= np.float64)
    eps = 0.000009 * 5
    
    for i in range(0, len(merged_cluster_cnt_list), 1):
        for j in range(i, len(merged_cluster_cnt_list), 1):
            if i != j:
                # 위도, 경도가 임계값 범위이면 같은 cluster
                if abs(merged_cluster_cnt_list[i][3] - merged_cluster_cnt_list[j][3]) <= eps and \
                abs(merged_cluster_cnt_list[i][4] - merged_cluster_cnt_list[j][4]) <= eps:
                    # 서로 다른 걸 비교할 때만 merge
                    if merged_cluster_cnt_list[j][0] != merged_cluster_cnt_list[i][0]:
                        merged_cluster_nums = np.insert(merged_cluster_nums, len(merged_cluster_nums), [merged_cluster_cnt_list[j][0], merged_cluster_cnt_list[i][0]], axis= 0)
                        merged_cluster_cnt_list[j][0] = merged_cluster_cnt_list[i][0]
        
    # reclustering gps_trajectory
    for i in range(0, len(merged_cluster_nums), 1):
        for j in range(0, len(merged_gps_trajectory), 1):
            if merged_cluster_nums[i][0] == merged_gps_trajectory[j][-1]:
                merged_gps_trajectory[j][-1] = merged_cluster_nums[i][1]

    return merged_gps_trajectory, merged_cluster_cnt_list