from app import app
import json

def test_home_route():
    r = app.test_client().get('/')
    assert b'<h3>Sklearn Prediction Home</h3>' in r.data

def test_predict_route():
    r = app.test_client().post('/predict', data=json.dumps(input_data), content_type='application/json')
    prediction = int(r.json['prediction'][0])
    assert prediction == 20


input_data ={
    'CHAS':{
      '0':0
    },
    'RM':{
      '0':6.575
    },
    'TAX':{
      '0':296.0
    },
    'PTRATIO':{
       '0':15.3
    },
    'B':{
       '0':396.9
    },
    'LSTAT':{
       '0':4.98
    }
}
