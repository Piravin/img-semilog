sr = ""
for i in range(1,7):
	st = "torqeq(" + str(i) +")*(rpm^"+str(7-i)+")+"
	sr = sr+st
print(sr)