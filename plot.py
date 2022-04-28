import matplotlib.pyplot as plt
import sys
import json
from datetime import datetime

# Example: /Users/toddmorris/Documents/Scripting/TimeWarrior Exports/timereport.json
# Load the given file path, and open it as a file
reportPath = sys.argv[1]

r = open(reportPath)

# Read the output in as a Python list
reportData = json.load(r)


rDict = {};



# Loop each entry in report
for i in reportData:

    # Look for tag in rDict, add if not present
    tags = i['tags']


    # -- All tags should be in rDict if not there yet. --
    # Determine the amount of time this entry took
    # Times are formatted YYYYMMDDTHHMMSSZ
    # If the event has an 'end',
    if 'end' in i:
            
        startTime = datetime.strptime(i['start'], "%Y%m%dT%H%M%SZ")
        endTime = datetime.strptime(i['end'], "%Y%m%dT%H%M%SZ")
        
        # Get delta between two times
        delta = endTime - startTime
        
        #Convert seconds to hours
        hrs = delta.seconds / 3600

    # Loop the tags for this entry
    for n in range(len(tags)):

        # Skip the first tag, it's always the name of the task
        if n != 0 :
            # Skip the 'next' tag
            if tags[n] != 'next':
                # If this tag is not in the dictionary yet, add it with a property of 0
                if tags[n] not in rDict:
                    rDict[tags[n]] = 0

                # Tag now exists, if it wasn't there
                # Add hours to the current value
                curHrs = rDict[tags[n]]
                rDict[tags[n]] = curHrs + hrs

D = plt.bar(*zip(*rDict.items()))
plt.show()

# print(rDict)


# Make Bar Graph


r.close()
"""
years = range(2000, 2006)
yield_apples = [0.895, 0.91, 0.926, 0.929, 0.931]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(years, oranges)

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")


plt.show()
"""