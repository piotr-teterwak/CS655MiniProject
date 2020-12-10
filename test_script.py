from multiprocessing.dummy import Pool
import requests
import numpy as np
from time import sleep
import time
import argparse

REST_API_URL = "http://10.10.5.1:5000/submit"

pool = Pool(1000)
s = requests.Session()
def run_test_loop(average_wait_interval,measurement_frequency,number_backend_servers,loop_length, image_path):
    times = []
    image = open(image_path, "rb").read()
    file_payload = {"image":image}
    data_payload = {"number_backend_servers": number_backend_servers}
    # Burn in the connection. 
    for x in range(10):
        s.post(REST_API_URL, files=file_payload, data=data_payload)
    for x in range(loop_length):
        wait_secs = np.random.poisson(average_wait_interval)
        sleep(wait_secs)
        start_time = time.time()
        future = pool.apply_async(s.post,[REST_API_URL], {'files':file_payload, 'data':data_payload})
        if ((x + 1)%measurement_frequency == 0):
            future.get()
            end_time = time.time()
            times.append(end_time - start_time)

    average_time = sum(times)/len(times)
    return(average_time)
