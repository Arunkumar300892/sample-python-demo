import os
import sys

from datetime import datetime
from simple_salesforce import Salesforce 
sf = Salesforce(username='abatini27@gmail.com', password='Salesa@1234', security_token='L9hbrqxdutQWm1bmswnM8uN51', sandbox=False)
Lastname='AD Bathini'
Firstname='Bathini'
Accountcreation = sf.Account.create({'Name':Lastname})
