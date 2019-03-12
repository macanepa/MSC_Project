
def mean_weight():
    import pandas as pd
    from config import Config,get_services,recreate_config_file
    import sys
    from utilities import Print_Error, Select_Menu, get_files
    from data_manager import Generate_Pivot_Table

    # pd.set_option('display.max_rows',3000)

    available_services = get_services()
    available_files = get_files()

    if(len(available_services) == 0):
        Print_Error(".config File Not Found! Recreating .config File!")
        recreate_config_file()
        return

    # Use parameters from command prompt

    if(len(sys.argv) == 1):

        file_name = Select_Menu(available_files,text="Input File Name",return_type=int)
        service = Select_Menu(available_services,text="Input Service",return_type=int)
        file_name = available_files[(file_name)]
        service = available_services[(service)]

    vessel_name = file_name.upper().split('/')[-1].rsplit('.',1)[0]
    config = Config()
    import os
    config.build_config("%s/CONFIG/%s.config"%(os.getcwd(),service.upper()))
    config.set_vessel(vessel_name.rsplit('.',1)[0])
    config.print_data()

    Generate_Pivot_Table(config,file_name)

