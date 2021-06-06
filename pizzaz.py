import sys
import math
import re

movie_information = [
    {"title": "The Shining.", "year": "1980.", "length": "2h 26m.", "time_start": "10:00.", "room": "Room 1"},
    {"title": "Your Name.", "year": "2016.", "length": "1h 52m.", "time_start": "13:00.", "room": "Room 1"},
    {"title": "Fate/Stay Night: Heaven's Feel - III. Spring Song.", "year": "2020.","length": "2h 0m.", "time_start": "15:00.", "room": "Room 1"},
    {"title": "The Night Is Short, Walk on Girl.", "year": "2017.", "length": "1h 32m.", "time_start": "17:30.", "room": "Room 1"},
    {"title": "The Truman Show.", "year": "1998.", "length": "1h 47m.", "time_start": "19:30.", "room": "Room 1"},
    {"title": "Genocidal Organ.", "year": "2017.", "length": "1hr 55m.", "time_start": "21:45.", "room": "Room 1"},
    {"title": "Jacob's Ladder.", "year": "1990.", "length": "1h 56m.", "time_start": "10:00.", "room": "Room 2"},
    {"title": "Parasite.", "year": "2019.", "length": "2h 12m.", "time_start": "12:15.", "room": "Room 2"},
    {"title": "The Dark Knight.", "year": "2008.", "length": "2h 32min.", "time_start": "14:45.", "room": "Room 2"},
    {"title": "Blade Runner 2049.", "year": "2017.", "length": "2h 44m.", "time_start": "17:45.", "room": "Room 2"},
    {"title": "The Mist.", "year": "2007.", "length": "2h 6m.", "time_start": "21:00.", "room": "Room 2"},
    {"title": "Demon Slayer: Mugen Train.", "year": "2020.", "length": "1h59min.", "time_start": "23:20.", "room": "Room 2"},
    {"title": "The Matrix.", "year": "1999.", "length": "2h 16m.", "time_start": "10:00.", "room": "Room 3"},
    {"title": "Inception.", "year": "2010.", "length": "2h 42m.", "time_start": "11:30.", "room": "Room 3"},
    {"title": "Shutter Island.", "year": "2010.", "length": "2h 19m.", "time_start": "14:30.", "room": "Room 3"},
    {"title": "Soul.", "year": "2020.", "length": "1hr 40m.", "time_start": "17:00.", "room": "Room 3"},
    {"title": "Mrs. Brown.", "year": "1997.", "length": "1h 41min.", "time_start": "19:00.", "room": "Room 3"},
    {"title": "Peppa Pig: Festival of Fun.", "year": "2019.", "length": "1h 8min.", "time_start": "21:00.", "room": "Room 3"},
    {"title": "Titanic.", "year": "1997.", "length": "3h 30min.", "time_start": "22:15.", "room": "Room 3"},
]

def switch_warning():
    print("\nSorry. This program does not recognise the switch options. ")
    sys.exit("Bye.")


def timeformat_warning():
    print("\nSorry. This program does not recognise the time format entered. ")
    sys.exit("Bye.")

def verify_time_str(time_str):
    time_str = str(time_str)
    value = re.compile(r'^[0-9]{2}\:[0-9]{2}$')
    if(value.match(time_str)):
        list_time_str = time_str.split(":")
        if(time_str == "24:00" or list_time_str[1] == "60"):
            timeformat_warning()
    else:
        timeformat_warning()

def convert_time_to_minutes(time):
    time_list = time.split(":")
    return int(time_list[0])*60+int(time_list[1])

def display_movies(input_time):
    for i in movie_information:
        if(convert_time_to_minutes(i["time_start"][:-1]) >= convert_time_to_minutes(input_time)):
            print(i["title"], i["year"], i["length"], i["time_start"], i["room"])
    print("\nBye.")

def ask_for_movie_title():
    matched = False
    input_movie = input("\nWhat is the name of the movie you want to watch? ").upper()
    movie_title_room=[]
    for i in movie_information:
        if(i["title"][:-1].upper() == input_movie):
            matched = True
            movie_title_room.append(input_movie)
            movie_title_room.append(i["room"])
    if(matched == True):
        return movie_title_room
    else:
        return handle_movie_notfound()

def handle_movie_notfound():
    input_for_notfound = input("\nSorry, we could not find that movie. Enter Y to try again or N to quit. ").upper()
    if(input_for_notfound.upper() == "Y"):
        return ask_for_movie_title()
    elif(input_for_notfound == "N"):
        sys.exit("Bye")
    else:
        return handle_movie_notfound()

def repeat_ask_size():
    reply_size_corn = input("\nYou want popcorn. What size Small, Medium or Large? (S/M/L) ").upper()
    if(reply_size_corn.upper() == "L"):
        return "L"
    elif(reply_size_corn.upper() == "M"):
        return "M"
    elif(reply_size_corn.upper() == "S"):
        return "S"
    else:
        return repeat_ask_size()

