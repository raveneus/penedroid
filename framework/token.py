def getToken(line):
    token = ""
    for letter in line:
        if letter != " ":
            token += letter
        else:
            break
    return token
