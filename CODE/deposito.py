
def Deposito():
    import pandas as pd
    from utilities import Print_Error,get_files,Select_Menu,create_directory



    available_file = []

    search_locations = []
    save_location = ""
    main_config = open("CONFIG/MAIN.config")
    for line in main_config:
        if (line.split(';')[0] == "search_location"):
            search_locations.append(line.split(';')[1].strip())
        elif (line.split(';')[0] == "save_location"):
            save_location=line.split(';')[1].strip()

    for file in get_files(search_locations):
        if(file.upper().endswith('.XLS')):
            available_file.append(file)
    file_name = Select_Menu(available_file,"Select a File",return_type=int)
    file_name = available_file[(file_name)]

    if (file_name.upper().endswith(".XLS")):
        print "Importing XLS File!"
        sheet = "LinnerBooking"
        df = pd.read_excel(io=file_name, sheet_name=sheet)

        df = df[['Booking','Deposito','Weight','Tipo Ctr']]
        df['Weight'] = df['Weight']/1000 #Transformar a Tons.

        table = pd.pivot_table(df,values='Weight',aggfunc='count',index='Deposito',columns='Tipo Ctr')

        print table

        import os

        if (save_location == ""):
            print "Saving Output in Program Location!"
        elif (not os.path.exists(save_location)):
            Print_Error("Save Directory Not Found!")
            create_directory(save_location)

        try:
            table.to_excel(save_location+'/file_output.xlsx')
            print "Saved Succesfully"
        except:
            Print_Error("Error with output directory")

    else:
        Print_Error("File not compatible!")