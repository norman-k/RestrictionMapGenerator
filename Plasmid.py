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
for b in h[0]:
  for a in h[0]:
      if a + b == x:
        c.append(a)
        c.append(b)
for l in h[0]:
    for q in h[0]:
        if l + q == y:
          d.append(l)
          d.append(q)
c.append(k[2:])
try:
  for r in h[1]:
    for e in h[1]:
        if r + e == max(g[0]):
            c.append(r)
            c.append(e)
except:
  print "no other enzyme used"
def First_Map_Slice():
    f = x - max(g[0])
    s = max(g[0])
    m = []
    m.append(f)
    m.append(s)
    return str(m)
def First_Map_Finish():
    if y == 0:
       return str(k[1:])
def Second_Map_Slice():
    return c
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
     web_page.write("Then on the other: \n")
     web_page.write(Second_Map_Slice())
     web_page.write("</p>\n</body>\n</html>\n")
     
Plasmid_Generator()
