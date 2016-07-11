import os
import numpy as np

def tree(root):
	#st=' '*(len(string)/2)
	print root
	try:
		for i in os.listdir(root):
			if i.startswith(".") or i in ignored:
				continue
			p=root+"/"+i
			database.append(p)
			if os.path.isfile(p):
				continue
			elif os.path.isdir(p) and p not in ignored:
				paths.append(p)

	except:
		print "permission denied for",root

paths=np.load("addDirectories.npy").tolist()
ignored=np.load("ignoreDirectories.npy").tolist()
print paths
print ignored
database=[]
locations=[]
while len(paths) > 0:
	#tree("____",path)
	path=paths.pop()
	tree(path)
print database
np.save("database.npy",database)

