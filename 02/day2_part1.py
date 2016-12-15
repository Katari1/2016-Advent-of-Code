contents = open("triangle.txt").read()
lines = contents.strip().split("\n")
count = 0
col_list = []

for l in lines:
    col_list.append(l.split())

for i in col_list:
    for z in range(len(i)):
        try:
            i[z] = int(i[z])
        except ValueError:
            pass
    i = sorted((i))
    print i
    if (i[0] + i[1]) > i[2]:
        count += 1
print "Total Number of Possible Triangles: ", count
