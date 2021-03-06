import re
import unittest
class Discount():
    def getCode(self):
        return self.code
    def getSpecialprice(self):
        return self.special_price
    def getApplyPosition(self):
        return self.position
    def getLimit(self):
        return self.limit
    def getValue(self):
        return self.value
    def setDiscount(self,specialoffer):
       str = re.sub(r"\s+", "", specialoffer.lower())
       if (str == "buy1get1free"):
           self.position = 2
           self.value = 1
           self.limit = 0
           self.code = 1
       if(str == "buy2get1halfoff"):
           self.position = 3
           self.value = 0.5
           self.limit = 0
           self.code = 1
       if(str == "buy3get220%off"):
           self.position = 5
           self.value = 0.4
           self.limit = 0
           self.code = 1
       if(str == "3for$5"):
           self.position = 3
           self.special_price = 5
           self.code = 2
       if(str == "2for$3"):
           self.position = 2
           self.special_price = 3
           self.code = 2
       if(str == "buy1get1free,limit6"):
           self.position = 2
           self.value = 1
           self.limit = 6
           self.code = 1
       if(str == "buy2get1halfoff,limit8"):
           self.position = 3
           self.value = 0.5
           self.limit = 8
           self.code = 1
       if(str == "buy3get220%off,limit10"):
           self.position = 5
           self.value = 0.4
           self.limit = 10
           self.code = 1
       if(str == "buy3.5lbget1.5lbhalfoff"):
           self.position = 3.5
           self.value = 0.75
           self.limit = 0
           self.code = 3
       
           
    def __init__(self,specialoffer):
        self.code = 0
        self.position = 0
        self.value = 0
        self.limit = 0
        self.special_price = 0
        self.setDiscount(specialoffer)
     

class product():

     def getName(self):
       return self.name

     def getPrice(self):
         price = self.price - self.markdown
         return price
     def getMarkdown(self):
        return self.markdown

     def getDiscount(self):
        return self.discount 
    
     def __init__(self,name, price, specialoffer , ifbyweight, markdown):
       self.name = name.lower()
       self.price = price
       self.markdown = markdown
       self.discount = None
       self.specialoffer = specialoffer
       if(specialoffer is not None):
        self.discount = Discount(specialoffer)
       
       self.ifbyweight = ifbyweight
class test(unittest.TestCase):
     #testcase1
     def test_dictionaryInputList(self):
         for input in inputList:
             self.assertEqual(dict[input.getName()],input)
     #testcase2       
     def test_properdiscount(self):
         item = product('banana',3.2,"buy 1 get 1 free",True,0.33)
         self.assertEqual(item.discount.getApplyPosition(),2)
         self.assertEqual(item.discount.getValue(),1)
         self.assertEqual(item.discount.getLimit(),0)   
         item1 = product('kiwa',4.2,"buy 1 get 1 free, limit 6",True,0.33)
         self.assertEqual(item1.discount.getApplyPosition(),2)
         self.assertEqual(item1.discount.getValue(),1)
         self.assertEqual(item1.discount.getLimit(),6) 
     #testcase3
     def test_discount(self):
        checkout_list.clear()
        #test discount item cal by unit without limit
        #apple*4+peach*4
        #total=8*2.2-(4*2.2)+1*4-(1*1*0.5)=12.3
        checkout_items = ["apple","peach","apple","peach","apple","apple","apple","peach","peach","apple","apple","apple"]
        for item in checkout_items:
            scan_item(item)
        self.assertEqual(round(get_total(), 2),12.3)
     #testcase4
     def test_discountWithLimit(self):
         #test discount item cal by unit without limit
         #kiwi*8+banana*9
         #total=8*2.2-(3*2.2)+1*9-(1*2*0.5)=19
          checkout_list.clear()
          checkout_items = ["kiwi","banana","kiwi","banana","kiwi","banana","banana","banana","kiwi","banana","banana","banana","kiwi","banana","kiwi","kiwi","kiwi"]
          for item in checkout_items:
              scan_item(item)
          self.assertEqual(round(get_total(), 2),19)
     #testcase5
     def test_discountwithSpeicalPrice(self):
         #test discount item cal by unit with discount "buy N for $M"
         #potato*7+tomato*5+banana*3
         #total=5+5+1*2+3+3+2+3-0.5=22.5
          checkout_list.clear()
          checkout_items = ["potato","tomato","potato","tomato","potato","tomato","potato","tomato","potato","tomato","potato","banana","potato","banana","banana"]
          for item in checkout_items:
              scan_item(item)
          self.assertEqual(round(get_total(), 2),22.5)
     #testcase6
     def test_byweightItems(self):
         #test item cal by weight
         #chicken 3 lb*(1.2-0.31)=2.84
          checkout_list.clear()
          checkout_items = ["chicken"]
          for item in checkout_items:
              scan_item(item)
          self.assertEqual(round(get_total(), 2),2.67)
     #testcase7
     def test_byweightItems(self):
         #test item cal by weight
         #chicken 3 lb*(1.2-0.31)=2.84 + lamb*5lb - 1.5*0.5=12.19+2.67=11.99
          checkout_list.clear()
          checkout_items = ["chicken","lamb"]
          print("This is testing case 7, please enter the 3 lb chicken and 5 lb lamb ")
          for item in checkout_items:
              print(item + ":")
              scan_item(item)
             
          self.assertEqual(round(get_total(), 2),14.87)
     #testcase8
     def test_inputByUser(self):
          #3*apple+3 peach
          #remove 1*apple +1*peach= 2.2+2=4.2
          checkout_list.clear()
          print("This is test case 8 please scan, 3 apples and 3 peaches ,and remove 1 apple 1 peach")
          checkout_item = str(input("enter item name or '0' to exit, 'c'to cancel item"))
          while(checkout_item != "0"): 
             if(checkout_item.lower() == "c"):
                remove_item()
             else:
                scan_item(checkout_item)
             checkout_item = str(input("enter item name or '0' to exit, 'c'to cancel item"))
          self.assertEqual(round(get_total(), 2),4.2)   
