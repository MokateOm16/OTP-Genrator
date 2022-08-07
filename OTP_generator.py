
#Name    :- Mokate Om Ranjeet
#program :-   OTP Genrator
#Date    :-  4 August 2022(THU)



import random
digit_list = [1,2,3,4,5,6,7,8,9]        #list create keli
OTP = []                                #empty list ghetli
otp = ''                                #empty str ghetli
digit_count = int(input("Enter how many digit you want in OTP = "))
for i in range(digit_count):        #for loop ghetla range la user kadun ghetle count pathavla  
    value = random.choice(digit_list)           #list madhun random number choice kela ani value madhe store kela
    OTP.append(value)                           #OTP list madhe append chay help ne add kela (ex --> ['1','2','3','4','5'])
for i in OTP:                               #list madhe otp hota mhanun for loop lavla all element string convert kela
    otp = otp + str(i)                  

print(f"your OTP is = {otp }")      #print kela
    
