a1 = int(input("podaj a1"))
a2 = int(input("podaj a2 - ma być większy od a1"))
b1 = int(input("podaj b1"))
b2 = int(input("podaj b2 - ma być większy od b1"))
c = "nie"
if (a2 < b1 or a1 > b2):
    c = "nie"
elif (a2 > b1 and a2 < b2) or (a1 > b1 and a1 < b2) or (b2 > a1 and b2 < a2) or (b1 > a1 and b1 < a2):
    c = "tak"
print(c)

#długość części wspólnej
cwspól = 0
if c == "tak":
    if (a2 > b1 and a2 < b2):
        cwspól = (a2-b1)
    if (a1 > b1 and a1 < b2):
        cwspól = (a1-b2)
    if (b2 > a1 and b2 < a2):
        cwspól = (b2-a1)
    if (b1 > a1 and b1 < a2):
        cwspól = (b1-a2)
    if (a1 < b1 and b2 < a2):
        cwspól = (b2 - b1)
    if (b1 <  a1 and a2 < b2):
        cwspól = (a2 - a1)
print(cwspól)

