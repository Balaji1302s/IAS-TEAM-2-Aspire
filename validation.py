import re
from view_items import Viewitems

class New_Registration:
    
    user_namedetails =[]
    user_password = []
    user_phonenumber = []
    user_emailId = []
    @classmethod
    def new_user(self):
        print("_"*100)
        print("\t\t\t\t\t-_-_Sign-Up Module_-_-")
        print("_"*100)
        flag = True
        while flag:
            temp_username = input("Enter your Name\n")
            regex = ("(?=.*[a-z])(?=.*[A-Z]).+$")
            constraint = re.compile(regex)
            if (re.search(constraint,temp_username)):
                self.user_namedetails.append(temp_username)
                flag = False
            else:
                print("you have entered a Invalid user name please try with valid one:)")
        

        flag = True
        while flag:
            temp_password = input("Enter your Password\n")
            regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?& ])[A-Za-z\d@$!#%*?&]{8,18}$"
            constraint = re.compile(regex)
            if (re.search(constraint,temp_password)):
                self.user_password.append(temp_password)
                flag = False
            else:
                print("you have entered a Invalid password please try with valid one:)")


        flag = True
        while flag:
            try:
                temp_mobilenumber = int(input("Enter your Mobile number\n"))
            except:
                print("you have entered a Invalid mobile number please try with valid one:)")
            else:
                if temp_mobilenumber > 6000000000 and temp_mobilenumber < 10000000000 and temp_mobilenumber != 6666666666 and temp_mobilenumber != 7777777777 and temp_mobilenumber != 8888888888 and temp_mobilenumber != 9999999999:
                    self.user_phonenumber.append(temp_mobilenumber)
                    flag = False
        flag= True
        while flag:
             Email = input("Enter your Email address:")
             regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
             match = re.compile(regex)
             if (re.search(match, Email)):
                self.user_emailId.append(Email)
                flag = False
             else:
              print("Please, Enter your Valid Email Address:")
                
    
class Login(New_Registration):
   
    def __init__(self):
       self.__user_name =""
       self.__password = ""
    @classmethod
    def login(self):
        print("_"*100)
        print("\t\t\t\t\t-_-_Login Module_-_-")
        print("_"*100)
        self.__user_name = input("Enter your Name: ")
        self.__password = input("Enter your Password: ")
        flag = True
        while flag:
            global valid
            valid = 1
            for i in range (len(New_Registration.user_namedetails)):
                if New_Registration.user_namedetails[i] ==  self.__user_name:
                    if New_Registration.user_password[i] == self.__password:
                            
                            valid = 0
                            print("Hi you are loggen in successfully")
                            print("1 for view items")
                            print("2 for view profile")
                            print("Press any key to goto login page")
                            choice = int(input("Enter your choice\n"))
                            if choice == 1:
                                Viewitems().viewitems()
                            elif choice == 2:
                                print(New_Registration.user_namedetails[i])
                                print(New_Registration.user_phonenumber[i])
                                print(New_Registration.user_emailId[i])
                            else:
                                flag = False
                else:
                    pass
            if valid == 1:
                print("You Have entered an wrong user name,Password")
                flag = False
