#user product name and quantity tesukovali
busket={}
while True:
    product_name=input("enter the product name(or type 'done'):")
    if product_name.lower()=='done':
        break
    quantity = int(input(f"enter the quantity of{product_name}:"))
    price=float(input(f"enter the price per unit of {product_name}:"))
    if product_name in busket:
        busket[product_name]['quantity']+=quantity
        busket[product_name]["total_price"]+=quantity*price
    else:
        busket[product_name]={"quantity":quantity,"total_price":quantity*price}
print("\nbusket entered:")
total_cost=0
for product,details in busket.items():
    print(f"{product}:{details['quantity']} unit(s),total price:{details['total_price']:.2f}")
    total_cost+=details["total_price"]

membership=input("\nenter your membership type(gold/sliver/bronze/none):").lower()

discount=0
if membership=="gold":
    discount=0.20*total_cost
elif membership=="sliver":
    discount=0.10*total_cost
elif membership=="bronze":
    discount=0.05*total_cost

final_cost=total_cost-discount

print("\nsummarry:")
print(f"total cost:{total_cost:.2f}")
print(f"discount:{discount:.2f}")
print(f"final cost after discount:{final_cost:.2f}")