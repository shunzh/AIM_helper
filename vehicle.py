#!/usr/bin/env python

class Vehicle:
	# mile
	LANE_LENGTH = 0.1
	# mile per hour (mph)
	DEFAULT_V = 35

	def __init__(self, laneId, vId):
		self.laneId = laneId
		self.vId = vId

		# policy-related
		self.admitted = False

		# position-related
		self.p = - LANE_LENGTH

		# dynamics-related
		self.v = DEFAULT_V
		# set no acceleration by default
		self.a = 0
		# brake set to false by default. Otherwise, need to brake before disToEntry == 0
		self.brake = False

		self.dec = DecelerationModel()

	def move(self, interv):
		"""
		move happens in interv seconds
		"""
		if not self.admitted and self.p < 0:
			self.a = self.dec.getAcc(-self.p, self.v)

		# convert velocity to seconds first
		self.p += self.v / 3600 * interv
		self.v += self.a

	def admit(self):
		self.admitted = True


class DecelerationModel:
	DEC_LENGTH = 0.02

	def getAcc(self, dis, v):
		"""
		a * t^2 / 2 = dis
		"""
		if dis > DEC_LENGTH:
			return 0
		else:
			#TODO make sure
			return - 0.1 * dis / (v * v)
