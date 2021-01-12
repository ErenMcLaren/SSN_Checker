class SSN:
    
    def __init__(self, SSN, verbose = False):
        
        self.prospectiveSSN   = SSN
        self.isLegitimateSSN  = False
        self.trueSSN          = None
        self.area_number      = None
        self.group_number     = None
        self.serial_number    = None
        self.formattedSSN     = None
        self.hasScrubbed      = False
        self.blacklisted      = [
                                "072051120", #FWWoolworthAdvertisedSSN
                                "219099999" #SSNAdvertisementPamplhet
                                ]
        self.verbose          = verbose
        self.state_lookup     = {
                                'New Hampshire': [1, 2, 3], 
                                'Maine': [4, 5, 6, 7], 
                                'Vermont': [8, 9], 
                                'Massachusetts': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34], 
                                'Rhode Island': [35, 36, 37, 38, 39], 
                                'Connecticut': [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], 
                                'New York': [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134], 
                                'New Jersey': [135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158], 
                                'Pennsylvania': [159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211], 
                                'Maryland': [212, 213, 214, 215, 216, 217, 218, 219, 220], 
                                'Delaware': [221, 222], 
                                'Virginia': [223, 224, 225, 226, 227, 228, 229, 230, 231], 
                                'North Carolina': [232], 
                                'West Virginia': [232, 233, 234, 235, 236], 
                                'Not Issued': [750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772], 
                                'South Carolina': [247, 248, 249, 250, 251], 
                                'Georgia': [252, 253, 254, 255, 256, 257, 258, 259, 260], 
                                'Florida': [261, 262, 263, 264, 265, 266, 267], 
                                'Ohio': [268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302], 
                                'Indiana': [303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317], 
                                'Illinois': [318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361], 
                                'Michigan': [362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386], 
                                'Wisconsin': [387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399], 
                                'Kentucky': [400, 401, 402, 403, 404, 405, 406, 407], 
                                'Tennessee': [408, 409, 410, 411, 412, 413, 414, 415], 
                                'Alabama': [416, 417, 418, 419, 420, 421, 422, 423, 424], 
                                'Mississippi': [425, 426, 427, 428], 
                                'Arkansas': [429, 430, 431, 432], 
                                'Louisiana': [433, 434, 435, 436, 437, 438, 439], 
                                'Oklahoma': [440, 441, 442, 443, 444, 445, 446, 447, 448], 
                                'Texas': [449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467],
                                'Minnesota': [468, 469, 470, 471, 472, 473, 474, 475, 476, 477], 
                                'Iowa': [478, 479, 480, 481, 482, 483, 484, 485], 
                                'Missouri': [486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500], 
                                'North Dakota': [501, 502], 
                                'South Dakota': [503, 504], 
                                'Nebraska': [505, 506, 507, 508], 
                                'Kansas': [509, 510, 511, 512, 513, 514, 515], 
                                'Montana': [516, 517], 
                                'Idaho': [518, 519], 
                                'Wyoming': [520], 
                                'Colorado': [521, 522, 523, 524], 
                                'Arizona': [526, 527], 
                                'Utah': [528, 529], 
                                'Washington': [531, 532, 533, 534, 535, 536, 537, 538, 539], 
                                'Oregon': [540, 541, 542, 543, 544], 
                                'California': [545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573], 
                                'Alaska': [574], 
                                'Hawaii': [575, 576], 
                                'District of Columbia': [577, 578, 579], 
                                'Virgin Islands': [580], 
                                'Puerto Rico': [580, 581, 582, 583, 584], 
                                'Philippine Islands': [586], 
                                'Railroad Board': [700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728], 
                                'Enumeration at Entry': [729, 730, 731, 732, 733]
                                }
        
    def extract(self):
        step_one = self.primary_scrub()
        if not step_one:
            self.hasScrubbed = True
            return
        step_two = self.get_SSN_length()
        if not step_two:
            self.hasScrubbed = True
            return
        step_three = self.check_blacklist_SSNs()
        if not step_three:
            self.hasScrubbed = True
            return
        step_four = self.collect_number_info()
        step_five = self.scrub_area_number()
        if not step_five:
            self.hasScrubbed = True
            return
        step_six = self.scrub_group_number()
        if not step_six:
            self.hasScrubbed = True
            return
        step_seven = self.scrub_serial_number()
        if not step_seven:
            self.hasScrubbed = True
            return
        self.analyze_area_number()
        if self.verbose:
            print(f"{self.prospectiveSSN} has finished scrubbing.")
        return True
        
    def primary_scrub(self):
        if (len(str(self.prospectiveSSN)) >= 10):
            if self.verbose: print("ERROR: That's not an SSN you're entering... Try again.")
            return False
        else:
            if self.verbose: print(f"{self.prospectiveSSN} passed initial scrub.")
            return True
        
    def ensure_true_SSN(self):
        if not self.isLegitimateSSN:
            return False
        else:
            return True
        
    def get_SSN_length(self):
        if len(str(self.prospectiveSSN)) != 9:
            self.isLegitimateSSN = False
            if self.verbose: print(f"ERROR: {self.prospectiveSSN} is not 9 digits long.")        
        else:
            self.isLegitimateSSN = True
            self.trueSSN = str(self.prospectiveSSN)
            if self.verbose: print(f"{self.prospectiveSSN} passed 9-digit criteron.")
            return True
    
    def collect_number_info(self):
        if not self.ensure_true_SSN():
            return
        else:
            self.area_number, self.group_number, self.serial_number = self.trueSSN[0:3], self.trueSSN[3:5], self.trueSSN[5:9]
            if self.verbose:
                print(f"{self.trueSSN} has AAA = {self.area_number}, GG = {self.group_number}, SSSS = {self.serial_number}")
        return self
    
    def check_blacklist_SSNs(self):
        if not self.ensure_true_SSN():
            return
        else:
            for item in self.blacklisted:
                if self.trueSSN == item:
                    if self.verbose:
                        print(f"ERROR: SSN matched blacklisted SSN -> {item}.")
            if self.verbose:
                print(f"{self.trueSSN} did not match blacklisted SSNs.")
            return True
        
    def scrub_area_number(self):
        if not self.ensure_true_SSN():
            return
        else:
            for number in range(900, 1000):
                if (self.area_number == str(number)):
                    if self.verbose:
                        print(f"ERROR: Area number of '{self.area_number}' now allowed in SSNs.")
                        return False
            if (self.area_number == "000") or (self.area_number == "666"):
                if self.verbose:
                    print(f"ERROR: Area number of '{self.area_number}' cannot be either 000 or 666.")
                    return False
            else:
                if self.verbose:
                    print(f"{self.trueSSN} passed area number requirement: Area number did not match blacklisted area numbers.")
                return True
        
    def scrub_group_number(self):
        if not self.ensure_true_SSN():
            return
        else:
            if self.group_number == "00":
                if self.verbose:
                    print(f"ERROR: Group number of '00' not allowed in SSNs.")
                    return False
            else:
                if self.verbose:
                    print(f"{self.trueSSN} passed group number requirement: Group number was not '00'.")
                return True

    def scrub_serial_number(self):
        if not self.ensure_true_SSN():
            return
        else:
            if self.serial_number == "0000":
                if self.verbose:
                    print(f"ERROR: Serial number of '0000' not allowed in SSNs.")
                    return False
            else:
                if self.verbose:
                    print(f"{self.trueSSN} passed serial number requirement: Serial number was not '0000'.")
                return True
            
    def analyze_area_number(self):
        if not self.ensure_true_SSN():
            return
        else:
            for state, arrayOfNumbers in self.state_lookup.items():
                for item in arrayOfNumbers:
                    if int(self.area_number) == item:
                        if self.verbose:
                            print(f"{self.trueSSN} has AAA = {self.area_number} which corresponds to {state}.")
                        return True
                
