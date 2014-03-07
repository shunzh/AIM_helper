#!/usr/bin/env python

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

	t = 0
	while t < MAX_TIME:
		step()

	log()

if __name__ == "__main__":
	main()
