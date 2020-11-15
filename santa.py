#Seret Santa Generator for 6 people with exclusions
#Nate Jalbert 11-14-20
import random
import smtplib
#Create the original list
#persons 1&2 3&4 5&6 are in relationships and should not be matched
family = ["person1","person2","person3","person4","person5","person6"]
#create a list for the shuffle
fam_suffle = ["person1","person2","person3","person4","person5","person6"]
#shuffle the list
random.shuffle(fam_suffle)

#check to make sure no person is matched with themselves
ans = "Y"
while (ans != "N" and ans !="n"):
    for x in range (0,5,1):
        if family[x] == fam_suffle[x]:
            print("Match detected, re-run program")
    #check to make sure no spouses are matched
    if fam_suffle[0] == "person2":
        print("Re-run the suffle")
    else:
        if fam_suffle[1] == "person1":
            print("Re-run the suffle")
        else:
            if fam_suffle[2] == "person4":
                print("Re-run the suffle")
            else:
                if fam_suffle[3] == "person3":
                    print("Re-run the suffle")
                else:
                    if fam_suffle[4] == "person6":
                        print("Re-run the suffle")
                    else:
                        if fam_suffle[5] == "person5":
                            print("Re-run the suffle")
                        else:
                            print("No spouses are matched")
    ans = raw_input("Do you need to shuffle again (Y/N)? ")
    if ans == "Y" or ans == "y":
        random.shuffle(fam_suffle)
        
#connect to gmail and send the email to each recipient
'''gmail_user="email@gmail.com"
gmail_password="P@$$w0rd"

#recipent emails
person1_email = "person1@gmail.com"
person2_email = "person2@gmail.com"
person3_email = "person3@gmail.com"
person4_email = "person4@gmail.com"
person5_email = "person5@gmail.com"
person6_email = "person6@gmail.com"

#email content
subject = "Your secret Santa Person"
person1_body = "Person1 your secret Santa is " +fam_suffle[0]
person2_body = "Person2 your secret Santa is " +fam_suffle[1]
person3_body = "Person3 your secret Santa is " +fam_suffle[2]
person4_body = "Person4 your secret Santa is " +fam_suffle[3]
person5_body = "Person5 your secret Santa is " +fam_suffle[4]
person6_body = "Person6 your secret Santa is " +fam_suffle[5]

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user,person1_email,person1_body)
    server.sendmail(gmail_user,person2_email,person2_body)
    server.sendmail(gmail_user,person3_email,person3_body)
    server.sendmail(gmail_user,person4_email,person4_body)
    server.sendmail(gmail_user,person5_email,person5_body)
    server.sendmail(gmail_user,person6_email,person6_body)
    server.close()
    print("Emails sent")
except:
    print 'Something went wrong with email client...'
'''

