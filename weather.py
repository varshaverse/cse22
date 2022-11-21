def read_file(filename):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    return lines

def create_dictionary_from_data(filename):
    lines = read_file(filename)
    website_cont = {}

    for i in range(len(lines)):
        items = lines[i].split(",")
        website = items[0]
        email = items[1]
        password = items[2]
        website_cont[website] = [email,password]
    return website_cont

def write_file(filename, website_cont):
    w = open(filename, "w")
    for website in website_cont:
        line = website + "," + website_cont[website][0] + "," + website_cont[website][1]
        w.write(line)
    w.close()

def updatePassword(filename, website, password):
    website_cont = create_dictionary_from_data(filename)
    if website in website_cont:
        if "\n" in website_cont[website][1]:
            website_cont[website][1] = password + "\n"
        else:
            website_cont[website][1] = password
    write_file(filename,website_cont)

if __name__ == "__main__":
    updatePassword("credentials.csv", "Netflix", "abc123")
    lines = read_file("credentials.csv")
    print(lines)

