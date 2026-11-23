def ticket_total(count, price=12):
    r = count * price
    return r
def final_price(count, is_school_group=False):
    total = ticket_total(count)
    if is_school_group == True:
        total = total * 0.75
    return total
p1 = final_price(3)
print("3 обычных билета:", p1, "руб.")
p2 = final_price(4, is_school_group=True)
print("4 билета для школьной группы:", p2, "руб.")
p3 = ticket_total(2, price=15)
print("2 билета по 15 рублей:", p3, "руб.")
