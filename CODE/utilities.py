def Print_Error(text = None):
    if(text!=None):
        print "Error! <%s>"%(text)
    else:
        print "Error!"

def Select_Menu(options=None,text=None,return_type=int,can_quit = True):




    if(return_type == int):
        for option in options:
            print "%s. %s"%(options.index(option)+1,option)
        if (text != None):
            if (can_quit):
                print "0. Exit\n",text
            else:
                print text
        while True:
            try:
                ops = (range(1,len(options)+1))
                ops.append(0)

                selection = int(raw_input(":> "))

                if(not (selection) in ops):
                    Print_Error("Not Valid Index!")
                    continue
                selection-=1
                break

            except:
                Print_Error("Not Valid Entry")
    elif(return_type==basestring):
        selection = (raw_input(":> "))
    if(can_quit and str(selection) == "-1"):
        exit()
    return selection

def Get_Date():
    import datetime
    date = str(datetime.datetime.now().date().day) + "." + str(datetime.datetime.now().date().month)
    date = datetime.datetime.now()
    date = "{:%d.%m}".format(date)
    return date

def get_files(directories = []):
    import os
    available_files = []

    desktop_dir = os.path.expanduser("~/Desktop")
    directories.append(desktop_dir)
    directories.append(os.getcwd())
    for dir in directories:
        if(os.path.exists(dir)):
            for file in os.listdir(dir):
                if (file.lower().endswith('.asc'))or(file.lower().endswith('.xls')):
                    available_files.append(dir+"/"+file)
    return available_files


def create_directory(dir):
    import os
    print "Creating Directory: '%s'"%dir
    os.makedirs(dir)


def PrintGitHub():
    print ">>GNU GENERAL PUBLIC LICENCE v3.0<<"
    print ">>Developed by Matias Canepa Gonzalez<<"
    print ">>https://github.com/macanepa<<\n"