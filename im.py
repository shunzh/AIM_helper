#!/usr/bin/env python
import intersection, policy

class IntersectionManager:
	"""
	Main file for intersection simulator.
	No grid world simulation done. Taken as points.
	"""
	def init(laneNum, spawnRateSpec):
		"""
		Initialize lanes and spawning points
		"""
		lanes = [Lane(i, spawnRateSpec[i]) for i in range(0, laneNum)]

	def step(intv):
		"""
		One step of the simulator

		Usually called linearly, possibly called recursively (trying each possibility)
		"""
		for lane in lanes:
			lane.spawn(intv) # spawn according to the interval
			for v in lane:
				v.move()

	def log():
		"""
		Save necessary data to output
		"""
		print "log here."

	def main():
		"""
		Main function of the simulator
		"""
		init()
		policy = Policy.Optimal

		t = 0
		while t < MAX_TIME:
			# let policy modify reservation status
			policy.step()
			# let vehicles move
			step(intv)

		log()

if __name__ == "__main__":
	im = IntersectionManager()
	im.main()
