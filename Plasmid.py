import os
import csv

with open("Data.csv","r") as database:
    read_file = csv.reader(open("Data.csv", "rb"), skipinitialspace=True)
    data = str(database.readlines()).strip().split('\\n')
    data = [x.split(",") for x in data]
    name = []        
    index = 2
    vector = []
    insert = []
    vector.append(int(data[1][3]))
    vector_length = sum(vector)
    if data[1][4] != '':
        insert.append(int(data[1][4]))
        if data[1][5] != '':
            insert.append(int(data[1][5]))    
    insert_length = sum(insert)    
    if data[3][2] != '':
        enzyme_count = 2
    else:
        enzyme_count = 1
fragment_list = []
count_all = 1
while count_all <= enzyme_count:
    fragment_size = [int(data[index][3]),int(data[index][4]),int(data[index][5]),int(data[index][6])]
    count_all += 1
    index += 1
    fragment_carrier = []
    fragment_carrier.append(fragment_size)
    fragment_list.append(fragment_carrier)
vector_fragments = []
insert_fragments = []
initial_fragments = fragment_list[0]
try: 
  second_fragments = fragment_list[1]
except:
  print "calculating"
for fragment_one in fragment_list[0]:
  for fragment_two in fragment_list[0]:
      if fragment_one + fragment_two == vector_length:
        vector_fragments.append(fragment_one)
        vector_fragments.append(fragment_two)
for insert_one in fragment_list[0]:
    for insert_two in fragment_list[0]:
        if insert_one + insert_two == insert_length:
          insert_fragments.append(insert_one)
          insert_fragments.append(insert_two)
vector_fragments.append(fragment_size[2:])

def First_Map_Slice():
    gap_left = vector_length - max(initial_fragments[0])
    initial_slice = max(initial_fragments[0])
    first_map = []
    first_map.append(gap_left)
    first_map.append(initial_slice)
    return str(first_map)
def First_Map_Finish():
    if insert_length == 0:
       return str(fragment_size[1:])
def Second_Map_Slice():
    if len(fragment_size) == 4:
      return str(vector_fragments[(len(vector_fragments) - 2):len(vector_fragments)])
    else:
       return str(vector_fragments[len(vector_fragments) - 1])
def Plasmid_Generator():
 with open("Plasmid.html","w",) as web_page:
     web_page.write("<!doctype html>\n<html>\n<head>\n")
     web_page.write("<link rel='stylesheet' type='text/css' href='stylesheet.css' />\n")
     web_page.write("</head>\n<body>\n<p>\n")
     web_page.write("<div></div>")
     web_page.write("First, slice it into\n")
     web_page.write(First_Map_Slice())
     web_page.write("Then on one side, slice it into: \n")
     web_page.write(First_Map_Finish())
     if enzyme_count > 1:
         web_page.write("Then on the other: \n")
         web_page.write(Second_Map_Slice())
     web_page.write("</p>\n</body>\n</html>\n")
     
Plasmid_Generator()

try:
    os.startfile("Plasmid.html")
except:
    print "Open 'Plasmid.html'"
