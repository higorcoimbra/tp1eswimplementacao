from django.test import TestCase
from django.test import Client

# Create your tests here.
class AccessViewTestCase(TestCase):
	def test_access_denied(self):
		c = Client()
		response = c.get('/home')
		self.assertEqual(403,response.status_code)

	def test_access_accepted(self):
		c = Client()
		c.login(username='teste', password='esw123456')
		response = c.get('/home')
		self.assertEqual(200,response.status_code)