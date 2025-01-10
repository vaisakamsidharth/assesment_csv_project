csv_project

This project is a Django REST Framework (DRF) API that enables users to upload a CSV file containing user data. The API validates the data and stores valid records in the database. It also provides detailed error reporting for invalid records.

Features

Upload a CSV file via a POST endpoint.

Validate the CSV data based on:

Name: Non-empty string.

Email: Valid email format.

Age: Integer between 0 and 120.

Gracefully skip duplicate email addresses.

Return a detailed summary of successful and failed records.

Provide detailed validation errors for rejected records.

Unit tests for functionality validation.

Installation

Clone the repository: git clone <repository_url>
cd <repository_folder>

Create and activate a virtual environment:
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

Run migrations:
python manage.py migrate


Start the server:

python manage.py runserver

Endpoint

POst url =http://127.0.0.1:8000/user_api/api/upload/

Request

Upload a CSV file with the following columns: name, email, age.

Example CSV content:
name,email,age
John Doe,john@example.com,30
Jane Smith,jane@example.com,25


succes response
{
  "total_records": 2,
  "successful_records": 2,
  "failed_records": 0,
  "errors": []
}
