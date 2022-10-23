from locust import task
from locust import between
from locust import HttpUser

sample = [[6.4,3.5,4.5,1.2]]

class MLZoomUser(HttpUser):
    """
    Usage:
        Start locust load testing client with:
            locust -H http://localhost:3000
        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn
        rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)
    
'''
QUESTION 6

Which model has better performance at higher volumes?

With a maximum concurrency of 2000 and a generation rate of 500.

Model_1: RPS 612
Model_2: RPS 563

Model 1 has better performance at higher volumes.

'''