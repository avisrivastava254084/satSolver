clauseFile = open('days.txt', "r")
cluaseFileLines = clauseFile.readlines()
cnf = list()
cnf.append(list())
maxvar = 0

for line in cluaseFileLines:
    tokens = line.split()
    if len(tokens) != 0 and tokens[0] not in ("p", "c"):
        for tok in tokens:
            lit = int(tok)
            maxvar = max(maxvar, abs(lit))
            if lit == 0:
                cnf.append(list())
            else:
                cnf[-1].append(lit)

assert len(cnf[-1]) == 0
cnf.pop()

print(cnf)
print(maxvar)