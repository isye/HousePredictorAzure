from app import app
import json
from data_test import input_data

def test_home_route():
    r = app.test_client().get('/')
    assert b'<h3>Sklearn Prediction Home</h3>' in r.data

def test_predict_route():
    r = app.test_client().post('/predict', data=json.dumps(input_data), content_type='application/json')
    prediction = int(r.json['prediction'][0])
    assert prediction == 20



