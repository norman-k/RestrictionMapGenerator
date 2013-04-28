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
for b in k:
  for a in k:
      if a + b == x:
        c.append(a)
        c.append(b)
        
def First_Map():
    return str(c[0:2])

def Plasmid_Generator():
 with open("Plasmid.html","w",) as web_page:
     web_page.write("<!doctype html>\n<html>\n<head>\n")
     web_page.write("<link rel='stylesheet' type='text/css' href='stylesheet.css' />")
     web_page.write("</head>\n<body>\n<p>\n")
     web_page.write("<div></div>")
     web_page.write(First_Map())
     web_page.write("</p>\n</body>\n</html>\n")
     
Plasmid_Generator()
