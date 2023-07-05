print("Welcome to the SBI Bank!")
while True:
    Client=input("Please insert your card\n")
    if Client!="yes":
     continue
    else:
       Client=="yes"
    Languages=["1-Tamil","2-English","3-Hindi"]
    1,2,3==Languages
    for x in Languages:
     print(x)
    break
while True:
    user=int(input("Please Select Language\n"))
    if user!=2:
        print("Select the language correctly!")
        continue
    else:
        user==2
        break
while True: 
    n=int(input("Enter the Pin Number\n"))
    if len(str(n))!=4:
        print("Enter the correct four digit pin number!\n ")
        continue
    elif str(n)==4226:
        print("Hello Vishal!")
    options=["1-Registration","2-Mini Statement","3-Services","4-Quick Cash", "5-Transfer","6-Banking"]
    1,2,3,4,5,6==options
    for x in options:
     print(x)
    break
    #else:
       #len(str(n))==4
      #options={"Registration:R","Mini Statement:M","Services:S","Quick Cash:Q", "Transfer:T","Banking:B"}
    #R,M,S,Q,T,B=options
    #print(options)
    #break
while True:
    a=int(input("Please choose Banking for cash Withdrawal and Balance Enquiry\n"))
    if a!= 6:
        print("Pls select the number only from above given list\n" )
        continue
    else:
        a==6
    transactions=["1-Pin change","2-Deposit","3-Cash withdrawal","4-Balance Enquiry","5-Mini Statement","6-Others"]
    1,2,3,4,5,6==transactions
    for x in transactions:
     print(x)
    break
bal=50000
while True:
    m=int(input("Please select transactions\n"))
    if m==4:
        print("your balance is :",bal)
        exit()
    elif m==3:
        accounttype=["1-KCC","2-Current","3-Saving"]
        1,2,3==accounttype
        for x in accounttype:
         print(x)
        break
while True:
    c=int(input("please select account type\n"))
    if c!=3:
        continue
    else:
        c==3
    cashavailable=[100,500,2000,200]
    print(cashavailable)
    x,y,z,i=cashavailable
    break
d=int(input("Enter the amount\n"))
import time
if d=='x':
    print("Your transaction is being proceeded")
    time.sleep(3)
    print (d)
    time.sleep(3)
elif d == 'y':
    print("your transaction is being proceeded")
    time.sleep(3)
    print(d)
    time.sleep(3)
elif d=='z':
    print("Your transaction is being proceeded")
    time.sleep(3)
    print(d)
    time.sleep(3)
else :
    d=='i'
    print("Your transaction is being proceeded")
    time.sleep(3)
    print(d)
    time.sleep(3)
print("Collect your cash!!")
#time.sleep(1)
print("Transaction is complete")
time.sleep(3)
customer=input('Want you to display the balance in the screen?\n')
time.sleep(2)
while True:
    customer=input('Want you to display the balance in the screen?\n')
    if customer=="yes":
        aval_bal=(bal-d)
        print(aval_bal)
        print("Thankyou!")
        break
    elif customer=="no":
        print("Thankyou!")
        break
    else:
        print("enter correct answer")
while True:
    h=input("Do you want to register this is as favourite transcation?\n")
    print(" type:yes or no")
    if h=="yes":
        print("Done! It is regitered.")
        print("Thank You!")
        break
    elif h=="no":
        print("Thank You!")
        break
    else:
        print("enter correct answer")
    
    

