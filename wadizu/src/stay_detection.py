import numpy as np


# gps_trajectory의 column은 (위도, 경도, 0, 고도, 타임스탬프, 날짜, 시간)
def stay_detection(gps_trajectory):
    clustered_gps_trajectory = np.copy(gps_trajectory)
    cluster_list = np.empty(shape=(0, 9), dtype=np.float64)
    eps = 0.000009 * 5
    start_latitude = clustered_gps_trajectory[0][0]
    start_longtitude = clustered_gps_trajectory[0][1]
    sum_latitude = start_latitude
    sum_longtitude = start_longtitude
    start_timestamp = clustered_gps_trajectory[0][4]
    end_timestamp = clustered_gps_trajectory[0][4]
    interval_timestamp = 0
    cluster_num = 1
    cluster_cnt = 0
    min_cluster_num = 2

    # cluster_num column 추가
    clustered_gps_trajectory = np.insert(clustered_gps_trajectory, len(clustered_gps_trajectory[0]), 0, axis=1)

    for i in range(0, len(clustered_gps_trajectory), 1):

        # 위도, 경도가 임계값 범위이면 같은 cluster
        if pow(pow(start_latitude - clustered_gps_trajectory[i][0], 2) + pow(
                start_longtitude - clustered_gps_trajectory[i][1], 2), 0.5) <= eps:
            clustered_gps_trajectory[i][-1] = cluster_num
            cluster_cnt += 1
            sum_latitude += clustered_gps_trajectory[i][0]
            sum_longtitude += clustered_gps_trajectory[i][1]

            if clustered_gps_trajectory[i][4] > end_timestamp:
                end_timestamp = clustered_gps_trajectory[i][4]

        # 다른 cluster로 지정
        else:
            if cluster_cnt >= min_cluster_num:
                interval_timestamp = abs(start_timestamp - end_timestamp)
                cluster_list = np.insert(cluster_list, len(cluster_list),
                                         [cluster_num, start_timestamp, end_timestamp, interval_timestamp,
                                          start_latitude, start_longtitude, sum_latitude / cluster_cnt,
                                          sum_longtitude / cluster_cnt, cluster_cnt], axis=0)

            cluster_cnt = 1
            cluster_num += 1
            clustered_gps_trajectory[i][-1] = cluster_num
            start_latitude = clustered_gps_trajectory[i][0]
            start_longtitude = clustered_gps_trajectory[i][1]
            sum_latitude = start_latitude
            sum_longtitude = start_longtitude
            start_timestamp = clustered_gps_trajectory[i][4]
            end_timestamp = clustered_gps_trajectory[i][4]

        # 마지막 데이터 cluster_cnt_list에 삽입
        if i == len(clustered_gps_trajectory) - 1:
            interval_timestamp = abs(start_timestamp - end_timestamp)
            cluster_list = np.insert(cluster_list, len(cluster_list),
                                     [cluster_num, start_timestamp, end_timestamp, interval_timestamp, start_latitude,
                                      start_longtitude, sum_latitude / cluster_cnt, sum_longtitude / cluster_cnt,
                                      cluster_cnt], axis=0)

    return clustered_gps_trajectory, cluster_list