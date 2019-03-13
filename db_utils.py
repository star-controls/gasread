
from softioc.builder import aIn

#_____________________________________________________________________________
def db_load(dbname):
    #load original TOF and TPC database
    #dictionary for analog input PVs
    pvs = {}
    #fields from the orignal database to be loaded
    flist = ["PREC", "HOPR", "LOPR", "HIHI", "LOLO", "HIGH", "LOW"]
    flist_str = ["HHSV", "LLSV", "HSV", "LSV", "EGU"]
    f = open(dbname, "r")
    ll = [x for x in f]
    f.close()
    while ll != []:
        line = ll.pop(0)
        if line.find("record") >= 0:
            #get record name
            pvnam = get_field(line, "\"", "\"")
            pvs[pvnam] = aIn(pvnam)
            while True:
                #get fields for the record
                line = ll.pop(0).strip()
                if line == "}": break
                if line.find("field") < 0: continue
                #name and value for the field
                fnam = get_field(line, "(", ",")
                if fnam not in flist and fnam not in flist_str: continue
                fval = get_field(line, "\"", "\"")
                #put '"' characters for string-valued fields
                if fnam in flist_str: fval = "\""+fval+"\""
                #set the field for the record
                exec("pvs.get(\""+pvnam+"\")."+fnam+"="+fval)

    #put the complete PV dictionary to the caller
    return pvs

#_____________________________________________________________________________
def get_field(inp, c1, c2):
    inp = inp[inp.find(c1)+1:]
    inp = inp[:inp.find(c2)]
    return inp




