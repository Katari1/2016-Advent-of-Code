import md5

num = 0
code=[None] * 8
while None in code:
    input="ffykfhsq"
    input = input + str(num)
    md = md5.new()
    md.update(input)
    a = md.hexdigest()
    if a[:5] == '00000':
        try:
            position = int(a[5])
        except ValueError:
            position = int(100)
        number = a[6]
        try:
            if not code[position]:
                code[position] = number
        except IndexError:
            pass

        print code
        num +=1
    else:
        num += 1

print code