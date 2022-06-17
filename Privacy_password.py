import csv
import time
import datetime
import base64
import pickle
import mysql.connector as msc


def insertVal():
    conn= msc.connect(host="localhost",user="root",password= "PASSWORDISRAJ",database="privacy")
    if conn.is_connected():
        print("mysql successfully connected")
    else:
        print("There is some problem in connection with mysql  please check out")
    cursor= conn.cursor()
    usernm= input("Enter your Username here:")
    pssd= input("enter your password here:")
    data="insert into privacy(usernm,email,password) values(%s,%s,%s)"
    email=""
    value= (usernm,email,pssd)
    cursor.execute(data,value)

    
    conn.commit()
    conn.close()


def showVal():
    conn= msc.connect(host="localhost",user="root",password= "PASSWORDISRAJ",database="privacy")
    if conn.is_connected():
        print("mysql successfully connected")
    else:
        print("There is some problem in connection with mysql  please check out")
    cursor= conn.cursor()
    cursor.execute("select *  from privacy;")
    values= cursor.fetchall()
    for i in values:
        print("%10s| %10s| %10s |"%(i[0],i[1],i[2]))
    
    
insertVal()
ask= input("do you want to continue(y/n):")
if ask=="y":
    showVal()
else:
    print("goodbye")



# function
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()
# A List of Items
items = list(range(0, 57))
l = len(items)

# Initial call to print 0% progress
def loading():
    printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.1)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

def box_text(a):
    f= open("box_text.csv","w",newline="")
    write= csv.writer(f)
    
    write.writerow(["-"*len(a)])
    write.writerow([a])
    write.writerow(["-"*len(a)])
    f.close()
    f= open("box_text.csv","r")
    rd= csv.reader(f)
    for j in rd:
        print(f"|%{len(a)}s|"%(j[0]))

def S_NO(file): #function to put serial no on the table of the first column 
    global last_val
    f= open(file,"r")
    rd= csv.reader(f)
    last_val=0
    
    for J in rd:
        last_val=last_val+1
          
    last_val=last_val/2

def arrange(FILE):   # this function is now only for user_regiestered file 
      f= open(FILE,"r")
      rd= csv.reader(f)
      L1=[]
      for i in rd:
            L1.append(i)
      l_new=[]
      for j in range(len(L1)):
            l_new.append(j+1)
      L3=[]
      for k in l_new:
            if k%2==0:
                  p="2@!!#"
            else:
                  L3.append(k)
      L_final=[]
      for l in range(len(L3)):
            L_final.append(l+1)
      f.close()
      
      
      
      for x in L1:
          
          
          if str(x[0]).isdigit() is True:  
                x.insert(0,L_final[0])
                L_final.pop(0)
                x.pop(1)
          else:
              Z="nothing\n"
     
      f= open(FILE,"w",newline='')
      write= csv.writer(f)
      for z in L1:
          
          write.writerow(z)
      f.close()
      
      
def pssd_set(): # this function is used here to set your new password
    user_nm= input("SET your user name:")
    print("----------------------------------------------------")
    pssd= input("SET your password here:")
    
    usr= base64.b64encode(user_nm.encode("utf-8"))
    psd= base64.b64encode(pssd.encode("utf-8"))
    f= open("pssd.db","wb")
    
    pickle.dump(usr,f)
    pickle.dump(psd,f)
    f.close()
    print("USER NAME AND PASSWORD IS SUCCESFULLY SET")
def pssd_check(): #This function is used to check your password by taking user inputs
    f= open("pssd.db","rb")
    rd= pickle.load(f)
    rd2= pickle.load(f)
    
    user_nm= input("Enter your user name:")
    user_nm=user_nm.strip()
    usr_encode= base64.b64encode(user_nm.encode("utf-8"))
    
    while rd!=usr_encode:
        user_nm= input("ENTER correct user name to proceed:")
        usr_encode= base64.b64encode(user_nm.encode("utf-8"))
    print("Correct user name")
    
    pssd= input("Enter your password here:")
    psd_encode= base64.b64encode(pssd.encode("utf-8"))
    while rd2!=psd_encode:
        pssd= input("Enter correct password:")
        psd_encode= base64.b64encode(pssd.encode("utf-8"))
    print('correct password')
def update_password(): #This fuction checks the correct user name and password
    print("PLEASE VERIFY FIRST TO CHANGE USER NAME AND PASSWORD")
    print("ENTER YOUR LAST USER NAME AND PASSWORD")
    time.sleep(1)
    pssd_check()
    time.sleep(1)
    
    print("verfied success")
    pssd_set()
    time.sleep(1)
    loading()
    print("Password changed successfully")

