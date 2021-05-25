from flask import Flask, render_template, redirect, request, url_for
import numpy as np
import pandas as pd
from stay_detection import stay_detection
from cluster_merging import cluster_merging

app = Flask(__name__)
 
@app.route('/')
def inputTest():
    return render_template('app.html')
    
@app.route('/clustering')
def clstering_template():
    return render_template('app.html')

@app.route('/clustering',methods=['POST'])
def clustering():
    render_template('app.html')
    if request.method == 'POST':
        data = pd.read_csv("C:/Users/skyle/Wadizu/data/1day.csv", sep= ',', header= None)
        gps_trajectory = np.array(data)

        clustered_gps_trajectory, clustered_cnt_list = stay_detection(gps_trajectory)
        
        merged_gps, merged_cluster_cnt_list = cluster_merging(clustered_gps_trajectory, clustered_cnt_list)
    
    return "Clustering 완료\n{0}\n{1}".format(merged_gps, merged_cluster_cnt_list)
        # temp = request.form['clustered_gps_trajectory', 'clustered_cnt_list']
    # else:
        # temp = None
    # return redirect(url_for('inputTest'))
 
if __name__ == '__main__':
    app.run(port=8000, debug=True)