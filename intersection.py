#!/usr/bin/env python
import random

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
		self.disToEntry = LANE_LENGTH
		self.v = DEFAULT_V
		# set no acceleration by default
		self.a = 0

	def move(self, interv):
		"""
		move happens in interv seconds
		"""
		# convert velocity to seconds first
		self.disToEntry -= self.v / 3600 * interv
		self.v += self.a

class Lane:
	def __init__(self, laneId, spawnRate):
		"""
		spawnRate is vehicles/second
		"""
		self.laneId = laneId
		self.spawnRate = spawnRate

		# array that keeps the vehicles in this lane
		self.vehicles = []
	
	def spawn(self, interv):
		"""
		Add a vehicle with spawning probability
		interv is in seconds.
		"""
		# Follow Poission Distribution
		if random.random() < spawnRate:
			self.vehicles.append(Vehicle())
