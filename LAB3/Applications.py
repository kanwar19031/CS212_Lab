# SimPy models for the Sending and Receiving Applications.
#
# The sending application:
#	- keeps creating new messages
#	- requests the lower-layer (rdt_sender)
#	  to deliver each message using the rdt_send() function
#
# The receiving application:
#	- receives the message delivered by the lower-layer to its
#	   deliver_data() method.
#	- does some basic validation. 

# Author: Neha Karanjkar
# Modified By : Kanwarraj singh(1903122) & Afzal Hussain(2103103)


import simpy
import random
from Packet import Packet
import sys
class SendingApplication(object):

	def __init__(self,env):
		# Initialize variables
		self.env=env 
		self.rdt_sender=None
		self.total_messages_sent=0
		self.total_time = 0
		# start behavior
		self.env.process(self.behavior())

	def behavior(self):
		
		while True:
			# wait for a random amount of time
			#t=random.randint(1,5)
			delay_for_packet = random.randint(0,6)
			yield self.env.timeout(delay_for_packet)
			
			# create a message (its just a number, for now.)
			msg = self.total_messages_sent
			
			# try to send it.
			if self.rdt_sender.rdt_send(msg):
				# success.
				self.total_messages_sent+=1
				print("TIME:",self.env.now,"SENDING APP: sent data",msg)

class ReceivingApplication(object):

	def __init__(self,env):
		# Initialize variables
		self.env=env 
		self.total_packets_received=0
		self.isCompleted = env.event()

	def deliver_data(self,data):
		# This function is called by the lower-layer (rdt_receiver)
		# to deliver data to the Receiving Application
		print("TIME:",self.env.now,"RECEIVING APP: received data",data)
		
		# do some basic validation.
		if not (data==self.total_packets_received):
			print("ERROR!! RECEIVING APP: received wrong data:",data,",expected:",self.total_packets_received)
			print("Halting simulation...")
			sys.exit(0)
		self.total_packets_received+=1
		if self.total_packets_received==1000:
			print("\n-------- All 1000 ACKs recieved")
			self.isCompleted.succeed()

