def verify_card_number(card_number):
    char_to_remove = " -"
    clean = str.maketrans("", "", char_to_remove)
    number = card_number.translate(clean)
    total = 0
    reverse = number[::-1]
    
    for i, digit in enumerate(reverse):
        num = int(digit)
        
        if i % 2 == 1:
            num *= 2
            if num > 9:
                num -= 9
            
        total += num

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number('453914889'))
print(verify_card_number('4111-1111-1111-1111'))
print(verify_card_number('453914881'))
print(verify_card_number('1234 5678 9012 3456'))
