#!/usr/bin/env python
import random

class Lane:
	# mile
    LANE_LENGTH = 0.1

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
		if random.random() < spawnRate * interv:
			self.vehicles.append(Vehicle())
