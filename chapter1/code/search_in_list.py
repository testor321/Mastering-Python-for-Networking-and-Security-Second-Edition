"""
In this example, we can see the code for finding the location of a given element inside a list. We use the range
function to get elements inside protocolList and we compare each element with the element to find. When both elements
are equal, we break the loop and return the element.
"""
protocolList = ["FTP", "HTTP", "SNMP", "SSH"]
toFind = "SSH"
found = False
elem = 0
for elem in range(len(protocolList)):
    found = protocolList[elem] == toFind
    if found:
        break
if found:
    print("Element found at index", elem)
else:
    print("Element not found")
