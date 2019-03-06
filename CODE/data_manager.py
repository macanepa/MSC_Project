def Generate_Pivot_Table(config, file_dir):
    import pandas as pd
    from ASC_Converter import Convert_to_DF

    if (file_dir.upper().endswith(".XLS")):
        print "Importing XLS File!"
        sheet = "CASP"
        df = pd.read_excel(io=file_dir, sheet_name=sheet)
    elif (file_dir.upper().endswith(".ASC")):
        print "Importing ASC File!"
        df = Convert_to_DF(file_dir)

    if (config.service == 'andes' or config.service == 'inca' or config.service == 'string'):
        print "SERVICE:", config.service.upper()

        cols = df.columns
        cols = cols.map(lambda x: x.replace('/', '_') if isinstance(x, (str, unicode)) else x)
        df.columns = cols

        # Apply Filters
        df = df.query('(f_e == "F") & (opr == "MSC")')

        # Create column POD
        df = df.assign(POD="")

        df_ts = []
        if (len(config.pods) > 0):
            for POD in config.pods:

                print "POD: %s -\tQuery :> '%s'" % (POD, config.query[POD])
                if (config.query[POD] != ''):
                    df_t = df.query("%s" % config.query[POD])
                else:
                    df_t = df.copy()
                # CREATE POD FOR SELECTION
                df_t = df_t[['ctrnr', 'POD']]
                df_t['POD'] = POD

                df_ts.append(df_t)

            df_t = pd.concat(df_ts)
            df = df.set_index('ctrnr').join(df_t.set_index('ctrnr'), rsuffix='F')

        # Filter POL
        if (len(config.pols) > 0):
            query = ''
            for pol in config.pols:
                query += '(pol == "%s") | ' % (pol)
            query = query[:-2]
            df = df.query(query)

        # Show only the required container sizes. FIXED. Doesn't depend of config file.
        df = df.loc[(df['sztp'] == '20DV') | (df['sztp'] == '40DV') | (df['sztp'] == '40HC') | (df['sztp'] == '40HR')]

        # Build Pivot Table
        df["wgt"] = pd.to_numeric(df["wgt"])
        table = pd.pivot_table(df, values=config.values[0], index=['pol', 'PODF'],
                               columns=[config.columns[0]], aggfunc=(config.aggfunc[0]))

        # Reorder index
        reindex_list = []
        for pol in config.pols:
            for pod in config.pods:
                reindex_list.append([pol, pod])

        table = table.reindex(tuple(reindex_list))
        table = table.reindex(columns=['20DV', '40DV', '40HC', '40HR'])

        print "\n\n>>> PIVOT TABLE\n\n", table
        Save_To_Excel(table,config)

def Save_To_Excel(table,config):
        from utilities import Get_Date,Print_Error,create_directory,OpenFile
        print "\nSaving to Excel"

        dir=config.destination + '/%s/OUTPUTS/' % (config.service.upper())
        import os
        if(not os.path.exists(dir)):
            Print_Error("Directory Not Found!")
            create_directory(dir)

        try:
            table.to_excel(
                config.destination + '/%s/OUTPUTS/%s %s.xlsx' % (config.service.upper(), config.vessel_name.upper(), Get_Date()))
            print "Saved Successfully"

            table.to_excel('Output.xlsx')
            OpenFile(os.getcwd()+ '/Output.xlsx')

        except:
            Print_Error("Error with output directory")
