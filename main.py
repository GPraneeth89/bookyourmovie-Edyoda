from bym import *
if __name__ == "__main__":
   
       
    r_o,c_o=map(int,input("Enter row and col with space").split())
    a_obj=BYM(r_o,c_o)
    while True:

        print("1.Show the seats")
        print("2. Buy a Ticket")
        print("3. Statistics")
        print("4.Show Booked Tickets User Info")
        print("0. Exit")
        b_in=input("Choose an option")

        if b_in=="1":
            a_obj.show()
        elif b_in=="2":
            b_r,b_c=map(int,input("ENter booking seat").split())
            li={}
            a_list=['Name','Gender','Age','Phone']
            for i in range(4):
                li[a_list[i]]=input(a_list[i])
            try:
                a_obj.bookSeat(b_r,b_c,li)
            except IndexError as e:
                print("Seat Number not available")

        elif b_in=='3':
            a_obj.stats()

        elif b_in=='4':
            a_obj.showbok(input("Enter row and col without space"))

        elif b_in=='0':
            break

       
        

            

