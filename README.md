## Run Tests

For Automation and API Tests you can run this from project root:

pytest --browser=firefox
or
pytest --browser=chrome

For Load Test you can run this from project root:

locust -f load_test/locustfile.py