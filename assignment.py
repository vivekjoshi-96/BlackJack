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

def ass4(lot):
    output={}
    for project, role, emp in lot:
        prj_details = output.get(project, {})
        emp_list = prj_details.get(role, [])
        emp_list.append(emp)
        prj_details.update({role: emp_list})
        output[project] = prj_details

    print(output)

