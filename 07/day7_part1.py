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
def converttostring(list):
    your_mom = ""
    for i in list:
        your_mom+=str(i) +'|'
    return your_mom
def check_abba(string):
    for i in range(len(string)):
        try:
            if (string[i] == string[i+3]) and (string[i+1] == string[i+2]) and string[i] != string[i+1]:
                return True
        except IndexError:
            pass


count = 0
data = parse_input('day7.txt')
for i in data:
    your_mom =""
    hypernet, string = parse_data(i)
    string_hypernet = converttostring(hypernet)
    string_combined = converttostring(string)
    if check_abba(string_combined) and not check_abba(string_hypernet):
         print i
print "Total IPs Supporting TLS: ", count
