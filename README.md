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
As discussed above, the load balancer is responsible for allocating the varying workload (HTTP Requests) to the available servers in the network using the four load balancing algorithms we’ve taken into account for the project, namely Round Robin, Weighted Round Robin, Least Response Time load balancing, and Chained Fallover load balancing algorithm. 
The load balancing algorithms have been evaluated at Layer 7 of the network which is the application layer, responsible for handling HTTP requests and responses. 
WRK2 benchmarking tool has been used to measure the performance of these load balancing algorithms on parameters such as Throughput, Latency, and Response Time. We have used Github to host our source code along with the documentation for the project.

Github Repository:

The github repository has been made public for easy access of the codes and the associated documentation.
