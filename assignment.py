import random

listofstr= [
 'Hercules Soloway',
 'Tessa Aleksankov',
 'Darill Grafham',
 'Arney Crichton',
 'Barney Fullick',
 'Tate Lindmark',
 'Howey Tape',
 'Erastus Mixworthy',
 'Daniel Marchington',
 'Korney Scantleberry',
 'Stillman Barley',
 'Inger Kryszka',
 'Cam Sapson',
 'Jennica Renny',
 'Brannon Apdell',
 'Ashlie Gentzsch',
 'Cassey MacFadden',
 'Hercules Worner',
 'Marget Dusey',
 'Hadria Dumberrill',
 'Idaline Schlag',
 'Griffy Redding',
 'Bobby Grigorio',
 'Walliw Batten',
 'Boycey Grog',
 'Maryellen Figgess',
 'Rori Bartali',
 'Ysabel Rowbottom',
 'Aloysia Swetman',
 'Ashlen Croxton',
 'Costanza Hellwig',
 'Luciano Saiz',
 'Myca Habert',
 'Bernarr Geill',
 'Howey Jirzik',
 'Max Kobu',
 'Archy Feldheim',
 'Darby Hinstridge',
 'Sebastiano McCathy',
 'Howey Codling',
 'Shaun McNab',
 'Ambur Sigg',
 'Trefor MacCahey',
 'Luella Stratford',
 'Shirl Mulvaney',
 'Lindsay Bothen',
 'Hortensia Winspur',
 'Kev Licas',
 'Danielle Tooley',
 'Pearline Reeve',
 'Obie Collicott',
 'Marge Leser',
 'Annalee Bellis',
 'Sheppard De Giorgis',
 'Ines Romushkin',
 'Noble Wiskar',
 'Quentin McPhillimey',
 'Reinald Whales',
 'Lesli Schreurs',
 'Nerita Bonellie',
 'Christel McCawley',
 'Franzen Mart',
 'Luis Wharram',
 'Betty Barthropp',
 'Cairistiona Donalson',
 'Roanne Peat',
 'Masha Durbann',
 'Dela Gulleford',
 'Katharina McBrearty',
 'Joanie Rainville',
 'Rowland Scranney',
 'Orel Sher',
 'Ailyn Phillot',
 'Nertie Simoneton',
 'Mark Keiling',
 'Moishe Condit',
 'Luz Casini',
 'Madelaine Lightbourne',
 'Joelie Slayny',
 'Clemmie Stubbings',
 'Cheryl Maunder',
 'Normie Weddup',
 'Salomo Lippini',
 'Shauna McConville',
 'Cully Chimes',
 'Audrey Harwell',
 'Westbrook Aggis',
 'Verney Yockney',
 'Whitney Jaggi',
 'Consuelo Earp',
 'Patric Donativo',
 'Brigitta Blakemore',
 'Luis Roiz',
 'Aimil Vicioso',
 'Anderea Huguenet',
 'Paule Radmore',
 'Brok Schowenburg',
 'Vickie Clever',
 'Kay Kettow',
 'Netti Shepland'
]

lot=[('project_1', 'developer', 'employee_1'),
     ('project_1', 'developer', 'employee_4'),
     ('project_1', 'qa', 'employee_3'),
     ('project_2', 'developer', 'employee_6'),
     ('project_2', 'qa', 'employee_2'),
     ('project_3', 'developer', 'employee_5'),]




class Person:
  def __init__(self, name):
    self.name = name

def ass1(listofstr):
    dictList=[{'name': 'vivek', 'age': random.randint(10,100), 'weight': random.randint(1,100)}]
    for x in listofstr:
        y= random.randint(10,100)
        z= random.randint(10,100)
        dict={'name': x, 'age': y, 'weight':z}
        dictList.append(dict)
    print(dictList)

def ass2(listofstr):
    l1=[]
    max=len(listofstr)
    for x in range(max-1):
        fname = listofstr[x].split()[0]
        for y in range(x+1,max):
            fname1 = listofstr[y].split()[0]
            if fname==fname1 and fname not in l1:
                l1.append(fname)
    print(l1)

def ass3(listofstr):
    max=len(listofstr)
    l1=[]
    for x in range(max):
        splitname= listofstr[x].split()
        y=len(splitname)
        lname=splitname[y-1]
        if(lname[0] == 'A'):
            l1.append(lname)
    for x in l1:
        l2=[]
        print(x, '-')

        for y in range(len(x)):
            if x[y] not in l2:
                l2.append(x[y])
        print(l2)


def ass4():
    projects = []
    roles = []
    employees = []

    for x in lot:
        if x[0] not in projects:
            projects.append(x[0])
    for x in lot:
        if x[1] not in roles:
            roles.append(x[1])
    for x in lot:
        if x[2] not in employees:
            employees.append(x[2])

    for x in projects:
        for y in roles:
            for z in employees:
                for f in lot:
                    if f[0] = x and f[1] = y and f[2]= z:




