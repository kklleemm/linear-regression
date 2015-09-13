# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_linear_regression.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cdeniau <cdeniau@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/09/13 18:17:05 by cdeniau           #+#    #+#              #
#    Updated: 2015/09/13 19:25:47 by cdeniau          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python

import sys

if len(sys.argv) < 2:
	print 'Usage : python ft_linear_regression.py #mileage'
else:
	mileage = input ('Car mileage : ')
	int theta0 = 0
	int theta1 = 0
	theta0 = execfile("ft_learn.py theta0")
	theta1 = execfile("ft_learn.py theta1")
	print ('Estimated value for this car : ', theta0 + theta1 * mileage)
