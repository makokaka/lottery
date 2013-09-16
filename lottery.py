#coding=utf8
"""
This script is written for fun!
Auto generate lottery category & buy numbers
"""

import sys
from random import seed, random, sample

class BaseLottery(object):
	def __init__(self, category=None):
		self.category = category

	def cathectic(self):
		pass

	def output(self):
		print 'BaseLottery output'

class DoubleColorBall(BaseLottery):
	def __init__(self, category='DoubleColorBall'):
		BaseLottery.__init__(self)

		self.red_balls = []
		self.blue_ball = []

		self.candidate_red_balls = ['%2d' % e for e in range(1, 34)]
		self.candidate_blue_balls = ['%2d' % e for e in range(1, 17)]

		self.min_red_ball_num  = 6
		self.min_blue_ball_num = 1

	def cathectic(self):
		self.red_balls = sorted(sample(self.candidate_red_balls, self.min_red_ball_num))
		self.blue_ball = sample(self.candidate_blue_balls, self.min_blue_ball_num)

	def output(self):
		print 'Red Balls: ', ','.join((str(e) for e in self.red_balls))
		print 'Blue Ball: ', self.blue_ball[0]

if __name__ == '__main__':
	obj = DoubleColorBall()
	obj.cathectic()
	obj.output()