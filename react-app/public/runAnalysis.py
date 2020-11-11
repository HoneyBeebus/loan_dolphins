# Sript to run FAIR analysis

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                             INPUT AND VARIABLE INSTANTIATION                                                      #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Simple input function for testing purposes
def InputTEST():

    #padInherent = Probability of Action Deterrence Inherent = cell C36
    global padInherent = input("Probability of Action Deterrence Inherent: ")
    
    #padControls = Probability of Action Deterrence Controls = cell D36
    global padControls = input("Probability of Action Deterrence Controls: ")
    
    #rsvInherent = Resistance Strength Vulnerability Inherent = cell G36
    global rsvInherent = input("Resistance Strength Vulnerability Inherent: ")
    
    #rsvControls = Resistance Strength Vulnerability Controls = cell H36
    global rsvControls = input("Resistance Strength Vulnerability Controls: ")
    
    #cfaInherent = Contact Frequency Avoidance Inherent = cell C31
    global cfaInherent = input("Contact Frequency Avoidance Inherent: ")
    
    #cfaControls = Contact Frequency Avoidance Controls = cell D31
    global cfaControls = input("Contact Frequency Avoidance Controls: ")
    
    #tcOWASP = Threat Capability OWASP = cell H31
    global tcOWASP = input("Threat Capability OWASP: ")
    
    #slpPer = Secondary Loss Probability % = cell R26
    global slpPer = input("Secondary Loss Probability %: ")
    
    #plmrInherent = Primary Loss Magnitude Responsive Inherent = cell H21
    global plmrInherent = input("Primary Loss Magnitude Responsive Inherent: ")
    
    #plmrControls = Primary Loss Magnitude Controls = cell I21
    global plmrControls = input("Primary Loss Magnitude Controls: ")
    
    #slmrInherent = Secondary Loss Magnitude Responsive Inherent = cell L21
    global slmrInherent = input("Secondary Loss Magnitude Responsive Inherent: ")
    
    #slmrControls = Secondary Loss Magnitude Responsive Controls = cell M21
    global slmrControls = input("Secondary Loss Magnitude Responsive Controls: ")

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                               LOGIC                                                               #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function to calculate threat event frequency
def threatEventFrequency():
    #Threat Event Frequency variable
    global tefInherent = 0
    
    #temporary variable to hold sum
    temp = padInherent + cfaInherent

    if temp < 5:
        tefInherent = 1
    elif temp = 5:
        tefInherent = 2
    elif temp = 6:
        tefInherent = 3
    elif temp = 7:
        tefInherent = 4
    elif temp > 7:
        tefInherent = 5
    else:
        print("INVALID OUTPUT FOR THREAT EVENT FREQUENCY")

#Function to calculate vulnerability
def vulnerability():
    #vulnerability variable
    global vulInherent = 0

    #temporary variable to hold sum
    temp = padInherent + cfaInherent

    if temp < 5:
        vulInherent = 1
    elif temp = 5:
        vulInherent = 2
    elif temp = 6:
        vulInherent = 3
    elif temp = 7:
        vulInherent = 4
    elif temp > 7:
        vulInherent = 5
    else:
        print("INVALID OUTPUT FOR VULNERABILITY") 

#Function to calculate primary loss event frequency
def primaryLossEventFrequency():
    #primary loss event frequency variable
    global plefInherent = 0

    #temporary variable to hold sum
    temp = tefInherent + vulInherent

    if temp < 5:
        plefInherent = 1
    elif temp = 5:
        plefInherent = 2
    elif temp = 6:
        plefInherent = 3
    elif temp = 7:
        plefInherent = 4
    elif temp > 7:
        plefInherent = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY LOSS EVENT FREQUENCY")

#Function to calculate primary risk
def primaryRisk():
    #primary risk variable
    global priskInherent = 0

    #temporary variable to hold sum
    temp = plefInherent + plmrInherent
    
    if temp < 5:
        priskInherent = 1
    elif temp = 5:
        priskInherent = 2
    elif temp = 6:
        priskInherent = 3
    elif temp = 7:
        priskInherent = 4
    elif temp > 7:
        priskInherent = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY RISK")

#Function to calculate secondary loss event frequency
def secondaryLossEventFrequency():
    #secondary loss event frequency variable
    global sLEFInherent = 0

    #temporary variable to hold sum
    temp = slpPer + plefInherent

    if temp < 5:
        sLEFInherent = 1
    elif temp = 5:
        sLEFInherent = 2
    elif temp = 6:
        sLEFInherent = 3
    elif temp = 7:
        sLEFInherent = 4
    elif temp > 7:
        sLEFInherent = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY LOSS EVENT FREQUENCY")

#Function to calculate secondary risk
def secondaryRisk():
    #secondary risk variable
    global sriskInherent = 0

    #temporary variable to hold sum
    temp = sLEFInherent + slmrInherent

    if temp < 5:
        sriskInherent = 1
    elif temp = 5:
        sriskInherent = 2
    elif temp = 6:
        sriskInherent = 3
    elif temp = 7:
        sriskInherent = 4
    elif temp > 7:
        sriskInherent = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY RISK")

