import re
def parse_input(location):
    data=[]
    content = open(location).read()
    lines = content.strip().split("\n")
    for l in lines:
        data.append(l.split())
    return data

def get_data(list):
    for i in list:
        var = str(i)
        digits = ""
        encrypted_name = ""
        encrypted_name = re.search(r'([^[0-9]+)', var)
        checksum = re.search(r"\[(\w+)\]", var)
        digits = re.search(r'([0-9]+)', var)

        checksum = checksum.group(1)
        encrypted_name = encrypted_name.group(1)
        digits = int(digits.group(1))
        return encrypted_name,digits,checksum

def sorted_encrypted_name(en):
    counter={}
    chars = set(en)
    for i in chars:
        if i == '-':
            pass
        else:
            counter[i] = en.count(i)
    sorted_counter = [v[0] for v in sorted(counter.iteritems(), key=lambda (k, v): (-v, k))]
    return sorted_counter

def is_match(checksum,en):
    your_mom = ""
    for i in xrange(0,5):
        your_mom = your_mom + en[i]
    if checksum == your_mom:
        return True
    else:
        return False

raw_data = parse_input('day4.txt')
total = 0
for i in raw_data:
    en,digits,checksum = get_data(i)
    name = sorted_encrypted_name(en)
    if is_match(checksum,name):
        total += digits
    else:
        pass

print "Total Checksum: ", total
