import test_script

if __name__ == "__main__":
    rtt_size_map = {                    '128': 'test_images/test_128.jpg',
                   }
    for size in rtt_size_map.keys():
        for wait_time in [0.5,0.2,0.1, 0.01]:
            for num_servers in [1,2,4]:
                average_time = test_script.run_test_loop(wait_time,100,num_servers,500,rtt_size_map[size])
                print('average RTT for wait time {} with {} servers is {} seconds'.format(wait_time, num_servers, average_time))