def ask_single_popcorn():
    reply_popcorn = input("\nWould you like to order popcorn? Y/N ").upper()
    if(reply_popcorn.upper() == "Y"):
        return repeat_ask_size()
    elif(reply_popcorn.upper() == "N"):
        return "N"
    else:
        return ask_single_popcorn()

def check_money_divisible(final_price, amount_paid):
    split_amount_paid = str(amount_paid).split(".")
    if(len(split_amount_paid) == 1):
        return
    elif(float(split_amount_paid[1]) % 0.05 == 0):
        return
    print('The input given is not divisible by 5c. Enter a valid payment.')
    return pay_money(final_price)

def check_input_isnum(amount_paid):
    value = re.compile(r'^[0-9]+\.?[0-9]+$')
    result = value.match(amount_paid)
    if result:
        return True
    else:
        return False

def pay_money(final_price):
    amount_paid = input("\nEnter the amount paid: $")
    if(check_input_isnum(amount_paid) == False):
        return pay_money(final_price)
    check_money_divisible(final_price, amount_paid)
    change = float(amount_paid)-float(final_price)
    if(change < 0):
        print("The user is $%.2f short. Ask the user to pay the correct amount." % (-change))
        return pay_money(final_price)
    elif(change == 0):
        print("Change: $0.00")
        sys.exit("Bye.")
    else:
        print("Change: $%.2f" % change)
        map_res = handle_payment(amount_paid, final_price)
        for key in map_res.keys():
            print(" "+key+": "+map_res[key])
        sys.exit("Bye.")

def check_ticket_price(movie_title):
    ticket_price = 0.00
    for i in movie_information:
        if(i["title"][:-1].upper() == movie_title):
            time_start = i["time_start"][:-1]
            break
    if(time_start >= '16:00'):
        ticket_price = 15.00
    elif(time_start < '16:00'):
        ticket_price = 13.00
    return float(ticket_price)

def check_popcorn_price(answer_for_popcorn):
    popcorn_price = 0.00
    if(answer_for_popcorn == "S"):
        popcorn_price = 3.50
    elif(answer_for_popcorn == "M"):
        popcorn_price = 5.00
    elif(answer_for_popcorn == "L"):
        popcorn_price = 7.00
    return popcorn_price

def price_check_popcorn_size(popcorn_price):
    size = ''
    if(popcorn_price == 3.5):
        size = "Small"
    elif(popcorn_price == 5.00):
        size = "Medium"
    elif(popcorn_price == 7.00):
        size = "Large"
    else:
        size = "No   "
    return size

def calculate_single_price(movie_title, answer_for_popcorn):
    popcorn_price = final_price = 0
    ticket_price = check_ticket_price(movie_title)
    popcorn_price = check_popcorn_price(answer_for_popcorn)
    size = price_check_popcorn_size(popcorn_price)
    final_price = popcorn_price+ticket_price
    if(ticket_price == 15.00):
        print("For 1 person, the initial cost is $%.2f" % final_price)
        print(" Person 1: Ticket from 16:00      $15.00")
    elif(ticket_price == 13.00):
        print("For 1 person, the initial cost is $%.2f" % final_price)
        print(" Person 1: Ticket before 16:00    $13.00")
    print(" Person 1: %s popcorn          $ %.2f\n" % (size, popcorn_price))
    print(" No discounts applied             $ 0.00\n")
    print("The final price is                $%.2f\n" % final_price)
    pay_money(final_price)

def ask_num_people(movie_room):
    capacities = {
        "Room 1":"35",
        "Room 2":"136",
        "Room 3":"42"
    }
    capacity = int(capacities[movie_room])
    if(capacity%2 == 0):
        capacity = capacity/2
    else:
        capacity = round(capacity/2)
    reply_num_people = input("\nHow many persons will you like to book for? ")
    if(reply_num_people.isdigit() == False):
        return ask_num_people(movie_room)
    elif(int(reply_num_people) < 2):
        reply_continue = input("\nSorry, you must have at least two customers for a group booking. Enter Y to try again or N to quit.").upper()
        if(reply_continue == "N"):
            sys.exit("Bye.")
        else:
            return ask_num_people(movie_room)
    elif(int(reply_num_people) > capacity):
        response = input("\nSorry, we do not have enough space to hold %d people in the theater room of %d seats. Enter Y to try a different movie name or N to quit." 
        %(int(reply_num_people), capacity)).upper()
        if(response == "Y"):
            ask_num_people(movie_room)
        else:
            sys.exit("Bye.")
    else:
        return int(reply_num_people)

def calculate_decimal_money(original_decimal):
    original_decimal = float("%.2f" % original_decimal)
    remainder = original_decimal % 0.1
    if(remainder < 0.025):
        return round(original_decimal, 1)
    elif(remainder > 0.075):
        return round(original_decimal, 1)
    else:
        a, b, c = str(original_decimal).partition('.')
        c = c[:1]
        del b
        return round(float(".".join([a, c]))+0.05, 2)

def group_discount(type_of_cost, price):
    if type_of_cost == "ticket":
        return calculate_decimal_money(price*0.1)
    elif type_of_cost == "popcorn":
        return calculate_decimal_money(price*0.2)

