# DIS Load Balancer Comparison and Performance Analysis

Overview of the Project:

The main objective of this project is to implement and compare the performance of various load balancing algorithms in order to identify the most efficient one among them in terms of balancing the load within the various servers in the network and thus enhancing the overall performance of the system. 

Network Architecture:

The architecture we have chosen consists of one load balancer, five servers and one client.
HTTP requests are sent to the load balancer by the client which then allocates these requests to the different servers in the network using the below mentioned load balancing algorithms.


Load Balancing Algorithms:

In the project, we have compared the working of 4 load balancing algorithms namely Round Robin, Weighted Round Robin, Least Response Time load balancing, and Chained Fallover load balancing algorithm. 

Evaluation Metrics:

We have tried to measure the performance of these algorithms based on metrics such as Throughput, Latency, Scalability etc. to provide actual performance data.

Tools used for Evaluation and associated network layer:

For conducting our evaluation, we have used the WRK2 benchmarking tool which will function at Layer 7 of the network. 

Projected Outcome:

This detailed analysis will help network and system administrators and architects to choose the best load balancing algorithm out of the ones we’ve taken into consideration based on the type of network scenarios.

Solution Implementation:

Technical details and Tech Stack used

Programming Language used:

For the purpose of creating the network and the load balancer, we have used Python as the programming language. 
There are two main files created using Python, namely network and load balancer.

Implementation Details:

The network consists of five servers, one load balancer, and one client. 

The repository contains two Python files namely server.py and loadbalancer.py.

In order to form the network, we open the terminal and run the following command:

python3 loadbalancer.py

Upon this, the loadbalancer window will prompt the user to select the load balancing algorithm out of the 4 we've considered, to be used by the load balancer.

Then we open 5 different terminal windows for running the server code in order to form the network.
We allocate different port numbers to each of these servers in order to commmunicate with them.
For the purpose of testing, we have assigned port numbers 8000, 8001, 8002, 8003 and 8004 to the 5 respective servers.
Command (To be run on each terminal window):

python3 server.py

WRK2 benchmarking tool has been used to measure the performance of these load balancing algorithms on parameters such as Throughput, Latency, and Number of socket errors. We have used Github to host our source code along with the documentation for the project.

To test the network:

We run the following commands to download and build WRK2:

git clone https://github.com/giltene/wrk2.git
cd wrk2
make

Once WRK2 is built, we can run the following command to test our network and see the data:

./wrk -t2 -c50 -d20s -R5000 --latency http://localhost:8080

The port number 8080 mentioned in the command above is the port, the load balancer is running on.

t is the number of threads
c is the number of concurrent connections
d is the duration of the test
R is the number of requests per second

Github Repository:

The github repository has been made public for easy access of the codes and the associated documentation.
