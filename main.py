#!/usr/bin/env python
import intersection, policy

"""
Main file for intersection simulator.
No grid world simulation done. Taken as points.
"""

def init(laneNum, spawnRateSpec = None):
	"""
	Initialize lanes and spawning points
	"""

def step():
	"""
	One step of the simulator

	Usually called linearly, possibly called recursively (trying each possibility)
	"""

def log():
	"""
	Save necessary data to output
	"""

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
		step()

	log()

if __name__ == "__main__":
	main()
