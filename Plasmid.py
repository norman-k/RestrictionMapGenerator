x = input("Please enter the length of the vector in kb for the initial restriction enzyme: ")
y = input("Please enter the length of the insert in kb[Enter 0 if there is none]: ")
z = input("How many more enzymes are there?: ")
h = []
j = 1
while j <= z:
    k = input("Enter the size in kb of each fragment, denote a ',' for each one: ")
    j += 1
    g = []
    g.append(k)
    h.append(g)
c = []
d = []
for b in k:
  for a in k:
      if a + b == x:
        c.append(a)
        c.append(b)
for l in k:
    for q in k:
        if l + q == y:
          d.append(l)
          d.append(q)
c.append(k[2:])        
def First_Map_Slice():
    f = x - max(k)
    s = max(k)
    m = []
    m.append(f)
    m.append(s)
    return str(m)
def First_Map_Finish():
    if y == 0:
       return str(k[1:])
def Plasmid_Generator():
 with open("Plasmid.html","w",) as web_page:
     web_page.write("<!doctype html>\n<html>\n<head>\n")
     web_page.write("<link rel='stylesheet' type='text/css' href='stylesheet.css' />")
     web_page.write("</head>\n<body>\n<p>\n")
     web_page.write("<div></div>")
     web_page.write("First, slice it into\n")
     web_page.write(First_Map_Slice())
     web_page.write("Then on one side, slice it into: \n")
     web_page.write(First_Map_Finish())
     web_page.write("</p>\n</body>\n</html>\n")
     
Plasmid_Generator()
