import csv

reader = csv.reader(open("EPL-15-16.csv", "rb"), delimiter=",")

f = csv.writer(open("MUFC-15-16.csv", "wb"))
for line in reader:
	if "Man United" in line:
		f.writerow(line)
		print(line)
