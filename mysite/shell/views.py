from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new_page(request):
    data = request.GET['fulltextarea']
    # os.system('say Mahadev')
    os.system('python3 ../testnmap.py '+data)

    os.system('python3 ../testnmap.py '+data)
    file=open('./text1.txt','r')
    data1 = file.readlines()
    file.close()
    data1= str(data1[0])
    data1 = data1.strip('Starting Nmap 7.70 ( https://nmap.org ) at ')
    data1 =["Scanning Started at: "+data1]
    

    file=open('./text2.txt','r')
    data2 = file.readlines()
    data2 = list(data2)
    file.close()

    file=open('./text3.txt','r')
    data3 = file.readlines()
    file.close()
    data3= str(data3[0])
    data3 = data3.strip('Nmap done: ')
    data3 = ['Scan Completed at: '+data3]



    file=open('./text4.txt','r')
    data4 = file.readlines()
    data = list(data4)
    
    file.close()

    file=open('./text5.txt','r')
    data5 = file.readlines()
    data = list(data5)
    file.close()

    return render(request, 'newpage.html', {'data1':data1,'data2':data2,'data3':data3,'data4':data4,'data5':data})
    