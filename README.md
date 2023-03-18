# Distributed Cake
This was created for the Distributed Systems course (521290S).

## Course Project Overview
The project is a AI-based Tic-Tac-Toe game that implements an architecture in which multiple players can connect to a server and play a game. We thought of making the game more interesting by making the tic-tac-toe an AI-based game. This means that players would be able to connect to the main server and play with the server. In response, the server plays back with each independent player concurrently, and the server can handle as many clients as possible (game players) if it has sufficient resources. 

The project will use centralized organization system architecture object-based where we have a broker and use RPC (Remote Procedure Call) for communication. 

To evaluate the performance of the system, we will launch the server and players in ascending fashion. This means that first the server is run and waits for new players. Then, statistics such as network bandwidth usage, memory usage, CPU usage, and disk transfer rate will be collected. We then launch a new player and collect the statistics. This process happens repeatedly until we reach our computer’s limit. Then we will redo the entire process and collect statistics each time. We do this procedure multiple times and compare the results. We would take an average between the results and consider it as our final evaluation. 

Detailed statistics and plots will be provided as well to measure if this implementation can deliver the same performance across all the clients and distribute the resources accordingly. 
