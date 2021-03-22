string = 'python'
print(string[0],string[2])


license_plate = "24가 2210"
print(license_plate[4:8])
print(license_plate[-4:])


string1 = "홀짝홀짝홀짝"
print(string1[::2])

string2 = "PYTHON"
print(string2[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
print(phone_number.replace("-",""))


url ="http://sharebook.kr"
url_split = url.split('.')
print(url_split[1])
