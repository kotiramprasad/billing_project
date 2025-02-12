items_lists={"apple":12,"sampoo":80,"books":20,"idly ravva":80,"rice":900,"oil":180,"saop set":70,"choclates pack":100}
name=input("please enter your name:")
number=input("plaese enter your mobile number:")
print("Available items:")
print("-" * 40)
for item, price in items_lists.items():
    print(f"{item:20} ₹{price:5}")
print("-" * 40)
print("please choose the items you want",items_lists)
def selecting_items():
        try:
            
            bill_items=[]
            total_price=0
            while True:
                item_name=input("enter the item name:(or done):").strip()
                if item_name.lower()=="done":
                    break
                if item_name not in items_lists:
                    raise ValueError("the item is  not avalibale ,please enter the items as show in the avaliable list ")
                quantity=int(input("please enter the quantity for {item_name}:"))
                price=items_lists[item_name]*quantity
                total_price +=price
                bill_items.append((item_name, quantity, price))

            if bill_items:
                print("\n"+"_"*60)
                print(f"{'product_name':20} {'quantity':10} {'price':10}" )
                print("_"*60)
                for item_name, quantity, price in bill_items:
                     print(f"{item_name:20} {quantity:<10} {price:<10}")
                print("_"*60)
                gst = (total_price * 5) / 100
                final_price = total_price + gst
                print(f"{'Total (without GST):':40} ₹{total_price}")
                print(f"{'GST (5%):':40} ₹{gst:.2f}")
                print(f"{'Final Price:':40} ₹{final_price:.2f}")
                print("_" * 60)
            else:
                 print("no items were selcted")
        except ValueError as ve:
             print(f"input error:{ve}")
        except Exception as e:
            print(f"an unexpected error:{e}")
selecting_items()

