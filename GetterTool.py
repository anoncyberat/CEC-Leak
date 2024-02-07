import ParserHelper
import VisualArgs
import requests

DOWNLOADS = "Downloads"
CEC = "https://data.cyber.org.il/"
ROOT = "root:\\"
COMMANDS = ["ls   - list of local dir.", 
            "cd   - enter into another folder.", 
            "get  - Download file from the server, format 'get {index}' - example: 'get 15'.", 
            "link - print the link to the file on the server, format 'link {index}' - example 'link 12'.", 
            "help - list of all exists commands.", 
            "exit - exit from this tool."]
curr_folder = []
dir_folders = ""
command = ""

def main():
    global curr_folder
    Contents = ParserHelper.getParseFileData()
    folders = ParserHelper.dirCurrFolders(curr_folder, Contents)
    while True:
        print(ROOT + '\\'.join(curr_folder))
        command = input("$ ").split(" ")
        match command[0]:
            case "ls":
                i = 0
                for dirData in folders:
                    if not len(dirData[2]):
                        dirData[2] = "."
                    print(i, (4 - len(str(i))) *  " " + dirData[0] + " " + dirData[1] + "\t\t" + dirData[2])
                    i += 1
            case "cd":                
                if len(command) == 2:
                    if command[1] == "..":
                        if len(curr_folder):
                            curr_folder.pop()
                            folders = ParserHelper.dirCurrFolders(curr_folder, Contents)
                    elif command[1] != '.' and command[1] in VisualArgs.getFoldersName(folders) and VisualArgs.getFolderSize(command[1], folders) == '0':
                        curr_folder.append(command[1])
                        folders = ParserHelper.dirCurrFolders(curr_folder, Contents)
                else:
                    print(ROOT + VisualArgs.viewCurrLocation(curr_folder))
            case "get":
                if len(command) == 2 and command[1].isdecimal() and int(command[1]) <= len(folders):
                    url = CEC + '/'.join(curr_folder) + "/" + VisualArgs.getFolderByID(int(command[1]), folders)[2]
                    file_name = VisualArgs.getFolderByID(int(command[1]), folders)[2]

                    # Send a GET request to the URL
                    response = requests.get(url)

                    # Check if the request was successful (status code 200)
                    if response.status_code == 200:
                        # Open a file in binary write mode and write the content of the response
                        with open(DOWNLOADS + "\\" + file_name, 'wb') as f:
                            f.write(response.content)
                        print(f"File [{file_name}] downloaded successfully.")
                    else:
                        print("Failed to download file.")

            case "link":
                if len(command) == 2 and command[1].isdecimal() and int(command[1]) <= len(folders):
                    print(CEC + '/'.join(curr_folder) + "/" + VisualArgs.getFolderByID(int(command[1]), folders)[2])
            case "help":
                print("Commands:")
                print('\n'.join(COMMANDS))
            case "exit":
                exit()            

if __name__ == "__main__":
    main()
