from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
import json

class APITest(TestCase):
    def test_register_company(self):
        url = reverse('register_company')
        data = {
            "companyName": "Test Company",
            "ownerName": "Test Owner",
            "rollNo": "123",
            "ownerEmail": "test@example.com",
            "accessCode": "abc123"
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Company registered successfully"})

    def test_obtain_auth_token(self):
        url = reverse('obtain_auth_token')
        data = {
            "companyName": "Test Company",
            "clientID": "Test Client ID",
            "clientSecret": "Test Client Secret",
            "ownerName": "Test Owner",
            "ownerEmail": "test@example.com",
            "rollNo": "123"
        }
        response = self.client.post(url, data=data, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("token" in response.json())

    def test_get_top_products(self):
        url = reverse('get_top_products', kwargs={"company_name": "TestCompany", "category_name": "TestCategory"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("top_products" in response.json())
