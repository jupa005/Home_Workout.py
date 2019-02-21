# -*- coding: cp1252 -*-
import webbrowser
print('HELLO! WELCOME TO WORKOUT PROGRAM!')
file=open("./brojac.txt",'r') #INSERT YOUR DIRECTORY 
dan= len(file.readlines(  ))
print ('Today is your '+str(dan)+'. day!')
file.close()
file=open("./brojac.txt",'a') #INSERT YOUR DIRECTORY
file.write('\n1')
file.close()
if dan%7==1:
    print('Today is Legs/Abs day!')
    a=int(input('Do you need workout videos? (1=yes,2=no)'))
    if a==1:
        webbrowser.open('https://www.youtube.com/watch?v=3p8EBPVZ2Iw') #abs
        webbrowser.open('https://www.youtube.com/watch?v=Jbvb_MMGc8s') #legs
    c=int(input('Do you want abs workout timer?(1=yes,2=no)'))
    if c==1:
        webbrowser.open('https://www.online-stopwatch.com/full-screen-interval-timer/?c=w5sb8ndghr&fbclid=IwAR0Ko_X5o_ejnHhLTdQVv6imYzr7f7fD0pOAORZNypDKVY_cjpLz54g1L7I')
    b=int(input('Press 1 to get exercises for today!'))
    if b==1:
        file=open("./legs_abs.txt",'r') #INSERT YOUR DIRECTORY
        print(file.read())
        file.close()
    print('That is it! Enjoy!')
elif dan%7==2:
    print('Today is Chest day!')
    a=int(input('Do you need workout videos? (1=yes,2=no)'))
    if a==1:
        webbrowser.open('https://www.youtube.com/watch?v=AK6yZKvJ0uY') #chest       
    b=int(input('Press 1 to get exercises for today!'))
    if b==1:
        file=open("./chest.txt",'r') #INSERT YOUR DIRECTORY
        print (file.read())
        file.close()
    print('That is it! Enjoy!')
elif dan%7==3:
    print('Today is Back/Abs day!')
    a=int(input('Do you need workout videos? (1=yes,2=no)'))
    if a==1:
        webbrowser.open('https://www.youtube.com/watch?v=3p8EBPVZ2Iw') #abs
        webbrowser.open('https://www.youtube.com/watch?v=JQeOhQoi3GY') #back
    c=int(input('Do you want abs workout timer?(1=yes,2=no)'))
    if c==1:
        webbrowser.open('https://www.online-stopwatch.com/full-screen-interval-timer/?c=w5sb8ndghr&fbclid=IwAR0Ko_X5o_ejnHhLTdQVv6imYzr7f7fD0pOAORZNypDKVY_cjpLz54g1L7I')
    b=int(input('Press 1 to get exercises for today!'))
    if b==1:
        file=open("./back_abs.txt",'r') #INSERT YOUR DIRECTORY
        print (file.read())
        file.close()
    print('That is it! Enjoy!')
elif dan%7==4:
    print('Today is your rest day!')
    print('Take a rest, you deserved it!')
elif dan%7==5:
    print('Today is Shoulder/Abs day!')
    a=int(input('Do you need workout videos? (1=yes,2=no)'))
    if a==1:
        webbrowser.open('https://www.youtube.com/watch?v=3p8EBPVZ2Iw') #abs
        webbrowser.open('https://www.youtube.com/watch?v=GXk1GgvhyF8') #shoulder
    c=int(input('Do you want abs workout timer?(1=yes,2=no)'))
    if c==1:
        webbrowser.open('https://www.online-stopwatch.com/full-screen-interval-timer/?c=w5sb8ndghr&fbclid=IwAR0Ko_X5o_ejnHhLTdQVv6imYzr7f7fD0pOAORZNypDKVY_cjpLz54g1L7I')
    b=int(input('Press 1 to get exercises for today!'))
    if b==1:
        file=open("./shoulder_abs.txt",'r') #INSERT YOUR DIRECTORY
        print (file.read())
        file.close()
    print('That is it! Enjoy!')
elif dan%7==6:
    print('Today is Arms day!')
    a=int(input('Do you need workout videos? (1=yes,2=no)'))
    if a==1:
        webbrowser.open('https://www.youtube.com/watch?v=u7MVeTlDX9A') #arms      
    b=int(input('Press 1 to get exercises for today!'))
    if b==1:
        file=open("./arms.txt",'r') #INSERT YOUR DIRECTORY
        print (file.read())
        file.close()
    print('That is it! Enjoy!')
elif dan%7==0:
     print('Today is your rest day!')
     print('Take a rest, you deserved it!')
    
    
    
    
    


