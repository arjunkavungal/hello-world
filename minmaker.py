print("127")
eggs = int(input("Qantes hueves hoi"))
vodque = int(input("Qantes vodques"))
no2 = int(input("Qantes bareles"))
pax = int(input("Qantes paxes"))
if (eggs < 4 or vodque < 2 or no2 < 3 or pax < 6):
  print('no min')
else:
  egg = eggs // 4
  vodques = vodque // 2
  no1 = no2 // 3
  pax = pax // 6
  n = [egg,vodques,no1,pax]
  print("You can make " + str(min(n)) + ' mins')
