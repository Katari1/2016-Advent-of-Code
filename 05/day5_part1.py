import md5
count = 0
num = 0
while count <= 7:
    input="ffykfhsq"
    input = input + str(num)
    md = md5.new()
    md.update(input)
    a = md.hexdigest()
    if a[:5] == '00000':
        print a[5]
        count += 1
        num +=1
    else:
        num += 1