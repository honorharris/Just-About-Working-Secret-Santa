#importing everything to be used
import csv
import random 
import smtplib, ssl

#file with all emails in 
f#ilename = "C:/Users/honor/Downloads/secret santa.csv"

#message to be sent in the emails
message = """\
Subject: Your Cretins Secret Santa!
    
G'day {name}!
Welcome to the festive and fun ... Cretins Secret Santa 2021!!

After you signed up to the greatest event in all of human history, the elves are pleased to announce that you have been allocated your Secret Santa!
However, before we reveal to you who you are lucky enough to have been given, a few reminders!

The limit for gifts is 15 pounds.
To be confirmed nearer the time on the Crettymen chat, however it is likely that the gift exchange will occur at the Henry Bragg Building during the last week of term. Therefore, please have acquired all gifts by Friday 3rd December 2021 at 12pm. 

And that concludes the reminders! Now onto who your secret santa is...

drumroll please!


Congratualtions, your secret santa is {secretsanta}!!

Make sure you buy them a gift that they will despise, so that the rest of us and those in the North Pole can laugh at them! And if you have Nick Surtees, remember that he hates Peppa Pig. 
    
    
That is all! We hope you have a very merry day, week, month and year, that the rest of 2021 is beautiful and bright and full of light and happiness and good times and good memories!

Long Live the Crettymen!

Merry Christmas and Happy New Year! xxxx





P.S. What do you call an obnoxious reindeer? 
hehehe
... Rude-olph!!
"""
  

#function used when ready to send emails  
def sendemails_func(finallist, lengthoffinal, message):
    '''function for sending emails using the SSL port 465, smtp server and gmail.
    encrypted using ssl'''
    
    print("In Function")
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com" #host server - gmail
    sender_email = "secretsantacretins@gmail.com" #email sending from

    password = input("Type your password and press enter: ")#password for email sending from 

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password) #logging into server for email
        for x in range(0, lengthoffinal, 3): #loops over the finallist with all the names 
            reciever_email = finallist[x+1] #finds the email of sending to
            reciever = finallist[x] #finds the name of the person sending email to
            secretsantaname = finallist[x+2] #name of their secret santa
            #TAKE OUT PRINT STATEMENT IF DON'T WANT TO KNOW ALLL THE SECRET SANTA's
            #print(reciever_email, reciever, secretsantaname) #prints as sending
            #next line is what sends the email
            server.sendmail(sender_email, reciever_email, message.format(name = reciever, secretsanta = secretsantaname))

    return print("All Emails Sent") #once finished ends code and states how emails have been sent 

#opening file 
file = open(filename, "r")
#reading file
csv_reader = csv.reader(file)
#empty list to read into
originallist = []
#reading excel file into the emtpy list
for row in csv_reader:
    originallist.append(row)
    
#finding length of the list - no of people in secret santa
length = len(originallist)

#splitting elements of excel file into name and email- twice as one needed to keep same, one shuffled
name, email = map(list, zip(*originallist))  
nameog, emailog = map(list, zip(*originallist))

#shuffle one of the names
random.shuffle(name)

#empty array for rarranged list - will display as recipient name, recipient email, their secret santa name
finallist = []


#for range of number of people
for x in range(0, (length)):
    if nameog[x] == name[x]: #if names are equal will be giving someone themselves - don't want
        print("Redo - someone was assgined themselves, type no when asked if ready to send email.") #lets know to not continue the file
        break #stops the for loop as already won't work
    else:
        newlist = [nameog[x], emailog[x], name[x]] #holds name, email, their secret santa to write into own new list
        #loops over the row (one row!)
        for row in newlist:
            finallist.append(row)#places above values into a list

#REMOVE FOR SECRET SANTA
#print(finallist) #prints the final list of name, email, secret santa - not seperate so fancy x+1 and steps need to be used 


lengthoffinal = len(finallist) #length of all elements, needed for for loop in sending email 

file.close()    #just in case!


sendemails = input("Ready to send email?")
#check if ready - based on for loop from above - dodgy but run code again if has told to answer Yes if ready

if sendemails == "Yes":
    sendemails_func(finallist, lengthoffinal, message) # jump into function ready to send emails
else:
    print("Not going function.") #letting you know whats going on
    
    
    
    
    
#email: secretsantacretins@gmail.com
#password: cretinssecretsanta
    