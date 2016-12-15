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
        #checksum = re.search(r"\[(\w+)\]", var)
        digits = re.search(r'([0-9]+)', var)

        #checksum = checksum.group(1)
        encrypted_name = encrypted_name.group(1)
        digits = int(digits.group(1))
        return encrypted_name,digits
def decrypt_letter(encrypted_name,modifier):
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    index = alphabet.index(encrypted_name)
    encrypted_letter = (index + modifier)
    if encrypted_letter >= len(alphabet):
        encrypted_letter = (encrypted_letter % len(alphabet))
    return alphabet[encrypted_letter]




raw_data = parse_input('day4.txt')
for i in raw_data:
    name=""
    en,digits = get_data(i)
    for z in en:
        if z == '-':
            name += " "
        else:
            name += decrypt_letter(z,digits)
    print name," ", digits

