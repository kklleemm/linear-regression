# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_learn.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdeniau <cdeniau@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/09/13 19:01:46 by cdeniau           #+#    #+#              #
#    Updated: 2015/09/13 19:24:44 by cdeniau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python

import sys

# create file
def writeFile(filename,text):
	file = open(filename, "w")
	file.write(text)
	file.close()

def readFile(filename):
        file = open(filename,"r")
        line = file.readline()
        line = line.strip()
        print line
        #return line
        file.close()

def getTheta0():

def getTheta1():

if sys.argv == "theta0":
	return getTheta0()
if sys.argv == "theta1":
	return getTheta1()
if sys.argv == "w":
	writeFile("dataset.txt","contenu")
elif sys.argv == "r":
	readFile("dataset.txt")
