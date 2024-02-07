def getFoldersName(folders):
    return list(map(lambda cfolder: cfolder[2], folders))

def viewCurrLocation(folders):
    return '\\'.join(getFoldersName(folders))


def getFolderSize(name, folders):
    for folder in folders:
        if folder[2] == name:
            return folder[1]
        
def getFolderByID(id, folders):
    i = 0
    for folder in folders:
        if i == id:
            return folder
        i += 1
