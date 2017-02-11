import dryscrape
from bs4 import BeautifulSoup
import webbrowser
name=input('Enter name : ')
file_name=name+'.txt'
fw=open(file_name,'r')
st=str(fw.read())
fw.close()
firstHref=st
print('first href is '+firstHref)
url_name=''
if(name=='Ankit_singh'):
    url_name='akt_rabbit'
else:
    url_name='abisbaba1'
url='https://www.hackerearth.com/submissions/'+url_name+'/'
ses=dryscrape.Session()
ses.visit(url)
r=ses.body()
soup=BeautifulSoup(r,'html.parser')
link = soup.find_all('a' , class_='no-color hover-link')
l=0;
for x in link:
    if(firstHref.find(x['href'])!=-1):
        break
    l+=1;

if(l==0):
    print('No recent submission')
else:
    print('Total problem solved '+str(l))
    fw=open(file_name,'w')
    fw.write(link[0]['href'])
    fw.close()
    print('Enter YES to open all the question : ')
    whatDO = input()
    if (whatDO == 'YES'):
        km = 0
        base_url = 'https://www.hackerearth.com'
        for x in link:
            if (km == l):
                break;
            url = base_url + x['href']
            webbrowser.open(url)
            km += 1
