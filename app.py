import os
import sys
from datetime import datetime
from simple_salesforce import Salesforce 
sf = Salesforce(username='abatini27@gmail.com', password='Salesa@1234', security_token='4x8sp5Hi9tlbcBzfOCv2cP8N', sandbox=False)
Lastname='Ranganathan'
Firstname='Arunkumar'
Name = Firstname + " " + Lastname
print("User Name:" + Name)
Accountcreation = sf.Account.create({'Name': Name})
print("AccountCreated:")
for k, v in Accountcreation.items():
  print(k, v)
exit()
