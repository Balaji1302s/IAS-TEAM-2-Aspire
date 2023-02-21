from validation import New_Registration
from validation import Login
class Userchoice():
    @classmethod
    def userChoice(self):
        print("_"*100)
        print("\t\t\t\t-_-_Welcome Online Grocery store_-_-")
        print("_"*100)
        flag = True
        while flag:    
            print("Enter 1 for New Registration")
            print("Enter 2 for Login")
            
            choice = int(input())
            if choice == 1:
                New_Registration.new_user()
            
            elif choice == 2:
                Login.login()
             
            else:
                print("There is no Such Kind of action")
            

