from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

class UploadCsvTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # exampl of valid 
        self.valid_csv = SimpleUploadedFile(
            "valid.csv",
            b"name,email,age\nsidh,sidh@example.com,25\nraj,raj@example.com,30",
            content_type ="text/csv"
            )
        # example of invalid
        self.invalid_csv =  SimpleUploadedFile(
            "invalid.csv",
            b"name,email,age\nsidh,sidh@example.com,150",
            content_type ="text/csv"
            )

    # condition for testing valid
    def test_valid_upload(self):
        response = self.client.post('/user_api/api/upload/',{'file':self.valid_csv})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['saved_records'],2)
        self.assertEqual(response.data['rejected_records'],0)

    # condition for testing valid
    def test_invalid_upload(self):
        response = self.client.post('/user_api/api/upload/',{'file':self.invalid_csv})
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['saved_records'],0)
        self.assertEqual(response.data['rejected_records'],1)
        self.assertIn('errors', response.data)