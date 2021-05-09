import numpy as np

# clustered_gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간, 클러스터 번호)
# cluster_cnt의 column은 클러스터 번호 순으로 (클러스터 그룹원 수)

# def stay_merging(clustered_gps_trajectory, cluster_cnt):
def stay_merging(clustered_gps_trajectory):
    clustered_gps_trajectory = np.copy(clustered_gps_trajectory)
    standard_coordinate= np.array([[0,0]])
    cluster_cnt_list = np.array([])
    # merge 여부 식별 변수 추가
    clustered_gps_trajectory = np.insert(clustered_gps_trajectory, len(clustered_gps_trajectory[0]), False, axis= 1)
    initial_cluster_num = clustered_gps_trajectory[0][-2]
    eps = 0.000009
    cluster_cnt = 0
    
    # 각각 클러스터의 시작 좌표 식별
    for i in range(0, len(clustered_gps_trajectory), 1):
        if i == 0:
            standard_coordinate = np.insert(standard_coordinate, 1, [clustered_gps_trajectory[i][0], clustered_gps_trajectory[i][1]], axis= 0)
            standard_coordinate = np.delete(standard_coordinate, 0, axis= 0)
        else:
            if initial_cluster_num != clustered_gps_trajectory[i][-2]:
                standard_coordinate = np.insert(standard_coordinate, len(standard_coordinate), [clustered_gps_trajectory[i][0], clustered_gps_trajectory[i][1]], axis= 0)
    
    # 시작 좌표로 클러스터 merge
    for i in range(0, len(standard_coordinate), 1):
        for j in range(0, len(clustered_gps_trajectory), 1):
            clustered_gps_trajectory[j][-2] = 0
            
            if clustered_gps_trajectory[j][-1] == False:
                if abs(standard_coordinate[i][0] - clustered_gps_trajectory[j][0]) < eps and \
                   abs(standard_coordinate[i][1] - clustered_gps_trajectory[j][1]) < eps:
                    clustered_gps_trajectory[j][-2] = i + 1
                    clustered_gps_trajectory[j][-1] = True
    
    # 클러스터 그룹원 개수 식별
    for i in range(0, len(clustered_gps_trajectory), 1):
        if initial_cluster_num == clustered_gps_trajectory[i][-2]:
            cluster_cnt += 1
        else:
            cluster_cnt_list = np.insert(cluster_cnt_list, len(cluster_cnt_list), cluster_cnt, axis= 0)
            cluster_cnt = 0
    
    return clustered_gps_trajectory, cluster_cnt_list