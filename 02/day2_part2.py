import sys
def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data


keypad = [['-','-','1','-','-'],['-','2','3','4','-'],['5','6','7','8','9',],['-','A','B','C','-'],['-','-','D','-','-']]
data = parse_input('day2.txt')
keypad = [['-', '-', '1', '-', '-'], ['-', '2', '3', '4', '-'], ['5', '6', '7', '8', '9', ],
              ['-', 'A', 'B', 'C', '-'], ['-', '-', 'D', '-', '-']]
a = 2
b = 0
location = keypad[a][b]
for instruction in data:
    for i in instruction:
        for z in range(len(i)):
            instruction = str(i[z])
            if instruction == 'U':
                if a > 0 and a <= 4 and b >= 0 and b <= 4:
                    if keypad[a-1][b] != '-':
                        a = a-1
                        location = keypad[a][b]
            elif instruction == 'L':
                if a >= 1 and a <= 4 and b > 0 and b <= 4:
                    if keypad[a][b-1] != '-':
                        b = b - 1
                        location = keypad[a][b]
            elif instruction == 'D':
                if a >=0 and a <= 3 and b >= 0 and b <= 4:
                    if keypad[a+1][b] != '-':
                        a += 1
                        location = keypad[a][b]
            elif instruction == 'R':
                if a >= 0 and a <= 4 and b >= 0 and b < 4:
                    if keypad[a][b+1] != '-':
                        b += 1
                        location = keypad[a][b]
            else:
                pass

        print location,
