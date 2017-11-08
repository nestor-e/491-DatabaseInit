

def combineLineNum(part, num):
    return part + ":" + num

def parseNameId(stringId):
    return stringId.split("_")[1]




def readName(line):
    parts = line.split(",")
    nameData = {
        "Type":(1 if parts[0] == "PN" else 2),
        "Name":parts[4],
        "NameId":parseNameId(parts[5]),
        "Count": int( parts[3] ),
        "NormNameId":parseNameId(parts[2]),
        "NormName":parts[1]
    }
    return nameData

def readText(line):
    parts = line.split(",")
    nameData = {
        "TabletId":parts[0],
        "Source":parts[1],
        "Date":parts[2],
        "Seal": parts[3],
        "Line":combineLineNum(parts[5], parts[6]),
        "Text":parts[7]
    }
    return nameData

def readAttestation(line):
    parts = line.split(",")
    data = {
        "TabletId":parts[0],
        "Line":combineLineNum(parts[2], parts[3]),
        "NameId":parseNameId(parts[6])
    }
    return data



def main():
    fNames = open("Names.csv", "r", encoding="utf-8")
    next(fNames)
    fTexts = open("Texts.csv", "r", encoding="utf-8")
    next(fTexts)
    fAttest = open("Attestations.csv", "r", encoding="utf-8")
    next(fAttest)



    tableTablet = {}
    tableName = {}
    tableLine = []
    tableAttestation = []

    for line in fNames:
        data = readName(line.strip())
        tableName[data["NameId"]] = data

    for line in fTexts:
        data = readText(line.strip())
        if data["TabletId"] not in tableTablet:
            tableTablet[data["TabletId"]] = {
                "TabletId" : data["TabletId"],
                "Source" : data["Source"],
                "Date" : data["Date"],
                "Seal" : data["Seal"]
            }
        if data["Text"] != "":
            tableLine.append({
                "TabletId" : data["TabletId"],
                "Line" : data["Line"],
                "Text" : data["Text"]
            })


    for line in fAttest:
        data = readAttestation(line.strip())
        if data["TabletId"] in tableTablet and data["NameId"] in tableName:
            tableAttestation.append(data)

    fNames.close()
    fTexts.close()
    fAttest.close()

    fOut = open("TabletTable.txt", "w", encoding="utf-8")
    for key in tableTablet:
        d = tableTablet[key]
        print(d["TabletId"], d["Date"], d["Source"], d["Seal"], sep="\t", file=fOut)
    fOut.close()

    fOut = open("NameTable.txt", "w", encoding="utf-8")
    for key in tableName:
        d = tableName[key]
        print(d["NameId"], d["Type"], d["Name"], d["NormNameId"], d["NormName"], sep="\t", file=fOut)
    fOut.close()


    fOut = open("LineTable.txt", "w", encoding="utf-8")
    for d in tableLine:
        print(d["TabletId"], d["Line"], d["Text"], sep="\t", file=fOut)
    fOut.close()

    fOut = open("AttestationTable.txt", "w", encoding="utf-8")
    for d in tableAttestation:
        print(d["TabletId"], d["NameId"], d["Line"], sep="\t", file=fOut)
    fOut.close()

main()
