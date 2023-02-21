from order_items import Orderitems
class Viewitems:
    @classmethod
    def viewitems(self):
       
        veg_price =[100,50,35]
        grocery_price = [300,30,30]
        fruit_price = [100,70,120]
        print("1 for vegitables")
        print("2 for grocery")
        print("3 for fruits")
        user_choice = int(input("Enter Your Choice\n"))

        if user_choice == 1:
            print("1 for Carrot")
            print("2 for Potato")
            print("3 for Ladies finger")
            choice = int(input("Enter Your Choice:\n"))
            if choice == 1:                
                print("Price:",veg_price[0])
                Orderitems.orderitems(veg_price[0],0,0)
            elif choice == 2:
                print("Price:",veg_price[1])
                Orderitems.orderitems(veg_price[1],0,0)
            elif choice == 3:
                print("Price:",veg_price[2])
                Orderitems.orderitems(veg_price[2],0,0)
            else:
                print("Out of Stock")

        elif user_choice == 2:
            print("1 for Rice")
            print("2 for Dhal")
            print("3 for Oil")
            choice = int(input("Enter Your Choice:\n"))
            if choice == 1:                
                print("Price:",grocery_price[0])
                Orderitems.orderitems(grocery_price[0],0,1)
            elif choice == 2:
                print("Price:",grocery_price[1])
                Orderitems.orderitems(grocery_price[1],0,1)
            elif choice == 3:
                print("Price:",grocery_price[2])
                Orderitems.orderitems(grocery_price[2],0,1)
            else:
                print("Out of Stock")

        elif user_choice == 3:
            print("1 for Apple")
            print("2 for Orange")
            print("3 for Pomogranade")
            choice = int(input("Enter Your Choice:\n"))
            if choice == 1:                
                print("Price:",fruit_price[0])
                Orderitems.orderitems(fruit_price[0],0,2)
            elif choice == 2:
                print("Price:",fruit_price[1])
                Orderitems.orderitems(fruit_price[1],0,2)
            elif choice == 3:
                print("Price:",fruit_price[2])
                Orderitems.orderitems(fruit_price[2],0,2)
            else:
                print("Out of Stock")