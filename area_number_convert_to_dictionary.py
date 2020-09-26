'''
    Creating the dictionary for area number lookup
    - by: github.com/ErenMcLaren
'''

# The table below came from copy/pasting the table here: https://www.ssa.gov/employer/stateweb.htm
initialCopyPasteOfAreaNumberAndStates =  ''' 
001-003	New Hampshire
004-007	Maine
008-009	Vermont
010-034	Massachusetts
035-039	Rhode Island
040-049	Connecticut
050-134	New York
135-158	New Jersey
159-211	Pennsylvania
212-220	Maryland
221-222	Delaware
223-231	Virginia
232	North Carolina
232-236	West Virginia
237-246	Not Issued
247-251	South Carolina
252-260	Georgia
261-267	Florida
268-302	Ohio
303-317	Indiana
318-361	Illinois
362-386	Michigan
387-399	Wisconsin
400-407	Kentucky
408-415	Tennessee
416-424	Alabama
425-428	Mississippi
429-432	Arkansas
433-439	Louisiana
440-448	Oklahoma
449-467	Texas
468-477	Minnesota
478-485	Iowa
486-500	Missouri
501-502	North Dakota
503-504	South Dakota
505-508	Nebraska
509-515	Kansas
516-517	Montana
518-519	Idaho
520	Wyoming
521-524	Colorado
525,585	New Mexico
526-527	Arizona
528-529	Utah
530,680	Nevada
531-539	Washington
540-544	Oregon
545-573	California
574	Alaska
575-576	Hawaii
577-579	District of Columbia
580	Virgin Islands
580-584	Puerto Rico
586	Guam
586	American Samoa
586	Philippine Islands
587-665	Not Issued
667-679	Not Issued
681-690	Not Issued
691-699	Not Issued
700-728	Railroad Board
729-733	Enumeration at Entry
750-772	Not Issued
'''.strip()

    # Initialize the dictionary:
areaNumberAndStateLookupDictionary = {}

    # Initialize the final dictionary:
finalLookupDictionary = {}

    # Add to the dictionary:
for element in initialCopyPasteOfAreaNumberAndStates.split('\n'): # Split on the new lines
    number, state = element.split('\x09') # Split on the stupid tab
    for thing in state:
        areaNumberAndStateLookupDictionary[number] = state
        
    # Reverse the keys and items in the dictionary (want State to be the key):
reversedStateLookupDictionary = {value: key for key, value in areaNumberAndStateLookupDictionary.items()}

        # TWO BIG PROBLEMS IN THE MULTILINE COMMENT:
        # 1.: it has hyphens indicating number ranges
        # 2.: it has commas between two or more numbers

    # Turn the strings 'ABC-DEF' to an array of numbers including and between ABC and DEF:
for key, value in reversedStateLookupDictionary.items():
    if "-" in value:
        initialRangeOfValues = [(lambda integerList: range(integerList[0], integerList[-1] + 1))(list(map(int, value.split('-'))))]
        arrayOfNumbers = [item for number in initialRangeOfValues for item in number]
        finalLookupDictionary[key] = arrayOfNumbers
    elif "," in value:
        splitOnComma = [int(number) for number in value.split(",")]
    else:
        finalLookupDictionary[key] = [int(value)]
print(finalLookupDictionary)