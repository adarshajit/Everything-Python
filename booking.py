booking={
    "Her":[8.7,5],

    "Nightcrawler":[8.9,5],

    "Social Network":[8.9, 5],
}


print("#####  Welcome to the booking app!! ######")

print("Now Showing")
print("-------------")
show = list(booking)
for i in show:
    print(i)
print("-------------")
choice = input("Enter movie name: ").strip().title()

if choice in booking:
    if booking[choice][1] != 0 :
        print(f"{booking[choice][1]} seats are availabe....!!")
        seats = int(input("enter the number of seats: "))
        if booking[choice][1] >= seats:
            old = booking[choice][1]
            new =  booking[choice][1] - seats
            if( old != new):
                print("Thanks for booking!!")
        else:
            print("Sprry,we are sold out")            
else:
    print("that movie is not available")




