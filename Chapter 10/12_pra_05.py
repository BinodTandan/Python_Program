class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"The no. of seats of {self.name} available is {self.seats}.")

    def getFare(self):
        print(f"The fare of each seat is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("No seat available")

    def cancelTicket(self):
        self.seats = self.seats + 1
        print(f"The seat has been cancelled!")


janakpur = Train("janakpur Railway",  2, 3000)
janakpur.getStatus()
janakpur.getFare()
janakpur.bookTicket()
janakpur.getStatus()
janakpur.bookTicket()
janakpur.getStatus()
janakpur.bookTicket()
janakpur.cancelTicket()
janakpur.bookTicket()

# gorakpur = Train("Gorakpur Railway", 100, 5000)
# gorakpur.getStatus()
# gorakpur.getFare()
