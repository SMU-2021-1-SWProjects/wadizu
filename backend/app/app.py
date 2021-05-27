import os
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
from stay_detection import stay_detection
from cluster_merging import cluster_merging

app = Flask(__name__)
 
@app.route('/')
def render_main():
    return render_template('app.html')

@app.route('/clustering',methods=['POST'])
def clustering(gps = None, clusters = None):
    render_template('app.html')
    if request.method == 'POST':
        data = pd.read_csv("C:/Users/skyle/Wadizu/data/1day.csv", sep= ',', header= None)
        gps_trajectory = np.array(data)

        clustered_gps_trajectory, clustered_cnt_list = stay_detection(gps_trajectory)
        
        merged_gps, merged_cluster_list = cluster_merging(clustered_gps_trajectory, clustered_cnt_list)
    
    return render_template('clustering.html', gps=merged_gps, clusters=merged_cluster_list)

# file이 submit되면 전달되는 페이지
# upload.html에서 form이 제출되면 /file_uploaded로 옮겨지게 되어 있음.
@app.route('/file_uploaded', methods = ['POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        f = request.files['file1']
        # 파일 객체 혹은 파일 스트림을 가져오고, html 파일에서 넘겨지는 값의 이름을 file1으로 했기 때문에 file1임. 
        f.save(f'uploads/{secure_filename(f.filename)}') # 업로드된 파일을 특정 폴더에저장하고, 
        data= pd.read_csv('uploads/{secure_filename(f.filename)}', header= None)
        return data
    
if __name__ == '__main__':
    app.run(port=8000, debug=True)