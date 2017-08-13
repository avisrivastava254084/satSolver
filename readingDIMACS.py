import sys, copy
import pycosat

def readDMACS():
	global clauseFile, clauseFileLines, clauseSet
	clauseFile = open('days.txt', "r")
	clauseFileLines = clauseFile.readlines()
	clauseSet = list()
	clauseSet.append(list())
	maxvar = 0
	for line in clauseFileLines:
		tokens = line.split()
		if len(tokens) != 0 and tokens[0] not in ("p", "c"):
			for tok in tokens:
				lit = int(tok)
				maxvar = max(maxvar, abs(lit))
				if lit == 0:
					clauseSet.append(list())
				else:
					clauseSet[-1].append(lit)
	assert len(clauseSet[-1]) == 0
	clauseSet.pop()
	print(clauseSet)
	print(maxvar)

if __name__ == "__main__":
	print "Welcome!"
	readDMACS()
	print "The clause set after calling the parser function is:"
	print clauseSet
	print "This is the solution"
	for sol in pycosat.itersolve(clauseSet):
		print sol