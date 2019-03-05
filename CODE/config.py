
class Config:

    def __init__(self):
        self.service =""
        self.filters = {}
        self.rows = ""
        self.columns =""
        self.aggfunc =""
        self.values = ""    
        self.destination = ""
        self.pols = []
        self.pods = []
        self.vessel_name = ""


        # self.query = {'CALLAO' : 'pod == "CLL"',
        #               'MEXICO' : '(pod == "ZLO") & (dest.str.contains("MX"))',
        #               'USW' : '(pod == "ZLO") & ~(dest.str.contains("MX"))',
        #               'FAREAST' : '~(pod =="ZLO") & ~(pod =="CLL")'}
        self.query = {}

    def print_data(self):
        print ("=== Config File ===")
        print "SERVICE:",self.service
        print "VESSEL NAME:",self.vessel_name
        print "FILTERS:",self.filters
        print "PODS:",self.pods
        print "COLUMNS:",self.columns
        print "VALUES:",self.values
        print "AGGFUNC:",self.aggfunc
        print "DESTINATION:", self.destination
        print "POLS:",self.pols
        print "QUERY:",self.query

        print "\n"

    def build_config_test(self,config_dir="ANDES.config"):

        config_file = open(config_dir, "r")
        config_data = []
        for line in config_file:
            line = line.replace(":",";").strip()
            if (line==""):
                continue
            line = line.split(";")
            config_data.append(line[1:])
        config_file.close()

        self.service = config_data[0][0]
        for filter in config_data[1]:
            self.filters[filter.split()[0]]=filter.split()[1]
        self.rows = config_data[2]
        self.columns = config_data[3]
        self.values = config_data[4]
        self.aggfunc = config_data[5]
        self.destination = config_data[6][0]


    def build_config(self,config_dir = "ANDES.config"):
        config_file = open(config_dir,"r")
        for line in config_file:
            # data = line.strip().replace(":",";").split(";")
            data = line.strip().split(';')
            if (data[0] == "service"):
                self.service = data[1]
            elif (data[0] == "columns"):
                self.columns = data[1:]
            elif (data[0] == "values"):
                self.values = data[1:]
            elif (data[0] == "aggfunc"):
                self.aggfunc = data[1:]
            elif (data[0] == "destination"):
                self.destination = data[1]
            elif (data[0] == "pol"):
                self.pols = data[1].split()

            elif (data[0] == "filters"):
                for filter in data[1:]:
                    self.filters[filter.split()[0]]=filter.split()[1]



            elif (data[0] == "row"):
                if not(data[0] in self.pods):
                    self.pods.append(data[1])
                query = ''
                for instrucction in data[2:]:
                    inst = instrucction.split()
                    if (inst[0] == 'pod'):
                        for pod in inst[1:]:
                            if (pod[0] == "-"):
                                query += "~"
                                pod = pod[1:]
                            if (pod[0] == "%"):
                                pod=pod[1:]
                                query += '(pod.str.contains("%s")) & ' % pod
                            else:
                                query += '(pod == "%s") & ' % pod


                    if (inst[0] == 'dest'):
                        for pod in inst[1:]:
                            if(pod[0] == "-"):
                                query+="~"
                                pod = pod[1:]
                            if(pod[0] == "%"):
                                pod = pod[1:]
                                query += '(dest.str.contains("%s")) & ' % pod
                            else:
                                query += '(dest == "%s") & ' % pod

                query = query[:-2] #Removes last &
                self.query[data[1]] = query

    def set_vessel(self,vessel_name):
        self.vessel_name = vessel_name



def get_services():
    import os
    available_services = []
    for file in os.listdir(os.curdir+"/CONFIG"):
        if file.lower().endswith('.config'):
            available_services.append(file.strip('.config'))

    if ('SERVICE_NAME' in available_services):
        available_services.remove('SERVICE_NAME')
    if ('MAIN' in available_services):
        available_services.remove('MAIN')

    return available_services




def recreate_config_file():
    config_file = open("SERVICE_NAME.config","w")
    config_file.write("""service:SERVICE_NAME
filters;opr MSC;f/e F
columns;sztp
values;wgt
aggfunc;mean
destination;/home/matias/Desktop/PESO_PROMEDIO

pol;SAI CNL LQN PAG
row;FAREAST;pod -CLL -ZLO
row;MEXICO;pod ZLO;dest %MX
row;USW;pod ZLO;dest -%MX
row;CALLAO;pod CLL""")
    config_file.close()
    print ".config recreation completed successfully.\nPlease edit this file to match the desired service.\n"
