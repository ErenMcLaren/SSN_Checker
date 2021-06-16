# SSN_Checker
Purpose: check and analyze if (1) a given SSN is valid and, (2) if valid, extract possibly meaning information from it.

## About
When SSNs were introduced in 1938, their original purpose was to track workers' earnings and assign social security benefits accordingly [[1]](#1). Nowadays, Social Security Numbers (SSN) are a universal, unique identifier number assigned to United States citizens by the Social Security Administration (SSA) [[1]](#1). They have become de facto a means of national identification with extensive public and private sector usage [[2]](#2). Since these numbers are inexorably related to an individual's identity, it is of interest to verify that a given SSN is valid and to whom it corresponds.

Checking for the validity of SSNs is as simple as traversing down a checklist. The structure of an SSN is the following: AAA-GG-SSSS [[1]](#1)[[3]](#3). These three sections are called the "area number," the "group number," and the "serial number" respectively [[1]](#1)[[3]](#3). It can be concluded that, as of August 29, 2020, SSNs are no less and no longer than nine digits long. Furthermore, there are a set of numbers that are unnacceptable as area numbers, these being 000, 666, and 900 to 999 [[3]](#3). It is also not allowed to have a string of all zeroes for the group number and serial number, i.e., AAA-00-SSSS or AAA-GG-0000 are not allowed. There is also a subset of SSNs that have been blacklisted based on their appearance in the media or , the most popular blacklisted SSN being "078-05-1120" [[4]](#4). "219-09-9999" is also not allowed [[4]](#4).

Before June 25, 2011, the area number (AAA) of SSNs used to be a geographic identifier [[1]](#1). Area numbers were assigned by taking the first three digits of the ZIP code of the mailing address on the SSN application [[1]](#1). In this way, the area number roughly increases from Northeast US to Southwest, with 001-003 corresponding to New Hampshire and 545-573 corresponding to California.  

When it comes to analyzing SSNs, the goal is to extract as much information about an individual based on their SSN. At the time of writing this README, approximately nine years have passed since the randomization of SSNs [[3]](#3). It could be possible that, for individuals who are approximately ten-years-old or older, the state of residence to which the SSN refers can be inferred (specifically, their state of residence when their SSN was assigned.) However, it is important that the degree of confidence for be left at "possible." If the SSN belongs to someone approximately nine-years-old or younger, their SSN is affected by the randomization of SSNs in 2011. Since there is no a priori way to know the age of the individual to which the scrubbed SSN belongs, there is no way to determine if the individual's area number refers to their state of residence at the time that they were assigned their SSN. Nonetheless, it is information that can be extracted.

Conversely, it is more likely to ascertain an individual's SSN based on publically-available records. Two researchers at Carnegie Mellon have already performed this experiment [[5]](#5). Their research highlighted, by using the SSA's publically-available database (titled Death Master File) with "...SSNs, names, dates of birth and death, and states of SSN application for individuals whose deaths have been reported to the SSA," that it is possible to accurately guess the first five digits of their SSN (serial number is generated at random) using the information in the database within two attempts [[6]](#6). 

Though there are many implications entailed with writing a program such as this one, its primary function is to verify that a given SSN is a legitimate one, and if it is, guess possible characteristics about a hypothetical individual to which the number corresponds. The program does not include any other executables that use the scrubbed information to perform "doxxing" or other malicious practices. Should somebody choose to use this program for the purpose of social engineering is not the responsibility of those that wrote the program, and anyone with a beginner-level command of Python can write a similar program.

To use this program, construct a new SSN, and then use its `extract()` method:

```python
coolguy = SSN("434576832", verbose = True)
coolguy.extract()
```

## References
<li>
<a id = "1">[1]</a>
Pickett, Carolyn (2009). <a href = "https://www.ssa.gov/policy/docs/ssb/v69n2/v69n2p55.html">"The Story of the Social Security Number"</a>. <i>Social Security Bulletin</i>. Vol. 69 no. 2. United States Social Security Administration. Retrieved August 29, 2020.
</li>

<li>
<a id = "2">[2]</a>
Kouri, Jim (March 9, 2005). <a href = "https://web.archive.org/web/20120629234649/http://www.americanchronicle.com/articles/view/3911">"Social Security Cards: De Facto National Identification"</a>. <i>American Chronicle</i>. Archived from the original on June 29, 2012. Retrieved August 29, 2020.
</li>

<li>
<a id ="3">[3]</a>
<a href = "https://www.ssa.gov/employer/randomization.html">"Social Security Number Randomization"</a>. Social Security Administration. Retrieved August 29, 2020.
</li>

<li>
<a id = "4">[4]</a>
<a href = "https://www.ssa.gov/history/ssn/misused.html">"Social Security Cards Issued by Woolworth"</a>. Social Security Administration. Retrieved August 29, 2020.
</li>

<li>
<a id = "5">[5]</a>
Timmer, John (July 17, 2009). <a href = "https://arstechnica.com/science/2009/07/social-insecurity-numbers-open-to-hacking/">"New algorithm guesses SSNs using date and place of birth".</a> Ars Technica. Retrieved August 29, 2020.
</li>

<li>
<a id = "6">[6]</a>
Acquisti A., Ralph G. (2009) Predicting Social Security numbers from public data <i>PNAS</i> 106 (27) 10975-10980 https://doi.org/10.1073/pnas.0904891106
</li>

## Parenthetical
For how to cite in a Github README.md file: https://stackoverflow.com/a/58693582 
