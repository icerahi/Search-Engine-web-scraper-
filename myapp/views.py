from django.shortcuts import render
import requests 
from requests.compat import quote_plus
from bs4 import BeautifulSoup
# Create your views here.
def home(request):
    return render(request,'home.html')

base_url="https://search.yahoo.com/search?p={}"
def search(request):
    search=request.POST.get('q')

    
    final_url=base_url.format(quote_plus(search))

    response=requests.get(final_url)
    data=response.text
    soup=BeautifulSoup(data,'html.parser')
    all_raw_data=soup.find_all('div',{'class':'dd'})
    final_result=[]
    for post in all_raw_data:
        post_title=post.find('a').text
        post_url =post.find('a').get('href')
        if post.find('p',{'class':'lh-16'}):
            post_details=post.find('p',{'class':'lh-16'}).text
        else:
            post_details='Details: not found!'
        print(post_title)
        print(post_url)
        print(post_details)
        final_result.append([post_title,post_url,post_details])
       
    

        context={
            'search':'search',
            'results':final_result,
        }

    


    
 
    return render(request,'result.html',context)
