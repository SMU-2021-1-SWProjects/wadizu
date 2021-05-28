import numpy as np

# clustered_gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간, cluster_num)
# cluster_list의 column은 (cluster_num, 시작 시간, 끝 시간, 시작 위도, 시작 경도, 평균 위도, 평균 경도, cluster_cnt)

def cluster_merging(clustered_gps_trajectory, cluster_list):
    merged_gps_trajectory = np.copy(clustered_gps_trajectory)
    merged_cluster_list = np.copy(cluster_list)
    merged_cluster_nums = np.empty(shape=(0, 2), dtype= np.float64)
    eps = 0.000009 * 5
    farthest_distance = 0
    
    merged_cluster_list = np.insert(merged_cluster_list, len(merged_cluster_list[0]), 0, axis=1)
    
    for i in range(0, len(merged_cluster_list), 1):
        for j in range(i, len(merged_cluster_list), 1):
            if i != j:
                # 위도, 경도가 임계값 범위이면 같은 cluster
                if abs(merged_cluster_list[i][4] - merged_cluster_list[j][4]) <= eps and \
                abs(merged_cluster_list[i][5] - merged_cluster_list[j][5]) <= eps:                   
                    # 서로 다른 걸 비교할 때만 merge
                    if merged_cluster_list[j][0] != merged_cluster_list[i][0]:
                        merged_cluster_nums = np.insert(merged_cluster_nums, len(merged_cluster_nums), [merged_cluster_list[j][0], merged_cluster_list[i][0]], axis= 0)
                        merged_cluster_list[j][0] = merged_cluster_list[i][0]

    # 평균 좌표로부터 가장 먼 좌표의 거리 파악
    for i in range(0, len(merged_cluster_list), 1):
        for j in range(0, len(merged_gps_trajectory), 1):
            if(merged_cluster_list[i][0] == merged_gps_trajectory[j][-1]):
                if abs(merged_cluster_list[i][6] - merged_gps_trajectory[j][0]) + abs(merged_cluster_list[i][7] - merged_gps_trajectory[j][1]) > farthest_distance:
                    farthest_distance = abs(merged_cluster_list[i][6] - merged_gps_trajectory[j][0]) + abs(merged_cluster_list[i][7] - merged_gps_trajectory[j][1])

        merged_cluster_list[i][-1] = farthest_distance
        farthest_distance = 0

    # reclustering gps_trajectory(cluster_num이 0은 unclustering 되었다는 것을 의미)
    for i in range(0, len(merged_cluster_nums), 1):
        for j in range(0, len(merged_gps_trajectory), 1):
            # clustering 되지 않은 좌표들은 cluster_num을 0으로 지정
            if merged_gps_trajectory[j][-1] not in merged_cluster_list and merged_gps_trajectory[j][-1] not in merged_cluster_nums:
                merged_gps_trajectory[j][-1] = 0
            else:
                if merged_cluster_nums[i][0] == merged_gps_trajectory[j][-1]:
                    merged_gps_trajectory[j][-1] = merged_cluster_nums[i][1]

    return merged_gps_trajectory, merged_cluster_list