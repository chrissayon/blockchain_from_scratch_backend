## Tests
'''
flake8
python3 -m pytest backend/tests
'''

## Running the application and API
python3 -m backend.app
gunicorn -b 127.0.0.1:4000 backend.app