#importing everything to be used
import csv
import random 
import smtplib, ssl

#csv file with all emails in 
#filename = "FILE LOCATION"

#message to be sent in the emails
message = """\
Subject: Secret Santa!
    
Message Goes Here
"""
  

#function used when ready to send emails  - someone hasnt gotten themselves
def sendemails_func(finallist, lengthoffinal, message):
    '''function for sending emails using the SSL port 465, smtp server and gmail.
    encrypted using ssl'''
    
    print("In Function")
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com" #host server - gmail
    sender_email = "GOOGLE EMAIL HERE" #email sending from

    password = input("Type your password and press enter: ")#password for email sending from 

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password) #logging into server for email
        for x in range(0, lengthoffinal, 3): #loops over the finallist with all the names 
            reciever_email = finallist[x+1] #finds the email of sending to
            reciever = finallist[x] #finds the name of the person sending email to
            secretsantaname = finallist[x+2] #name of their secret santa
            #TAKE OUT PRINT STATEMENT IF DON'T WANT TO KNOW ALLL THE SECRET SANTA's
            #print(reciever_email, reciever, secretsantaname) #prints as sending - check working
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
#print(finallist) #prints the final list of name, email, secret santa


lengthoffinal = len(finallist) #length of all elements, needed for for loop in sending email 

file.close()    #just in case?


sendemails = input("Ready to send email?")
#check if ready - based on for loop from above - dodgy but run code again if has told to answer Yes if ready

if sendemails == "Yes":
    sendemails_func(finallist, lengthoffinal, message) # jump into function ready to send emails
else:
    print("Not going function.") #letting you know whats going on
