#!/usr/bin/env python
import policy

from intersection import Lane

class IntersectionManager:
	MAX_TIME = 1000

	"""
	Main file for intersection simulator.
	No grid world simulation done. Taken as points.
	"""
	def __init__(self, laneNum, spawnRateSpec, policy):
		"""
		Initialize lanes and spawning points
		"""
		self.lanes = [Lane(i, spawnRateSpec[i]) for i in range(0, laneNum)]
		self.policy = policy

	def step(self, intv):
		"""
		One step of the simulator

		Usually called linearly, possibly called recursively (trying each possibility)
		"""
		for lane in lanes:
			lane.spawn(intv) # spawn according to the interval
			for v in lane:
				v.move()

	def log(self):
		"""
		Save necessary data to output
		"""
		print "log here."

	def main(self):
		"""
		Main function of the simulator
		"""
		t = 0

		intv = 0.1
		while t < self.MAX_TIME:
			# let policy modify reservation status
			self.policy.step(self.lanes)
			# let vehicles move
			step(intv)

			t += intv

		log()

if __name__ == "__main__":
	laneNum = 12
	spawnRateSpec = [.1] * laneNum

	im = IntersectionManager(laneNum, spawnRateSpec, policy.Optimal())
	im.main()
