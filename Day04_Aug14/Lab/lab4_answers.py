#Go to https://polisci.wustl.edu/faculty/specialization
#Go to the page for each of the professors.
#Create a .csv file with the following information for each professor:
# 	-Specialization
# 	-Name
# 	-Title
# 	-E-mail
# 	-Web page
	
from bs4 import BeautifulSoup
import urllib2
import csv 

web_address='https://polisci.wustl.edu/faculty/specialization'
web_page = urllib2.urlopen(web_address)
			
# Parse it
soup = BeautifulSoup(web_page.read())
soup.prettify()				

# Find all cases of a certain tag
soup.find_all('a')
				
# Get the attributes
my_a_tag=soup.find_all('a')[15]
my_a_tag.attrs #Gives a dictionary with the attributes
my_a_tag.attrs.keys()
my_a_tag['href']

# Refine search by using attributes
list_faculty = soup.find_all('a',{'class':"person-view-primary-field" })

faculty_names = []   

for i in range(0, len(list_faculty)):
    faculty_names.append(list_faculty[i].text)

faculty_websites = []   

for i in range(0, len(list_faculty)):
    faculty_websites.append(list_faculty[i]['href'])

mysection=soup.find_all('div',{'class':"view-content"})
list_all = mysection[0].contents

listit = []
for i in range(0, len(list_all)-1):
    try:
        listit.append(list_all[i].get_text())
    except:
        pass

newlist = [i.split("\n") for i in listit]

newlist = [[x.strip() for x in y] for y in newlist]

list_titles = []
for i in range(0,len(newlist)):
    try:
        list_titles.append(newlist[i][2])
    except:
        pass

Am = newlist[0]
Cm = newlist[12]
FT = newlist[26]
IR = newlist[32]
IPE = newlist[35]
M = newlist[38]
PT = newlist[43]
AL = newlist[len(newlist)-1]

list_specialization = []

for i in range(0,newlist.index(Cm)-1):
    try:
        list_specialization.append("American")
    except:
        pass

for i in range(newlist.index(Cm),newlist.index(FT)-1):
    try:
        list_specialization.append("Comparative")
    except:
        pass

for i in range(newlist.index(FT),newlist.index(IR)-1):
    try:
        list_specialization.append("Formal Theory")
    except:
        pass
    
for i in range(newlist.index(IR),newlist.index(IPE)-1):
    try:
        list_specialization.append("International Relations")
    except:
        pass

for i in range(newlist.index(IPE),newlist.index(M)-1):
    try:
        list_specialization.append("International Political Economy")
    except:
        pass

for i in range(newlist.index(M),newlist.index(PT)-1):
    try:
        list_specialization.append("Methodology")
    except:
        pass

for i in range(newlist.index(PT),newlist.index(AL)):
    try:
        list_specialization.append("Political Theory")
    except:
        pass

len(newlist)
len(list_specialization)
len(faculty_names)
len(list_titles)
len(faculty_websites)

url_page = "https://polisci.wustl.edu/faculty"
listpages = []
for name in faculty_websites:
    try:
        listpages.append(url_page + str(name))
    except Exception:
        pass

listpages = [w.replace('faculty/faculty/', 'faculty/') for w in listpages]
listpages.remove(listpages[16])
listpages.remove(listpages[-10])
listpages1 = [w.replace('faculty/', '') for w in listpages]

from urllib2 import HTTPError

faculty_emails = []
for i in range(0, len(listpages)):
    try:
        html_page = urllib2.urlopen(listpages[i])
        soup = BeautifulSoup(html_page)
        faculty_emails.append(soup.findAll('a', attrs={'href': re.compile("^mailto:")})[0].text)
    except urllib2.HTTPError:
        html_page = urllib2.urlopen(listpages1[i])
        soup = BeautifulSoup(html_page)
        faculty_emails.append(soup.findAll('a', attrs={'href': re.compile("^mailto:")})[0].text)
    except Exception:
        faculty_emails.append("NA")

faculty_emails.insert(15, "mgabel@wustl.edu")
faculty_emails.insert(-9, "mgabel@wustl.edu")

print faculty_emails



# Refine search by using attributes

#How about with field names
with open('faculty_info.csv', 'wb') as f:
  my_writer = csv.DictWriter(f, fieldnames=("Specialization", "Name", "Title", "Email", "Web Page"))
  my_writer.writeheader()
  for i in range(0, len(list_faculty)-1):
    my_writer.writerow({"Specialization" , "Name", "Title", "Email", "Web Page"})

with open('faculty_info.csv', 'wb') as f:
    my_writer = csv.DictWriter(f, fieldnames=("Names", "Title", "Specialization", "Web Page", "Email"))
    my_writer.writeheader()
    for i in range(0, len(faculty_names)-1):
        my_writer.writerow({"Names" :faculty_names[i], "Title":list_titles[i], "Specialization":list_specialization[i], "Web Page":faculty_websites[i], "Email":faculty_emails[i]})


