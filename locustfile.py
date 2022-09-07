from locust import HttpUser, task
# import json
from data_test import input_data

class HousePredictorTaskSet(HttpUser):

	@task
	def get_home_route(self):
		self.client.get('/')

	@task
	def post_prediction(self):
		self.client.post('/predict', json=input_data)
