from multiprocessing.dummy import Pool
import requests
import numpy as np
from time import sleep
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("average_wait_interval", help="Average wait between simulated traffic requests", type=float)
parser.add_argument("measurement_frequency", help="Measure rtt every measure_frequency requests", type=int)
parser.add_argument("number_backend_servers", help="How many backend servers to use", type=int)
args = parser.parse_args()

TEST_IMAGE_PATH="test_images/test.jpg"
#REST_API_URL = "http://192.12.245.161:5000/submit"
REST_API_URL = "http://localhost:5000/submit"

pool = Pool(1000)

if __name__ == '__main__':

    times = []

    for x in range(10000):
        image = open(TEST_IMAGE_PATH, "rb").read()
        file_payload = {"image":image}
        data_payload = {"number_backend_servers": args.number_backend_servers}
        wait_secs = np.random.poisson(args.average_wait_interval)
        sleep(wait_secs)
        start_time = time.time()
        future = pool.apply_async(requests.post,[REST_API_URL], {'files':file_payload, 'data':data_payload})
        if (x%args.measurement_frequency == 0):
            future.get()
            end_time = time.time()
            times.append(end_time - start_time)
            print(times[-1])
