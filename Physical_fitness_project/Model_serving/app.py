# flask file에 대한 구성
# 기존에 실습했던 내용을 바탕으로 구성해본다.
# 나이, 키, 몸무게, 제자리멀리뛰기, 셔틀런 성적을 입력하여 체지방을 추정하자.

from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('fat_rate.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def get_fat():
    data_age = request.form['data_age']
    data_height = request.form['data_height']
    data_weight = request.form['data_weight']
    data_jump = request.form['data_jump']
    data_shuttle = request.form['data_shuttle']
    data = np.array([[data_age, data_height, data_weight, data_jump, data_shuttle]])
    pred = model.predict(data)
    # 유효하지 않은 값을 뱉을 수 있으므로, 이를 방지하기 위한 예외 처리를 넣는다.
    if pred < 0:
        pred = 0
    if pred >= 100:
        pred = 100

    return render_template('prediction.html', data = pred)

if __name__== "__main__":
    app.run(debug=True)
