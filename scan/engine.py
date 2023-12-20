#from Tkinter import *
#from tkFileDialog import askopenfilename
#import tkMessageBox
import os
#import urllib2 as u
import urllib.request as u
import hashlib
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askdirectory
import tkinter.messagebox as tkMessageBox
import json
#CHECKING INTERNET CONNECTION
urltotest="http://www.google.com"
nboftrials=0
answer='NO'
flag=0
while answer=='NO' and nboftrials<2:
    try:
        u.urlopen(urltotest)
        answer='YES'
    except:
        essai='NO'
        nboftrials+=1
        print ("NET NOT CONNECTED!!")
        time.sleep(3)
        flag=-1


if flag==-1:
    print (" Quiting!!")
    quit()

print ("CONNECTION ESTABLISHED!!")

def start(decider):

    try:

        Tk().withdraw()
        if decider == 1: # Multiple files
            #print('h')
            filename=askopenfilenames()
            #print(filename)
            h = [str(hashlib.md5(open(a,'rb').read()).hexdigest()) for a in filename]
            #print(h)
            
            return [h,filename]
            

        elif decider == 0: # Directory files
            Tk().withdraw()
            filess=askdirectory()

            filename = []

            for root, dirs, files in os.walk(filess):
                for file in files:
                    #append the file name to the list
                    filename.append(os.path.join(root,file))

            h = [str(hashlib.md5(open(a,'rb').read()).hexdigest()) for a in filename]
            

            return [h,filename]
        

    except IOError:
        print (IOError)
        print ("\n\n YOU HAVE EIGHTER SELECTED WRONG PATH OR THE FILE FORMAT IS NOT READABLE.... \n\n QUITTING!!")
        quit()
    




def write(d,viruse_files):
    d1=d['scans']
    l=[]
    for i in d1:
        l+=[i,]
    f=open("Output.txt",'w')
    temp=[]
    for i in range(len(l)):
        temp+=[d1[l[i]],]
    sp=" "
    f.writelines("  ---S.No.---"+"\t"*4+"   ---VIRUS FILE PATH/ADDRESS ---"+"\t"*5+"  ---VIRUS FOUND---")
    f.write("\n"*3)
    for i in range(len(viruse_files)):
        t=str(l[i])
        while len(t)!=25:
            t+=sp
        f.writelines(str(i+1)+".)"+"\t"*5+str(viruse_files[i])+"\t"*6+str(temp[i]['result']))
        f.write("\n")
    f.close()    

#os.chdir("C:\Users\Saket\Documents\HackFest17")

def main(h,filename):
    viruse_files = []


    file_counter = 0
    num = len(h) -1
    viruses = 0

    while num > -1:
        import requests
        params = {'apikey': 'f0338650596aa96d724c70f3f0164ee32dbc88542269d515e070d2769cd00ebf', 'resource': h[num]}
        headers = {
        "Accept-Encoding": "gzip, deflate",
        "User-Agent" : "gzip,  My Python requests library example client or username"
                }
        response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
        params=params, headers=headers)

        import time
        global d
        #num = num -1
        if str( a := requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers, verify = False)) == '<Response [204]>'  and file_counter >0:
            startime = int(time.time())

            def blackbox():
                success = True

            import threading
            thread = threading.Thread(target=blackbox)
            thread.start()
            eli_count = 0
            success = False
            while str( a := requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers, verify = False)) == '<Response [204]>':
                endtime =  int(time.time())
                #print(endtime-startime," <-----  SECONDS HAVE PASSED....")
                # ADD LOADING BAR
                #time.sleep(1)

                print('Loading', '.'*(eli_count+1), ' '*(2-eli_count)," " ,endtime-startime,"  SECONDS HAVE PASSED",end='\r')
                eli_count = (eli_count + 1) % 3
                time.sleep(0.1)
                
            success = True   
            thread.join()

            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
            params=params, headers=headers)
            print(response)
            d = response.json()



        elif str( requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers, verify = False)) == '<Response [200]>'  :    
            response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
            params=params, headers=headers)
            print(response)
            d = response.json()
        
        elif str( requests.get('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers, verify = False )) == '<Response [404]>'  :
            print("Something went wrong")

            #print(d)
        #print (d)
        num = num -1
        file_counter = file_counter + 1
        
        #print (d)
        
        if d['verbose_msg'] == 'The requested resource is not among the finished, queued or pending scans':
            print("COULDN'T SCAN THE FILE %s ----- DUE TO TRAFFIC" %filename[num])

        else: 
            if d['positives'] > 3:
                print ("YES !!!, VIRUS HAS BEEN FOUND IN ===>", "Filename: ",filename[num])
                viruse_files.append(filename[num])
                write(d,viruse_files)
                
            
            else:
                print ("NO, VIRUS FOUND IN ===>", "Filename: ",filename[num])


    return viruse_files




def check(filename,viruse_files):
    if len(viruse_files)== 0:
        
            tkMessageBox.showinfo("Voila!!","0 VIRUSES FOUND AMONG %s FILES With MANY SEARCHES of Antivirus and AntiMalware Engines 😁.\n\nThis is not tested much so you can test it with other AV progroms "% (int(len(filename))))
            
    else:
        tkMessageBox.showinfo("ATTENTION!!"," WE HAVE FOUND %s VIRUS FILES OUT of  FILES \nWith MANY SEARCHES of Antivirus and AntiMalware Engines 😥.\n\nThis is not tested much so you can test it with other AV progroms"% (int(len(viruse_files)),int(len(filename))))
        
        if os.name() == 'Windows': 
            os.startfile("Output.txt")
        else: 
            def startfile(fn):
                os.system('open %s' % fn)
            startfile("Output.txt")