def handle_payment(amount_cash, final_price):
    if(float(amount_cash) > final_price):
        remainder = float(amount_cash)-final_price
        map_res = {}
        denominations = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
        map_key = ["$100", "$50", "$20", "$10", "$ 5", "$ 2", "$ 1", "50c", "20c", "10c", " 5 c"]
        i = 0
        while i < len(denominations):
            val = denominations[i]
            if(val <= remainder):
                map_res[map_key[i]] = str(int(remainder//val))
                remainder = remainder-(remainder//val)*val
            i=i+1
            if(remainder > 0.00001 and remainder < -0.00001):
                print("change calculation wrong!!!!!!")
    return map_res

def group_order_popcorn(num_people):
    detailed_popcorn_order = {}
    i = 1
    while i <= num_people:
        response = group_popcorn_YN(i)
        detailed_popcorn_order[i] = response
        i = i+1
    return detailed_popcorn_order

def group_popcorn_YN(i):
    response = input("\nFor person %d, would you like to order popcorn? Y/N " % i).upper()
    if(response == "N"):
        return response
    elif(response == "Y"):
        response_popcorn_size = group_popcorn_size(i)
        return "Y" + response_popcorn_size
    else:
        return group_popcorn_YN(i)

def group_popcorn_size(i):
    response = input("\nPerson %d wants popcorn. What size Small, Medium or Large? (S/M/L) " % i).upper()
    if(response == "S" or response == "M" or response == "L" ):
        return response
    else:
        return group_popcorn_size(i)

def group_seats_number(num_people):
    i = 1
    while i <= num_people:
        seatnum = 2*(i)-1
        print("The seat number for person %d is #%d" % (i, seatnum))
        i = i+1

def calculate_group_price(detailed_popcorn_order, movie_title, reply_num_people):
    each_popcorn_cost = []
    total_popcorn_price = initial_cost = 0
    ticket_price = check_ticket_price(movie_title)
    for i in detailed_popcorn_order:
        if(detailed_popcorn_order[i][0] == "Y"):
            each_popcorn_cost.append(check_popcorn_price(detailed_popcorn_order[i][1]))
        elif(detailed_popcorn_order[i][0] == "N"):
            each_popcorn_cost.append(0)
        else:
            each_popcorn_cost.append("0")
    for i in each_popcorn_cost:
        total_popcorn_price = total_popcorn_price+float(i)
    initial_cost = total_popcorn_price+ticket_price*reply_num_people
    print("\nFor %d persons, the initial cost is $%.2f" %(reply_num_people, float(initial_cost)))
    j = 1
    while j <= len(each_popcorn_cost):
        size = price_check_popcorn_size(each_popcorn_cost[j-1])
        print(" Person %d: Ticket before 16:00    $%.2f" % (j, ticket_price))
        print(" Person %d: %s popcorn          $ %.2f" % (j, size, each_popcorn_cost[j-1]))
        j = j+1
    if(initial_cost < 100):
        print("\n No discounts applied             $ 0.00")
        print("\nThe final price is                $%.2f\n" % initial_cost)
        pay_money(initial_cost)
    elif(initial_cost > 100):
        tickets_reduced_part = group_discount("ticket", ticket_price*reply_num_people)
        popcorn_reduced_part = 0.00
        for i in each_popcorn_cost:
            popcorn_reduced_part = popcorn_reduced_part + group_discount("popcorn", float(i))
        final_price = initial_cost - popcorn_reduced_part - tickets_reduced_part
        print("\n Discount applied tickets x%d     -$ %.2f\n" %(reply_num_people , tickets_reduced_part ))
        print(" Discount applied popcorn x%d     -$ %.2f" %(reply_num_people , popcorn_reduced_part ))
        print("The final price is                $%.2f\n" % final_price)
        pay_money(final_price)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("~ Welcome to Pizzaz cinema ~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

if(len(sys.argv) == 1):
    sys.exit("Usage: python3 pizzaz.py [--show <timenow> | --book | --group]")
elif(sys.argv[1] == "--show"):
    if(len(sys.argv) == 3):
        verify_time_str(sys.argv[2])
        display_movies(sys.argv[2])
    else:
        switch_warning()
elif(sys.argv[1] == "--book"):
    if(len(sys.argv) > 2):
        switch_warning()
    else:
        movie_title_room = ask_for_movie_title()
        movie_title = movie_title_room[0]
        answer_for_popcorn = ask_single_popcorn()
        print("\nThe seat number for person 1 is #17")
        calculate_single_price(movie_title, answer_for_popcorn)
elif(sys.argv[1] == "--group"):
    if(len(sys.argv) > 2):
        switch_warning()
    movie_title_room = ask_for_movie_title()
    movie_title = movie_title_room[0]
    movie_room = movie_title_room[1]
    reply_num_people = ask_num_people(movie_room)
    detailed_popcorn_order = group_order_popcorn(reply_num_people)
    group_seats_number(reply_num_people)
    calculate_group_price(detailed_popcorn_order, movie_title, reply_num_people)
else:
    switch_warning()