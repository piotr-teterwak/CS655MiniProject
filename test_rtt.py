import test_script

if __name__ == "__main__":
    rtt_size_map = {'16': 'test_images/test_16.jpg',
                    '32': 'test_images/test_32.jpg',
                    '64': 'test_images/test_64.jpg',
                    '128': 'test_images/test_128.jpg',
                    '224': 'test_images/test_224.jpg',
                    '2000': 'test_images/test_2000.jpg'
                   }
    for size in rtt_size_map.keys():
        average_time = test_script.run_test_loop(0.01,1,4,50,rtt_size_map[size])
        print('average RTT for size {} is {} seconds'.format(size, average_time))