#Function to calculate overall risk
def overallRisk():
    #overall risk variable
    global ovrInherent = 0

    if priskInherent = 1 and sriskInherent = 1:
        ovrInherent = 1
    elif priskInherent = 1 and sriskInherent = 2:
        ovrInherent = 2
    elif priskInherent = 1 and sriskInherent = 3:
        ovrInherent = 3
    elif priskInherent = 1 and sriskInherent = 4:
        ovrInherent = 4
    elif priskInherent = 1 and sriskInherent = 5:
        ovrInherent = 5
    elif priskInherent = 2 and sriskInherent = 1:
        ovrInherent = 2
    elif priskInherent = 2 and sriskInherent = 2:
        ovrInherent = 2
    elif priskInherent = 2 and sriskInherent = 3:
        ovrInherent = 3
    elif priskInherent = 2 and sriskInherent = 4:
        ovrInherent = 4
    elif priskInherent = 2 and sriskInherent = 5:
        ovrInherent = 5
    elif priskInherent = 3 and sriskInherent = 1:
        ovrInherent = 3
    elif priskInherent = 3 and sriskInherent = 2:
        ovrInherent = 3
    elif priskInherent = 3 and sriskInherent = 3:
        ovrInherent = 3
    elif priskInherent = 3 and sriskInherent = 4:
        ovrInherent = 4
    elif priskInherent = 3 and sriskInherent = 5:
        ovrInherent = 5
    elif priskInherent = 4 and sriskInherent = 1:
        ovrInherent = 4
    elif priskInherent = 4 and sriskInherent = 2:
        ovrInherent = 4
    elif priskInherent = 4 and sriskInherent = 3:
        ovrInherent = 4
    elif priskInherent = 4 and sriskInherent = 4:
        ovrInherent = 4
    elif priskInherent = 4 and sriskInherent = 5:
        ovrInherent = 5
    elif priskInherent = 5 and sriskInherent = 1:
        ovrInherent = 5
    elif priskInherent = 5 and sriskInherent = 2:
        ovrInherent = 5
    elif priskInherent = 5 and sriskInherent = 3:
        ovrInherent = 5
    elif priskInherent = 5 and sriskInherent = 4:
        ovrInherent = 5
    elif priskInherent = 5 and sriskInherent = 5:
        ovrInherent = 5
    else:
        print("INVALID OUTPUT FOR OVERALL RISK")

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                TRANSLATION FROM INT TO STRING                                                     #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function for translating primary risk integer values to strings
def translatePrisk():
    if priskInherent = 1:
        print("Primary Risk: INHERENT=Very Low")
    elif priskInherent = 2:
        print("Primary Risk: INHERENT=Low")
    elif priskInherent = 3:
        print("Primary Risk: INHERENT=Medium")
    elif priskInherent = 4:
        print("Primary Risk: INHERENT=High")
    elif priskInherent = 5:
        print("Primary Risk: INHERENT=Very High")
    else:
        print("ERROR IN PRIMARY RISK TRANSLATION")

#Function for translating secondary risk integer values to strings
def translateSrisk():
    if ovrInherent = 1:
        print("Overall Risk: INHERENT=Very Low")
    elif ovrInherent = 2:
        print("Overall Risk: INHERENT=Low")
    elif ovrInherent = 3:
        print("Overall Risk: INHERENT=Medium")
    elif ovrInherent = 4:
        print("Overall Risk: INHERENT=High")
    elif ovrInherent = 5:
        print("Overall Risk: INHERENT=Very High")
    else:
        print("ERROR IN OVERALL RISK TRANSLATION")

#Function for translating overall risk integer values to strings
def translateOrisk():
    if riskInherent = 1:
        print("Primary Risk: INHERENT=Very Low")
    elif priskInherent = 2:
        print("Primary Risk: INHERENT=Low")
    elif priskInherent = 3:
        print("Primary Risk: INHERENT=Medium")
    elif priskInherent = 4:
        print("Primary Risk: INHERENT=High")
    elif priskInherent = 5:
        print("Primary Risk: INHERENT=Very High")
    else:
        print("ERROR IN PRIMARY RISK TRANSLATION")

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                    DISPLAY FUNCTIONS                                                              #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function for handeling output
def display():
    print("                         ")
    print("                         ")
    print("++++++++++       OUTPUT         ++++++++++")
    print("                         ")
    print("                         ")
    print("Threat Event Frequency: INHERENT=" + tefInherent)
    print("Vulnerability: INHERENT=" + vulInherent)
    print("Primary Loss Event Frequency: INHERENT=" + plefInherent)
    translatePrisk()
    print("Secondary Loss Event Frequency: INHERENT=" + sLEFInherent)
    translateSrisk()
    translateOrisk()

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                      DRIVING FUNCTIONS                                                            #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function to handle all steps of FAIR analysis
def FAIR():
    print("[][][][][][][]")
    threatEventFrequency()
    print("[X][][][][][][]")
    vulnerability()
    print("[X][X][][][][][]")
    primaryLossEventFrequency()
    print("[X][X][X][][][][]")
    primaryRisk()
    print("[X][X][X][X][][][]")
    secondaryLossEventFrequency()
    print("[X][X][X][X][X][][]")
    secondaryRisk()
    print("[X][X][X][X][X][X][]")
    overallRisk()
    print("[X][X][X][X][X][X][X]")

#Main driving function
def main()
    print("++++++++++       INITIALIZED         ++++++++++")
    InputTEST()
    print("++++++++++       COMPUTING         ++++++++++")
    FAIR()
    print("++++++++++       COMPLETE!        ++++++++++")
    display()

#______________________________________________________________________________________________________________________________________#