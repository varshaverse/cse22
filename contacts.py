def queryContacts(filename, areacode):
    query = []

    f = open(filename,"r")

    contacts = f.readlines()
    f.close()

    for i in range(len(contacts)):
        contacts2 = contacts[i].strip(",")
        c = contacts2.split(",")
        result = int(c[1].split("-")[0])

        if result == areacode:
            query.append(c[0])
    return query
