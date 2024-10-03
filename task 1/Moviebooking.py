movies = {
    "Mankatha": {"totalseats": 200, "remainingseats": 200},
    "Veeram": {"totalseats": 200, "remainingseats": 200},
    "Vaalee": {"totalseats": 200, "remainingseats": 200},
    "Amarkalam": {"totalseats": 200, "remainingseats": 200},
    "Billa": {"totalseats": 200, "remainingseats": 200},
    "Dheena": {"totalseats": 200, "remainingseats": 200},
    "Citizen": {"totalseats": 200, "remainingseats": 200},
    "Yennai Arindhaal": {"totalseats": 200, "remainingseats": 200},
    "Varalaaru": {"totalseats": 200, "remainingseats": 200},
    "Arrambam": {"totalseats": 200, "remainingseats": 200},
    "Aasai": {"totalseats": 200, "remainingseats": 200},
    "Villain": {"totalseats": 200, "remainingseats": 200},
    "Vedalam": {"totalseats": 200, "remainingseats": 200},
    "Kadhal Kottai": {"totalseats": 200, "remainingseats": 200},
    "Kadhal Mannan": {"totalseats": 200, "remainingseats": 200}
}
bookings = {}

def bookticket(moviename, seats):  # Book a ticket for an Ajith Movie function
    if moviename in movies:
        if movies[moviename]["remainingseats"] >= seats:
            movies[moviename]["remainingseats"] -= seats
            if moviename in bookings:
                bookings[moviename] += seats
            else:
                bookings[moviename] = seats
            print(f"Successfully booked {seats} seat's for {moviename}.Enjoy your movie time")
        else:
            print(f"Sorry....., only {movies[moviename]['remainingseats']} seat's remaining.")
    else:
        print("Movie not found... please enter the exact name of the Movie ")


def viewmovies(): # View movies function
    print("Available Movies:")
    for movie, details in movies.items():
        print(f"{movie} - remaining Seats: {details['remainingseats']}/{details['totalseats']}")


def viewbookings():  # View  bookings function
    if bookings:
        print("Your Bookings:")
        for movie, seats in bookings.items():
            print(f"{movie}: {seats} seat(s)")
    else:
        print("You have no bookings. first go book your seats")


def cancelbooking(moviename):  # booking  Cancel function
    if moviename in bookings:
        movies[moviename]["remainingseats"] += bookings[moviename]
        print(f"Cancelled booking for {moviename}. {bookings[moviename]} seat's returned to us...")
        del bookings[moviename]
    else:
        print(f"You have no booking for {moviename}. first go book your seats")


def final(): # Final main Function
    while True:
        print("\n--- Thala Ajith Rasigar Mandram ---")
        print("\n--- Movies Ticket Booking ---")
        print("A. View Movies")
        print("B. Book Ticket")
        print("C. View My Bookings")
        print("D. Cancel Booking")
        print("E. Exit")

        choice = input("Enter your choice (A or B or C or D or E) :  ")

        if choice == "A":
            viewmovies()
        elif choice == "B":
            moviename = input("Enter movie name (Available movie names only)  : ")
            seats = int(input("Enter number of seats: "))
            bookticket(moviename, seats)
        elif choice == "C":
            viewbookings()
        elif choice == "D":
            moviename = input("Enter movie name to cancel booking: ")
            cancelbooking(moviename)
        elif choice == "E":
            print("Goodbye have a nice day")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    final()
