from openpyxl import load_workbook
from PlayerClass import Player

field = []

wb = load_workbook("practice.xlsx", read_only=True, data_only=True)
ws = wb.active

for row in ws:
    name = str(row[0].value) + " " + str(row[1].value)
    division = str(row[2].value)
    hometown = str(row[3].value)
    school = str(row[4].value)
    anniversary = str(row[5].value).lower() in ['yes']
    sande = str(row[6].value).lower() in ['yes']
    cit = str(row[7].value).lower() in ['yes']
    se1 = str(row[8].value).lower() in ['military']
    se2 = str(row[9].value).lower() in ['geography']
    bowl = str(row[11].value).lower() in ['yes']
    seed = str(row[12].value).lower()
    newplayer = Player(name, division, hometown, school, anniversary, sande, cit, se1, se2, bowl, seed)
    field.append(newplayer)

wb.close()

field.pop(0)
for players in field:
    print players.getinfo()
