import xml.etree.ElementTree as ET
import VisualArgs

# Access elements and attributes in the XML
namespace = {'ns': 'http://s3.amazonaws.com/doc/2006-03-01/'}

def getParseFileData():
    # Load the XML content from the file
    LeakFile = "CyberEducationCenterLeak.html"

    with open(LeakFile, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Parse the XML content
    root = ET.fromstring(xml_content)

    # Extract information about each <Contents> element
    contents_elements = root.findall('.//ns:Contents', namespaces=namespace)

    return contents_elements

def dirCurrFolders(folder, LeakData):
    folders = []
    index = 0

    for element in LeakData:
        key = element.find('ns:Key', namespaces=namespace).text
        size = element.find('ns:Size', namespaces=namespace).text
        LastModified = element.find('ns:LastModified', namespaces=namespace).text
        if (key.startswith('/'.join(folder)) or len(folder) == 0) and len(key.split("/")) > len(folder) and key.split("/")[len(folder)] not in VisualArgs.getFoldersName(folders):
            folders.append([LastModified, size, key.split("/")[len(folder)]])

    return folders
