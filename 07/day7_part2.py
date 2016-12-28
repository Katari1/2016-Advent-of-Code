import re
def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data
def parse_data(list):
    for i in list:
        strings=[]
        var = str(i)
        hypernet = re.findall(r"\[(\w+)\]", var)
        string = re.findall(r"\](\w+)?|(\w+)\[", var)
        for i in string:
            for z in range(len(i)):
                if i[z] != '':
                    strings.append(i[z])
        return hypernet, strings
def pull_aba(string):
    aba=[]
    for i in range(len(string)):
        try:
            if (string[i] == string[i+2]) and (string[i+1] != string[i]) and (string[i] != '|' and string[i+1] != '|'):
                aba.append(string[i:(i+3)])
        except IndexError:
            pass
    return aba
def check_bab(aba):
    bab = aba[1]+aba[0]+aba[1]
    return bab
def converttostring(list):
    your_mom = ""
    for i in list:
        your_mom+=str(i) +'|'
    return your_mom


data=parse_input('day7.txt')
count = 0
for i in data:
    hypernet,supernet = parse_data(i)
    supernet_string = converttostring(supernet)
    hypernet_string = converttostring(hypernet)
    aba = pull_aba(supernet_string)
    for z in aba:
        z = str(z)
        a = check_bab(z)
        if a in hypernet_string:
            count +=1
            break
print "Total IPs supporting SSL: ", count

