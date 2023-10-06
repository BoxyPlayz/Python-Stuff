import time

num = float(input('Initial value (To double):'))
typeadd = float(input('Multiplier:'))
i = 0

if ((typeadd == 'x') or (typeadd == '*')):
    t = "*"

while(True):
    i += 1
    num = (num + num) * typeadd
    time.sleep(0.05)
    print(str(i) + ": " + str(num))
    if(str(num) == "inf"):
        break