def init_productList():
   for input in inputList:

      dict[input.getName()] = input

def scan_item(checkout_product):
   temp_object = dict.get(checkout_product.lower())
   if (temp_object is None):
       print("The item is not scannable")
       return
   discount = temp_object.getDiscount()
   key = temp_object.getName()
   price = temp_object.getPrice()
   total = price
   add_number = 1
   item = checkout_list.get(key)
   if(temp_object.ifbyweight):
       add_number = input("enter item weight")
       total = float(price) * float(add_number)
       #add discount here:
       if(discount.getCode() != 0):
           position = float(checkout_list[key]['count'] + add_number) if item is not None else float(add_number)
       
           if(position >= discount.getApplyPosition()):
               number = int(position / discount.getApplyPosition()) * discount.getValue() * price
               total-=number
    
   if item is not None:
        position = checkout_list[key]['count']
        position +=add_number
        checkout_list[key]['count'] = position
        if (discount.getCode() != 0):
            if(position % discount.getApplyPosition() == 0):
                if(discount.getCode() == 1):
                    if(discount.getCode() == 1 and discount.getLimit() == 0 or (discount.getLimit() != 0 and position <= discount.getLimit())):
                          total = total - discount.getValue() * price
                          checkout_list[key]['discount'] = discount.getValue() * price
                elif(discount.getCode() == 2):
                    checkout_list[key]['total'] = discount.getSpecialprice() * (position / discount.getApplyPosition())
                    checkout_list[key]['discount'] = price - discount.getValue() * price
                    total = 0
        checkout_list[key]['total']+=total    
   else:
       checkout_list[key] = {'product':temp_object,'count':add_number,'total':total}

def remove_item():
    remove_item = str(input("enter item you like to remove"))
    checkout_item = checkout_list.get(remove_item.lower())
    item = checkout_item['product']
    if(item is None):
        print("The item you enter is not valid, please try again")
        return
    if(item.ifbyweight):
        del checkout_list[remove_item]
    else:
        if(checkout_item['count'] <= item.getDiscount().getApplyPosition()):
            checkout_list[remove_item]['total']+=checkout_item['discount']

        checkout_list[remove_item]['count']-=1
        checkout_list[remove_item]['total']-=item.getPrice()
def get_total():
    total = 0
    for item in checkout_list.values():
        total+=item['total']
    return total

if __name__ == '__main__':
    dict = {}
    checkout_list = {}
    inputList = [product('beef',3.2,"buy 5 get 3 half off,limit 8",False,0.33)
               ,product('pork',2.2,"",False,0)
               ,product('Apple',2.2,"buy1get1free",False,0)
               ,product('kiwi',2.2,"buy1get1free,limit6",False,0)
               ,product('Peach',1.5,"buy2get1halfoff",False,0.5)
               ,product('banana',1.5,"buy2get1halfoff,limit8",False,0.5)
               ,product('potato',2.5,"3for$5",False,0.5)
               ,product('tomato',2,"2for$3",False,0)
               ,product('lamb',3.2,"buy3.5 lb get1.5lb half off",True,0.33)
               ,product('chicken',1.2,"",True,0.31)]
    init_productList()
    total = 0
   
    
    unittest.main(exit=False)
