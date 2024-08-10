# Simulation Testbench
#
# Author: Neha Karanjkar
# Modified By : Kanwarraj singh(1903122) & Afzal Hussain(2103103)


import simpy
from Applications import SendingApplication,ReceivingApplication
from Channel import UnreliableChannel
from Protocol_rdt2 import *
#from Kanwarraj_Afzal_Protocol_rdt2.2 import *

# Create a simulation environment
env=simpy.Environment()

# Populate the simulation environment with objects:
sending_app	  = SendingApplication(env)
receiving_app = ReceivingApplication(env)
rdt_sender	  = rdt_Sender(env)
rdt_receiver  = rdt_Receiver(env)
channel_for_data  = UnreliableChannel(env=env,Pc=0.5,Pl=0,delay=2,name="DATA_CHANNEL")
channel_for_ack	  = UnreliableChannel(env=env,Pc=0,Pl=0,delay=2,name="ACK_CHANNEL")

# connect the objects together
# .....forward path...
sending_app.rdt_sender = rdt_sender
rdt_sender.channel = channel_for_data
channel_for_data.receiver = rdt_receiver
rdt_receiver.receiving_app = receiving_app
# ....backward path...for acks
rdt_receiver.channel = channel_for_ack
channel_for_ack.receiver = rdt_sender

# Run simulation
env.run(until=1000)

env.run(until = receiving_app.isCompleted)


t_avgs = []
    
# Run simulation
env.run(until=receiving_app.isCompleted)
current_t_avg = float('inf')
if len(rdt_sender.rtt) > 0:
     current_t_avg = sum(rdt_sender.rtt)/len(rdt_sender.rtt)
t_avgs.append(current_t_avg)
print("T_avg:", current_t_avg)

