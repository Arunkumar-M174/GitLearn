# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv('./config.env')
name=str(input("Enter your name:\n"))
print("Welcome To Python Agian",name,"Do well")
number=int(input("Enter the number:\n"))
for count in range (0,number):
    print("Hello",name ,count+1)
if(name!=os.getenv('OWNER')):
    print("You are not the owner of this git")
    
else:
    print("Welcome Owner")

