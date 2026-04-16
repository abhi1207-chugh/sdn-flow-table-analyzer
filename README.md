NAME:ABHINAV CHUHG
SRN:PES2UG24AM007
Problem Statement

Traditional networks lack centralized control and dynamic flow visibility. This project demonstrates how Software Defined Networking (SDN) can be used to analyze and monitor network traffic using a centralized controller.

The objective is to:

Capture packets in a Mininet network
Analyze flow entries dynamically
Understand how switches learn and install flow rules


Project Overview

This project uses:

POX Controller for SDN control logic
Mininet for network simulation
Custom Python scripts (analyzer.py, firewall.py)

The controller listens to packets and displays flow table entries for each switch



Setup Instructions
1. Install Required Tools
sudo apt update
sudo apt install mininet openvswitch-switch git python3
2. Clone Repository
git clone https://github.com/abhi1207-chugh/sdn-flow-table-analyzer.git
cd sdn-flow-table-analyzer
3. Navigate to POX
cd ~/pox


Execution Steps
Step 1: Run POX Controller
./pox.py forwarding.l2_learning analyzer
Step 2: Start Mininet Topology
sudo mn --topo linear,3 --controller=remote
Step 3: Test Connectivity
pingall



Expected Output:
1]Successful Ping
*** Results: 0% dropped (6/6 received)
2]Flow Table Entries (in POX terminal)

Example:

===== FLOW TABLE for Switch 1 =====
Match: ofp_match
in_port: 1
dl_src: xx:xx:xx:xx:xx:xx
dl_dst: xx:xx:xx:xx:xx:xx
nw_src: 10.0.0.1
nw_dst: 10.0.0.2
Status: ACTIVE


Project Files
File :	Description
analyzer.py :	Captures and prints flow table entries
firewall.py :	(Optional) Implements filtering logic
README.md  : Project documentation


Conclusion

This project demonstrates:

How SDN separates control and data planes
How flow rules are dynamically installed
Real-time monitoring of network traffic using POX
