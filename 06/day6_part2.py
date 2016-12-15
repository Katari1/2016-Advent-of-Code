def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data

def create_list(list):
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    column7 = []
    column8 = []

    for i in list:
        for z in i:
            column1.append(z[0])
            column2.append(z[1])
            column3.append(z[2])
            column4.append(z[3])
            column5.append(z[4])
            column6.append(z[5])
            column7.append(z[6])
            column8.append(z[7])
    return column1, column2, column3, column4, column5, column6, column7, column8

def least_used_letter(list):
    column1=[]
    counter={}
    for i in list:
        for z in i:
            column1.append(z[0])
    uniq = set(column1)
    for i in uniq:
        counter[i] = column1.count(i)
        #sorted_counter = [v[0] for v in sorted(counter.iteritems(), key=lambda (k, v): (-v, k))]
        sorted_counter = [v[0] for v in sorted(counter.iteritems(), key=lambda (v, k): (k, v))]
    return sorted_counter[0]



data = parse_input('day6.txt')
column1, column2, column3, column4, column5, column6, column7, column8 = create_list(data)
print least_used_letter(column1)
print least_used_letter(column2)
print least_used_letter(column3)
print least_used_letter(column4)
print least_used_letter(column5)
print least_used_letter(column6)
print least_used_letter(column7)
print least_used_letter(column8)

#a = most_used_letter(data)
#print a[0]