def row_remove(filenm,user_file): #this fuction remove simultanuosly two rows in a csv file
    
    f= open(filenm,"r")
    rd= csv.reader(f)
    l=[]
    c=0
    for i in rd:
        if user_file==i[1]:
            s= "$12@::2"
            break
            
        else:
            l.append(i)
            c=c+1
    f.close()
    f= open(filenm,"r")
    rd= csv.reader(f)
    l=[]
    
    for i in rd:
        if user_file==i[1]:
            s= "$12@::2"
            
        else:
            l.append(i)
            
    print(c)
    
    l.pop(c)
    f2= open(filenm,"w",newline="")
    write= csv.writer(f2)
    write.writerows(l)
    f2.close()
def decode_file():
        
    f= open("private.csv","r")
    rd= csv.reader(f)
    L=[]
    for i in rd:
        L.append(i)
    L2=[]
    print(L)
    for j in L:
        if j.isalnum() is True:

            L2.append(base64.b64encode(j.encode("utf-8")))
        else:
            pass
        for z in L2:
         
            print("|%5s |%10s | %35s | %20s |"%z[0],z[1],z[2],[3],z[4])
def read_privacy():

    f= open("private.csv","r")
    rd= csv.reader(f)
    for i in rd:
        if str(i).isalnum() is False:



            base64_message_1 = i[3]
            base64_bytes = base64_message_1.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message_1 = message_bytes.decode('ascii')

            base64_message_2 = i[2]
            base64_bytes = base64_message_2.encode('ascii')
            message_bytes = base64.b64decode(base64_bytes)
            message_2 = message_bytes.decode('ascii')
                
            print("|%5s|%40s ---> %30s| "%(i[0],message_2,message_1))

        else:
            print("blank line is excucted")

    
        
            
   



pssd_check()
# here the UI program starts===================================================>>>
while True:
    print("[1] To upadate/add your datas")
    print("[2] To Get secure datas")
    print("[3] To quit")
    print("[4] To get the whole privacy file")
    print("[5] To update password")
    print("[6] to remove any data from your private file")

    user= input("Enter your choice:")
    if user=="1":
        print("[1]--> username")
        print("[2]--> email id")
        usernm= input("Enter your choice:")
        if usernm=="1":
            usernm= input("Enter your username here:")
        else:
            usernm= input("Enter your email address here:")
            while usernm.endswith("@gmail.com") is False:
                usernm=input("Enter a VALID email address:")
        password= input("Enter your password:")

        again= input("Enter your confirm password:")
        while again!=password:
            print("password doesnot matched!! TRY AGAIN")
            
            again= input("Enteer your confirm password:")
        f= open("private.csv", "a",newline="")
        write= csv.writer(f)
        e= datetime.datetime.now()
        encode_usernm = usernm
        encode_usernm__bytes = encode_usernm.encode('ascii')
        base64_encode_usernm_bytes = base64.b64encode(encode_usernm__bytes)
        usernm_encode_value = base64_encode_usernm_bytes.decode('ascii')

        encode_password = password
        encode_password_bytes = encode_password.encode('ascii')
        base64_encode_password_bytes = base64.b64encode(encode_password_bytes)
        password_encode_value = base64_encode_password_bytes.decode('ascii')

        
        encode_usernm= base64.b64encode(usernm.encode("utf-8"))
        
        encode_password= base64.b64encode(password.encode("utf-8"))
        
        date= "%s/%s/%s"%(e.day,e.month,e.year)
        tm="%s:%s:%s"%(e.hour,e.minute,e.second)
        write.writerow([S_NO("private.csv"),date,usernm_encode_value,password_encode_value])
        write.writerow(["-"*5,"-"*10,"-"*35,"-"*20])
        f.close()
    elif user=="3":
        print("Godd bye")
        break
    elif user=="2":
        f= open("private.csv","r")
        rd=csv.reader(f)
        ask= input("Enter your username/email id:")
        encode_usernm = ask
        encode_usernm__bytes = encode_usernm.encode('ascii')
        base64_encode_usernm_bytes = base64.b64encode(encode_usernm__bytes)
        ask_encode = base64_encode_usernm_bytes.decode('ascii')
        loading()
        for i in rd:
            if ask_encode==i[2]:

                base64_message = i[3]
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                box_text("Your password is:"+message)
        

        



    elif user=="4":
        print("Getting your file wait...")
        loading()
        read_privacy()
    elif user=="5":
        update_password()
    elif user=="6":

        loading()
        read_privacy()
        filenm= "private.csv"
        userf= input("ENTER here NAME/S_NO to delete the record:")
                  
        f= open(filenm,"r")
        rd= csv.reader(f)
                  
        b=0
        for i in rd:
            if userf==i[0] or userf==i[2]:
                          
                s= ("$12@::2")
                file=i[2]
                break
                        
            else:
                          
                b=b+1
        f.close()
        f= open(filenm,"r")
        rd= csv.reader(f)
        l=[]
                
        for i in rd:
            if userf==i[0] or userf==i[2]:
                pass
           
                        
            else:

                l.append(i)
                        
          
                
        l.pop(b)
        f2= open(filenm,"w",newline="")
        write= csv.writer(f2)
        write.writerows(l)
        f2.close()

                  
        print("selected record deleted")
                  
        
        arrange("private.csv" )

            
        





        
            

