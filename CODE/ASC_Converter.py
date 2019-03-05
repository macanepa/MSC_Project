import pandas as pd

def Convert_to_DF(file_name):

    ASC_File = open(file_name)

    df = pd.DataFrame(columns=['ctrnr','opr','pol','pod','dest','sztp','wgt','f/e'])
    temp = []
    for line in ASC_File:
        if(line.startswith("$")):
            continue
        if(line.__contains__("***Refer")):
            break
        line = line.strip()
        # print line
        ctrnr = line[7:18]
        opr = line[19:22]
        pol = line[27:30]
        pod = line[30:33]
        dest = line[39:44]
        sztp = line[44:48]
        wgt = line[48:51]
        fe = line[51]


        # print ctrnr, opr, pol, pod, dest, sztp, wgt, fe
        temp.append({'ctrnr': ctrnr, 'opr': opr, 'pol': pol, 'pod': pod, 'dest': dest, 'sztp': sztp, 'wgt': int(wgt), 'f/e': fe})

    df = df.append(temp, ignore_index=True)
    return df
