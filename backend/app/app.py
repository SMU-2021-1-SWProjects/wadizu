from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from stay_detection import stay_detection
from cluster_merging import cluster_merging
from sort_descending_cluster_list import sort_descending_cluster_list

app = Flask(__name__)
 
@app.route('/')
def render_main():
    return render_template('app.html')

@app.route('/clustering',methods=['POST'])
def clustering(gps= None, clusters= None, clusters_cnt= None, clusters_time= None, gps_visualizing= None,cluster_visualizing= None):
    if request.method == 'POST':
        
        data = pd.read_csv('./data/file.filename', sep= ',', header= None)
        gps_trajectory = np.array(data)

        clustered_gps_trajectory, clustered_cnt_list = stay_detection(gps_trajectory)
        
        merged_gps, merged_cluster_list = cluster_merging(clustered_gps_trajectory, clustered_cnt_list)
        sorted_by_cluster_cnt = sort_descending_cluster_list(merged_cluster_list, 8)
        sorted_by_cluster_time = sort_descending_cluster_list(merged_cluster_list, 3)
        
        gps_lat_long = merged_gps[:, 0:2]
        
        clster_num = merged_cluster_list[:, 0:1]
        clster_alat_along = merged_cluster_list[:, 6:8]
        clster_distance = merged_cluster_list[:, -2:]
        clsuster_num_alat_along_distance = np.hstack((clster_num, clster_alat_along, clster_distance))
        clsuster_num_alat_along_distance = np.delete(clsuster_num_alat_along_distance, -2, axis=1)
        
        clsuster_num_alat_along_distance_dict = pd.DataFrame(clsuster_num_alat_along_distance, columns=["cluster_num", "avg_latitude", "avg_longtitude", "farthest_distance"])
        
    
    return render_template('clustering.html', gps= merged_gps, clusters= merged_cluster_list, clusters_cnt= sorted_by_cluster_cnt, clusters_time= sorted_by_cluster_time, gps_visualizing= gps_lat_long, cluster_visualizing= clsuster_num_alat_along_distance_dict)

@app.route('/upload_done', methods= ['POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        file = request.files['data_file']
        file.save('./data/file.filename') # 업로드된 파일을 특정 폴더에저장하고, 

        return render_template('app.html')
    
if __name__ == '__main__':
    app.run(port=8000, debug=True)