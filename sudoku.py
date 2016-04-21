
from copy import deepcopy

readfile = open('puzzles.txt', 'r')

couldntsolve = 0

for puzzle in readfile:

	allpossible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	grid = []
	counter = 0

	unsolved = 9*9

	for i in range(9):
		newlist = []
		# newlist = deepcopy(allpossible)
		grid.append(newlist)
		for j in range(9):
			newlist2 = deepcopy(allpossible)
			if (puzzle[counter] != '0'):
				newlist2 = [int(puzzle[counter])]
				unsolved = unsolved - 1
			# newlist2 = [counter]
			counter = counter + 1
			grid[i].append(newlist2)

	# print grid
	# print 'Unsolved: ' + str(unsolved)

	def clearRow(number, row, unsolved):
		changed = 0
		myrow = grid[row]
		for x in myrow:
			if (number in x and len(x) > 1):
				x.remove(number)
				changed = changed + 1
				if (len(x) == 1):
					unsolved = unsolved - 1
				# print x
		return [unsolved, changed]

	def clearCol(number, col, unsolved):
		changed = 0
		mycol = []
		for i in range(9):
			mycol.append(grid[i][col])
		# mycol = grid[0][col]
		for y in mycol:
			if (number in y and len(y) > 1):
				y.remove(number)
				changed = changed + 1
				if (len(y) == 1):
					unsolved = unsolved - 1
				# print y
		return [unsolved, changed]

	while unsolved > 0:
		prevunsolved = deepcopy(unsolved)
		changed = 0
		# print 'Unsolved: ' + str(unsolved)
		for i in range(9):
			for j in range(9):
				currentNum = grid[i][j]
				if (len(currentNum) == 1):
					[unsolved, changed1] = clearRow(currentNum[0], i, unsolved)
					changed = changed + changed1
					# print changed1
					[unsolved, changed2] = clearCol(currentNum[0], j, unsolved)
					changed = changed + changed2
					# print changed2
		# if (unsolved == prevunsolved):
		if (changed == 0):
			if (unsolved > 0):
				couldntsolve = couldntsolve + 1
				# print 'Algorithm finished, cannot solve further'
				# print 'Unsolved: ' + str(unsolved)
			break

	# if (unsolved == 0):
	# 	print 'Congratulations! The puzzle has been solved.'

	# for row in grid:
	# 	print row

print 'Couldn\'t solve ' + str(couldntsolve) + ' puzzles.'