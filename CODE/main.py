print "Initiating Program..."
from utilities import Select_Menu,Print_Error,PrintGitHub
PrintGitHub()




while True:
    print "\n\n==MAIN MENU=="
    options = ['Calculate Average Weight','Booking\'s Quantity from Deposit']
    selection = Select_Menu(options,"Select Operation",return_type=int)

    if(selection == 0):
        from mean_weight import mean_weight
        mean_weight()

    elif(selection == 1):
        from deposito import Deposito
        Deposito()


    selected_file=None

