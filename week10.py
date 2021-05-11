#실습 문제 2번
num = [int(x) for x in input("Number? " ).split()]

max = num[0]
for i in range(1, len(num)):
    if max < num[i]:
        max = num[i]
print(max)


#실습 문제 3번
sec1, sec2 = input("암호화 : ").split()
sec11=""
sec22=""

for i in sec1:
    s = ord(i)
    s = s + 1 
    ii = chr(s)
    sec11 = sec11 + ii
for i in sec2:
    s = ord(i)
    s = s + 1 
    ii = chr(s)
    sec22 = sec22 + ii
print(sec22, sec11)


orgn1, orgn2 = input("복호화 : ").split()
orgn11=""
orgn22=""

for i in orgn1:
    s = ord(i)
    s = s - 1 
    ii = chr(s)
    orgn11 = orgn11 + ii
for i in orgn2:
    s = ord(i)
    s = s - 1 
    ii = chr(s)
    orgn22 = orgn22 + ii
print(orgn22, orgn11)


#실습 문제 4번
phonebook = {}

for i in range(10) :
  key = input('이름 입력 : ')
  value = input('전화번호 입력 : ')
  phonebook[key] = value
  i += 1

name = input("이름 : ")
x = phonebook[name]
print(x)

number = input("전화번호 : ")
for key, value in phonebook.items():
  if value == number:
    print(key)
