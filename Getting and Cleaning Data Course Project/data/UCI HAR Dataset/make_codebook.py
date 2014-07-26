a = (1,2,3,4,5,6,41,42,43,44,45,46,81,82,83,84,85,86,121,122,123,124,125,126,161,162,163,164,165,166,201,202,214,215,227,228,240,241,253,254,266,267,268,269,270,271,345,346,347,348,349,350,424,425,426,427,428,429,503,504,516,517,529,530,542,543)
a = set(a)

filehandle = open("features.txt", 'r')
output = open("Codebook.txt", 'w')
count = 0
rownumber = 3 

output.write("1 Subject\n2 Activity\n")


for line in filehandle:
	count += 1
	if count in a:
		parts = line.split(" ")
		new_line = str(rownumber) + " " + str(parts[1])
		rownumber += 1
		output.write(new_line)
	else:
		b = 'do nothing'

