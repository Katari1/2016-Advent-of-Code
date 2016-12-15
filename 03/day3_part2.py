def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data
def create_colums(list):
    column1 = []
    column2 = []
    column3 = []
    column1_new = []
    column2_new = []
    column3_new = []
    for i in list:
        column1.append(i[0])
        column2.append(i[1])
        column3.append(i[2])

    maxt = len(column1) - 2
    #for i in range(len(column1[:maxt])):
    for i in xrange(0,maxt,3):
        column1_new.append(column1[i:(i + 3)])
        column2_new.append(column2[i:(i + 3)])
        column3_new.append(column3[i:(i + 3)])
    return column1_new,column2_new,column3_new

def get_triangles(list):
    count = 0
    for i in list:
        a = i[0]
        b = i[1]
        c = i[2]
        if len(a) >= 3 and len(b) >= 3 and len(c) >= 3:
            a = a[-3]
            b = b[-3]
            c = c[-3]
            if a == b == c:
                count += 1
    print "Total Good Triangles in Column: ", count
    return count

def try_again(list):
    count = 0
    for i in list:
        for z in range(len(i)):
            try:
                i[z] = int(i[z])
            except ValueError:
                pass
        i = sorted((i))
        if (i[0] + i[1]) > i[2]:
            count += 1
    return count


awesome = parse_input('triangle.txt')
column1_new,column2_new,column3_new = create_colums(awesome)

#print column1_new
a = try_again(column1_new)
b = try_again(column2_new)
c = try_again(column3_new)
print a+b+c