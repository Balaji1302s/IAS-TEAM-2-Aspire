from payments import Payments
class Orderitems:
    veg_stock =[10,10,10]
    grocery_stock =[10,10,10]
    fruit_stock =[10,10,10]
    
    # print(self.veg_stock)
    @classmethod
    def orderitems(self,price,ind,ind1):
        if ind1 == 0:
            quantity = int(input("Enter Quantity\n"))
            if quantity <= self.veg_stock[ind]:
                total_price = quantity*price
                print("price:",total_price)
                self.veg_stock[ind] -= quantity
                print(self.veg_stock[ind])
                Payments().paymentchoice()


        if ind1 == 1:
            quantity = int(input("Enter Quantity\n"))
            if quantity <= self.grocery_stock[ind]:
                total_price = quantity*price
                print("price:",total_price)
                self.grocery_stock[ind] -= quantity
                print(self.grocery_stock[ind])
                Payments().paymentchoice()


        if ind1 == 2:
            quantity = int(input("Enter Quantity\n"))
            if quantity <= self.grocery_stock[ind]:
                total_price = quantity*price
                print("price:",total_price)
                self.grocery_stock[ind] -= quantity
                print(self.grocery_stock[ind])
                Payments().paymentchoice()  

  

           
     
  
        