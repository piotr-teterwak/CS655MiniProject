# Image Recognition as a Distributed Web Service

This is github rep for CS655 GENI miniproject completed by Piotr Teterwak and Arsenii Mustafin.

The repository contain installation files, requirements and scripts needed to reproduce our experiments. Copy of our report can be found [here](https://docs.google.com/document/d/1ZrOqQRH866swqNUJgfwdP4bd2cT5bQS1hMqrs-XMJrI/edit?usp=sharing).

The website should be hosted at http://192.12.245.161:5000/. It's very simple! 

# Reproduction instructions

Either create a new slice with the [rspec](https://raw.githubusercontent.com/piotr-teterwak/CS655MiniProject/main/image_class.rspec) or use the existing slice MiniProjectImgClass. 

Log into each node and clone this repo. 

Run the `install_script.sh` in each node, and follow by running `source ~/.bashrc`. 

On the servers, run `python server_script.py`. On the load balancer, run `python load_balancer.py`. If you are spinning it up on a new slice, then change the ip in `templates/index.html`. 

To get experimental numbers, run `python test_rtt.py` and `python test_scaling.py` on the client.

# Technical details

As described in the project writeup, the servers are running a flask server with a prediction function MobileNetV2 trained on Imagenet.

The load balancer also runs a Flask Server. When it gets a GET request, it hosts the simple webpage at http://http://192.12.245.161:5000/
When it gets a POST request, at /submit, it randomly selects 1-of-n servers. This balances the load in expectation. Importantly, this server is threaded, so it can process many requests at once. 

`test_script.py` submits POST requests asynchronously to the load balancer in a loop, with wait calls between requests. This wait is average_wait_interval seconds long, where n is drawn from a Poisson distrubution. Every 'measurement frequency' reqeust is done synchronously, and the RTT is measured. 

# Video

See a tour of our project [here] (https://github.com/piotr-teterwak/CS655MiniProject/blob/main/miniproject_video.mp4).
