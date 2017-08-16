from bs4 import BeautifulSoup
import urllib2
import csv 
import urlparse

html = []
urls = []#empty list where I will store the relevant link endings
pet_urls = [] #empty list that will largely include only the petitions

x = ["0", "1", "2"] #number of pages
pages = [] #create urls per page
for a in x:
    pages.append(urlparse.urljoin('https://petitions.whitehouse.gov/', "?page=" + a))

for y in pages:#do it for each page
    #Get address, open url
    web_page = urllib2.urlopen(y)

    # Parse it
    soup = BeautifulSoup(web_page.read())
    soup.prettify()	

    # Find all cases of a certain tag
    soup.find_all('a')

    list_faculty = soup.find_all('a',{'span class':"element-invisible" })

    my_a_tag=soup.find_all('a')[-17]

    for link in soup.findAll('a', href = True):#find all links and store them in a list called htlm
        html.append(link['href'])

    import re
    for i in range(0, len(html)):
        urls.append(re.findall(r'/petition/[\'"]?([^\'" >]+)', html[i]))#find all links in html that follow the desired pattern

    for i in range(0, len(urls)):#remove repeated url endings
        if urls[i] in pet_urls:
            pass
        else:
            pet_urls.append(urls[i])

baseurl = "https://petitions.whitehouse.gov/petition/"
list_links = [] #create list of petition links by joining base url + url endings
for i in range(2, len(pet_urls)):
    list_links.append(urlparse.urljoin(baseurl, pet_urls[i][0]))


list_titles = []
list_dates = []
list_sign = []
list_fields = []
for i in range(0, len(list_links)-1):
    #Get address, open url
    web_address=list_links[i]
    web_page = urllib2.urlopen(web_address)

    # Parse it
    soup = BeautifulSoup(web_page.read())
    soup.prettify()	

    # Find case of a h1 tag, its text contains the titles of the petitions
    list_titles.append(soup.find('h1').text)

    # Find first case of a h4 tag with a class petition attribution, its text contains the dates of the petitions
    list_dates.append(soup.find_all('h4', {"class":"petition-attribution"})[0].text)

    # Find first case of a div tag with a class signatures text container, its text contains the number of signatures, also removes unnecessary stuff at the end
    list_sign.append(soup.find('div', {"class":"signatures-text-container"}).text.rstrip("\nsigned"))
    
    #Find issues, which are the text in the second element in the list from soup. 
    #To make the output nicer, I add " and " between issues
    if len(soup.find_all('div', {"class":"field-items"})[1].contents) == 1:
        list_fields.append(soup.find_all('div', {"class":"field-items"})[1].contents[0].text)

    elif len(soup.find_all('div', {"class":"field-items"})[1].contents) == 2:
        a = soup.find_all('div', {"class":"field-items"})[1].contents[0].text
        b = soup.find_all('div', {"class":"field-items"})[1].contents[1].text
        list_fields.append(a + " and " + b)
    
    else:
        a = soup.find_all('div', {"class":"field-items"})[1].contents[0].text
        b = soup.find_all('div', {"class":"field-items"})[1].contents[1].text
        c = soup.find_all('div', {"class":"field-items"})[1].contents[2].text
        list_fields.append(a + " and " + b + " and " + c)

#Clean some things
list_dates2=[]
for i in range(0, len(list_dates)-1):
    list_dates2.append(list_dates[i].split("on")[1].strip())

#Solve issues with unicode
list_titles = [x.encode('UTF8') for x in list_titles]
list_dates2 = [x.encode('UTF8') for x in list_dates2]
list_sign = [x.encode('UTF8') for x in list_sign]
list_fields = [x.encode('UTF8') for x in list_fields]

with open('petitions_info.csv', 'wb') as f:
    my_writer = csv.DictWriter(f, fieldnames=("Title", "Date", "Signatures", "Fields"))
    my_writer.writeheader()
    for i in range(0, len(list_titles)-1):
        my_writer.writerow({"Title" :list_titles[i], "Date":list_dates2[i], "Signatures":list_sign[i], "Fields":list_fields[i]})



