import flask
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.sav', 'rb'))


@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    avg_time_in_store = float(request.form['Avg_Time_in_Store'])
    avg_time_on_app = float(request.form['Avg_App_Time'])
    avg_time_on_website = float(request.form['Avg_Website_Time'])
    length_of_subscription = float(request.form['Length_of_Subscription'])
    result = model.predict([[avg_time_in_store, avg_time_on_app, avg_time_on_website, length_of_subscription]])[0]
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run()
