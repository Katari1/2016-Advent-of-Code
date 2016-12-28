def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split(",")
    for l in lines:
        data.append(l.split())
    return data



directions = parse_input('day1.txt')
#Starting North
pos = 'N'
north=0
south=0
east=0
west=0
for i in directions:
    dest = str(i[0][0])
    dist = int(i[0][1:])
    if pos == 'N' and dest =='R':
        pos = 'E'
        east += dist
    elif pos == 'N' and dest =='L':
        pos = 'W'
        west += dist
    elif pos == 'E' and dest == 'R':
        pos = 'S'
        south += dist
    elif pos == 'E' and dest == 'L':
        pos = 'N'
        north += dist
    elif pos == 'S' and dest == 'R':
        pos = 'W'
        west += dist
    elif pos == 'S' and dest == 'L':
        pos = 'E'
        east += dist
    elif pos == 'W' and dest == 'R':
        pos = 'N'
        north += dist
    elif pos == 'W' and dest == 'L':
        pos = 'S'
        south += dist

total_distance = abs((north - south) + (east - west))
print "Total Distance: ", total_distance
