from datetime import datetime
import random
from math import pow
from Elgamal import encrypt, decrypt, gen_key, power


now = datetime.now()

# q = 75351678916126275070911666971000668671126954864773
# h =  40469056636531550400901060534053229751740864348668
# g =  28428146280977578079874795557361448784731238739466

class block:
	class Message:
		def __init__(self, topic, text):
			self.text = text
			self.topic = topic
			self.q = random.randint(int(pow(10, 20)), int(pow(10, 50)))
			self.g = random.randint(2, self.q)

			self.key = gen_key(self.q)# Private key for receiver
			self.h = power(self.g, self.key, self.q)
			self.encryptedMessage, self.p = encrypt(topic + text, self.q, self.h, self.g)
			self.topiclen = len(topic)

	def __init__(self, Prevusername, topic, text):
		self.time = now.strftime("%d/%m/%Y %H:%M:%S")
		self.prevusername = Prevusername
		self.message = block.Message(topic, text)

	def decryptBlock(self):
		decMessage = decrypt(self.message.encryptedMessage, self.message.p, self.message.key, self.message.q)
		decMessage = ''.join(decMessage)
		print("Decrypted Topic is :", decMessage[0 : self.message.topiclen])
		print("Decrypted Text is : ", decMessage[self.message.topiclen : ])

	def __str__(self):
		return f"Time is {self.time}\nTopic is {self.message.topic}\nText is {self.message.text}"

