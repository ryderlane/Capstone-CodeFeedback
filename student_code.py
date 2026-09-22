def calculate_order_total(items, tax_rate):
    # make total
    t=0

    # loop
    for i in items:
        price=i["price"]
        qty=i["quantity"]

        # add
        t=t+(price*qty)

    # tax
    tax=t*tax_rate
    final=t+tax

    # check total
    if final>100:
        msg="Large order"
    else:
        msg="Normal order"

    # print stuff
    print("Subtotal:",t)
    print("Tax:",tax)
    print("Total:",final)
    print(msg)

    return final


orders = [
    {"price": 20.00, "quantity": 2},
    {"price": 15.50, "quantity": 3},
    {"price": 8.25, "quantity": 1}
]

calculate_order_total(orders,0.07)