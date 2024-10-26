class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall = hall
        self.hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self.__seats = {}
        self.__show_list = []
        Star_Cinema().entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        self.__show_list.append((show_id, movie_name, time))
        self.__seats[show_id] = [[0 for x in range(self._cols)] for x in range(self._rows)]

    def book_seats(self, show_id, ticket_cunt):
        if show_id not in self.__seats:
            print("Invalid Show ID!")
            return

        for x in range(ticket_cunt):
            row = int(input("Enter seat row: "))
            col = int(input("Enter seat col: "))
            
            if row < self._rows and col < self._cols:
                if self.__seats[show_id][row][col] == 0:
                    self.__seats[show_id][row][col] = 1
                    print(f"Seat ({row}, {col}) booked successfully!. Booked for show ID: {show_id}")
                else:
                    print(f"Seat ({row}, {col}) is already booked!!")
            else:
                print("Invalid seat number.")        
            
            
    def view_show_list(self):
        print("\nShows:")
        print("..........................................................")
        for show in self.__show_list:
            print(f"Show ID: {show[0]} , Movie: {show[1]} , Time: {show[2]}")
        print("..........................................................")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid Show ID!?")
            return

        print(f"\nSeat available for Show ID: {show_id}")
        seat = self.__seats[show_id]
        for x in seat:
            print(x)



hall = Hall(6, 6, 50)

hall.entry_show(510, 'Badsha', '26/10/2024 04:30 PM')
hall.entry_show(511, 'Boss', '26/10/2024 10:00 AM')
hall.entry_show(512, 'Love', '27/10/2024 05:00 PM')

print("************** WELCOME **************")
while True:
    print("Menu:")
    print("1. View All Shows Today")
    print("2. View Available Seats")
    print("3. Book Tickets")
    print("4. Exit")
    
    op = int(input("Enter option: "))
    if op == 1:
        hall.view_show_list()
    elif op == 2:
        show_id = int(input("Enter Show ID: "))
        hall.view_available_seats(show_id)
    elif op == 3:
        show_id = int(input("Enter Show ID: "))
        ticket_cunt = int(input("Enter number of ticket: "))
        hall.book_seats(show_id, ticket_cunt)
    elif op == 4:
        print("Thank you.")
        break
    else:
        print("Invalid option!")


# DONE 