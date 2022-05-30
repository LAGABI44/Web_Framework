#import flask
# import imageio
from flask import Flask, request, render_template
# import pickle
import joblib
import numpy as np

# model = pickle.load(open('model.pkl', 'rb'))
model = joblib.load('model.pkl')
scaler_rf = joblib.load('scale_rf.pkl')


# 플라스크 객체 생성(확인용)   
app = Flask(__name__)
   
# index 페이지 라우팅
@app.route('/')  #, methods=['GET','POST']
def main() :
   return render_template('home.html')

@app.route('/after')  
def input() :
   return render_template('after.html')

# 데이터 예측 처리
@app.route('/predict', methods=['POST'])
def after():
    data1 = request.form['sex']
    data2 = request.form['age']
    data3 = request.form['FBS']
    data4 = request.form['SBP']
    data5 = request.form['DBP']
    data6 = request.form['BMI']
    arr = np.array([[data1, data2, data3, data4, data5, data6]])
    #arr = scaler_rf.fit_transform(arr)
    pred = model.predict(arr)
    return render_template('result.html', data=pred)

if __name__ == "__main__":
    app.run(debug=True)