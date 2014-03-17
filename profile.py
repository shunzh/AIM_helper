#!/usr/bin/env python

class Profile:
	pass


class SimpleProfile:
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
