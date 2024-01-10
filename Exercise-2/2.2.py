price_of_book = 24.95
price_of_book_with_discount = 24.95 - (24.95*40/100)

delivery_price_for_firstcopy = 3
delivery_price_for_othercopy = 0.75 #75 cents = 0.75 $

total_price = (price_of_book_with_discount)*(delivery_price_for_firstcopy) + (59*price_of_book_with_discount)*(delivery_price_for_othercopy)

print(f"{total_price} $")

