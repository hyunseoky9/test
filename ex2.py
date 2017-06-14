import sys
dmNet=sys.argv[1]
handle=open(dmNet)

pairs=[]
unique=[]
for lines in handle:
	data=lines.strip().split('\t\t\t')
	pair=(data[0],data[1])
	pairs.append(pair)
	unique+=[data[0],data[1]]

handle.close()
unique=set(unique)
unique=list(unique)
cs=[]
for gene in unique:
	k=0
	N=[]
	for pair in pairs:
		if gene in list(pair) and pair[0]!=pair[1]:
			k+=1
			if pair[0]==gene:
				N.append(pair[1])
			else:
				N.append(pair[0])

	e=0
	for i in range(0,len(N)):
		for j in range(i,len(N)):
			if (N[i],N[j]) in pairs or (N[j],N[i]) in pairs:
				e+=1
	if k>1:
		c=float(2*e)/(k*(k-1))
		cs.append(c)
	else:
		cs.append(0)

Cbar=1/float(len(cs))*sum(cs)

print round(Cbar,6)








