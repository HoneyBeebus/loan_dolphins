# Script to run FAIR analysis

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                             INPUT AND VARIABLE INSTANTIATION                                                      #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Simple input function for testing purposes
def input_test():

    #padInherent = Probability of Action Deterrence Inherent = cell C36
    #padControls = Probability of Action Deterrence Controls = cell D36
    #rsvInherent = Resistance Strength Vulnerability Inherent = cell G36
    #rsvControls = Resistance Strength Vulnerability Controls = cell H36
    #cfaInherent = Contact Frequency Avoidance Inherent = cell C31
    #cfaControls = Contact Frequency Avoidance Controls = cell D31
    #tcOWASP = Threat Capability OWASP = cell H31
    #slpPer = Secondary Loss Probability % = cell R26
    #plmrInherent = Primary Loss Magnitude Responsive Inherent = cell H21
    #plmrControls = Primary Loss Magnitude Controls = cell I21
    #slmrInherent = Secondary Loss Magnitude Responsive Inherent = cell L21
    #slmrControls = Secondary Loss Magnitude Responsive Controls = cell M21



    d = dict()

    d["padInherent"] = int(input("Probability of Action Deterrence Inherent: "))
    d["padControls"] = int(input("Probability of Action Deterrence Controls: "))
    d["rsvInherent"] = int(input("Resistance Strength Vulnerability Inherent: "))
    d["rsvControls"] = int(input("Resistance Strength Vulnerability Controls: "))
    d["cfaInherent"] = int(input("Contact Frequency Avoidance Inherent: "))
    d["cfaControls"] = int(input("Contact Frequency Avoidance Controls: "))
    d["tcOWASP"] = int(input("Threat Capability OWASP: "))
    d["slpPer"] = int(input("Secondary Loss Probability %: "))
    d["plmrInherent"] = int(input("Primary Loss Magnitude Responsive Inherent: "))
    d["plmrControls"] = int(input("Primary Loss Magnitude Responsive Controls: "))
    d["slmrInherent"] = int(input("Secondary Loss Magnitude Responsive Inherent: "))
    d["slmrControls"] = int(input("Secondary Loss Magnitude Responsive Controls: "))

    return d

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                               LOGIC                                                               #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

def residual(d):

    if d["padInherent"] == 1:
        d["padResidual"] = 1
    elif d["padInherent"] == 2:
        if d["padControls"] == 1 or d["padControls"] == 2:
            d["padResidual"] = 2
        elif d["padControls"] == 3 or d["padControls"] == 4 or d["padControls"] == 5:
            d["padResidual"] = 1
    elif d["padInherent"] == 3:
        if d["padControls"] == 1 or d["padControls"] == 2:
            d["padResidual"] = 3
        elif d["padControls"] == 3 or d["padControls"] == 4:
            d["padResidual"] = 2
        elif d["padControls"] == 5:
            d["padResidual"] = 1
    elif d["padInherent"] == 4:
        if d["padControls"] == 1 or d["padControls"] == 2:
            d["padResidual"] = 4
        elif d["padControls"] == 3:
            d["padResdidual"] = 3
        elif d["padControls"] == 4:
            d["padResidual"] = 2
        elif d["padControls"] == 5:
            d["padResidual"] = 1
    elif d["padInherent"] == 5:
        if d["padControls"] == 1:
            d["padResidual"] = 5
        elif d["padControls"] == 2:
            d["padResidual"] = 4
        elif d["padControls"] == 3:
            d["padResidual"] = 3
        elif d["padControls"] == 4:
            d["padResidual"] = 2
        elif d["padControls"] == 5:
            d["padResidual"] = 1
    
    if d["cfaInherent"] == 1:
        d["cfaResidual"] = 1
    elif d["cfaInherent"] == 2:
        if d["cfaControls"] == 1 or d["cfaControls"] == 2:
            d["cfaResidual"] = 2
        elif d["cfaControls"] == 3 or d["cfaControls"] == 4 or d["cfaControls"] == 5:
            d["cfaResidual"] = 1
    elif d["cfaInherent"] == 3:
        if d["cfaControls"] == 1 or d["cfaControls"] == 2:
            d["cfaResidual"] = 3
        elif d["cfaControls"] == 3 or d["cfaControls"] == 4:
            d["cfaResidual"] = 2
        elif d["cfaControls"] == 5:
            d["cfaResidual"] = 1
    elif d["cfaInherent"] == 4:
        if d["cfaControls"] == 1 or d["cfaControls"] == 2:
            d["cfaResidual"] = 4
        elif d["cfaControls"] == 3:
            d["cfaResdidual"] = 3
        elif d["cfaControls"] == 4:
            d["cfaResidual"] = 2
        elif d["cfaControls"] == 5:
            d["cfaResidual"] = 1
    elif d["cfaInherent"] == 5:
        if d["cfaControls"] == 1:
            d["cfaResidual"] = 5
        elif d["cfaControls"] == 2:
            d["cfaResidual"] = 4
        elif d["cfaControls"] == 3:
            d["cfaResidual"] = 3
        elif d["cfaControls"] == 4:
            d["cfaResidual"] = 2
        elif d["cfaControls"] == 5:
            d["cfaResidual"] = 1
    
    if d["plmrInherent"] == 1:
        d["plmrResidual"] = 1
    elif d["plmrInherent"] == 2:
        if d["plmrControls"] == 1 or d["plmrControls"] == 2:
            d["plmrResidual"] = 2
        elif d["plmrControls"] == 3 or d["plmrControls"] == 4 or d["plmrControls"] == 5:
            d["plmrResidual"] = 1
    elif d["plmrInherent"] == 3:
        if d["plmrControls"] == 1 or d["plmrControls"] == 2:
            d["plmrResidual"] = 3
        elif d["plmrControls"] == 3 or d["plmrControls"] == 4:
            d["plmrResidual"] = 2
        elif d["plmrControls"] == 5:
            d["plmrResidual"] = 1
    elif d["plmrInherent"] == 4:
        if d["plmrControls"] == 1 or d["plmrControls"] == 2:
            d["plmrResidual"] = 4
        elif d["plmrControls"] == 3:
            d["plmrResdidual"] = 3
        elif d["plmrControls"] == 4:
            d["plmrResidual"] = 2
        elif d["plmrControls"] == 5:
            d["plmrResidual"] = 1
    elif d["plmrInherent"] == 5:
        if d["plmrControls"] == 1:
            d["plmrResidual"] = 5
        elif d["plmrControls"] == 2:
            d["plmrResidual"] = 4
        elif d["plmrControls"] == 3:
            d["plmrResidual"] = 3
        elif d["plmrControls"] == 4:
            d["plmrResidual"] = 2
        elif d["plmrControls"] == 5:
            d["plmrResidual"] = 1

    if d["slmrInherent"] == 1:
        d["slmrResidual"] = 1
    elif d["slmrInherent"] == 2:
        if d["slmrControls"] == 1 or d["slmrControls"] == 2:
            d["slmrResidual"] = 2
        elif d["slmrControls"] == 3 or d["slmrControls"] == 4 or d["slmrControls"] == 5:
            d["slmrResidual"] = 1
    elif d["slmrInherent"] == 3:
        if d["slmrControls"] == 1 or d["slmrControls"] == 2:
            d["slmrResidual"] = 3
        elif d["slmrControls"] == 3 or d["slmrControls"] == 4:
            d["slmrResidual"] = 2
        elif d["slmrControls"] == 5:
            d["slmrResidual"] = 1
    elif d["slmrInherent"] == 4:
        if d["slmrControls"] == 1 or d["slmrControls"] == 2:
            d["slmrResidual"] = 4
        elif d["slmrControls"] == 3:
            d["slmrResdidual"] = 3
        elif d["slmrControls"] == 4:
            d["slmrResidual"] = 2
        elif d["slmrControls"] == 5:
            d["slmrResidual"] = 1
    elif d["slmrInherent"] == 5:
        if d["slmrControls"] == 1:
            d["slmrResidual"] = 5
        elif d["slmrControls"] == 2:
            d["slmrResidual"] = 4
        elif d["slmrControls"] == 3:
            d["slmrResidual"] = 3
        elif d["slmrControls"] == 4:
            d["slmrResidual"] = 2
        elif d["slmrControls"] == 5:
            d["slmrResidual"] = 1

    d["rsvResidual"] = max(d["rsvInherent"], d["rsvControls"])

    return (d)

#Function to calculate threat event frequency
def threatEventFrequency(d):
    #Threat Event Frequency variable
    d["tefInherent"] = 0
    
    #temporary variable to hold sum
    temp = d["padInherent"] + d["cfaInherent"]


    if temp < 5:
        d["tefInherent"] = 1
    elif temp == 5:
        d["tefInherent"] = 2
    elif temp == 6:
        d["tefInherent"] = 3
    elif temp == 7:
        d["tefInherent"] = 4
    elif temp > 7:
        d["tefInherent"] = 5
    else:
        print("INVALID OUTPUT FOR THREAT EVENT FREQUENCY")
    
    return d


#Function to calculate vulnerability
def vulnerability(d):
    #vulnerability variable
    d["vulInherent"] = 0

    #temporary variable to hold sum
    temp = d["padInherent"] + d["cfaInherent"]


    if temp < 5:
        d["vulInherent"] = 1
    elif temp == 5:
        d["vulInherent"] = 2
    elif temp == 6:
        d["vulInherent"] = 3
    elif temp == 7:
        d["vulInherent"] = 4
    elif temp > 7:
        d["vulInherent"] = 5
    else:
        print("INVALID OUTPUT FOR VULNERABILITY")
    
    return d

#Function to calculate primary loss event frequency
def primaryLossEventFrequency(d):
    #primary loss event frequency variable
    d["plefInherent"] = 0

    #temporary variable to hold sum
    temp = d["tefInherent"] + d["vulInherent"]

    if temp < 5:
        d["plefInherent"] = 1
    elif temp == 5:
        d["plefInherent"] = 2
    elif temp == 6:
        d["plefInherent"] = 3
    elif temp == 7:
        d["plefInherent"] = 4
    elif temp > 7:
        d["plefInherent"] = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY LOSS EVENT FREQUENCY")

    return d

#Function to calculate primary risk
def primaryRisk(d):
    #primary risk variable
    d["priskInherent"] = 0

    #temporary variable to hold sum
    temp = d["plefInherent"] + d["plmrInherent"]
    
    if temp < 5:
        d["priskInherent"] = 1
    elif temp == 5:
        d["priskInherent"] = 2
    elif temp == 6:
        d["priskInherent"] = 3
    elif temp == 7:
        d["priskInherent"] = 4
    elif temp > 7:
        d["priskInherent"] = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY RISK")

    return d

#Function to calculate secondary loss event frequency
def secondaryLossEventFrequency(d):
    #secondary loss event frequency variable
    d["sLEFInherent"] = 0

    #temporary variable to hold sum
    temp = d["slpPer"] + d["plefInherent"]
    print(temp)

    if temp < 5:
        d["sLEFInherent"] = 1
    elif temp == 5:
        d["sLEFInherent"] = 2
    elif temp == 6:
        d["sLEFInherent"] = 3
    elif temp == 7:
        d["sLEFInherent"] = 4
    elif temp > 7:
        d["sLEFInherent"] = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY LOSS EVENT FREQUENCY")

    return d

#Function to calculate secondary risk
def secondaryRisk(d):
    #secondary risk variable
    d["sriskInherent"] = 0

    #temporary variable to hold sum
    temp = d["sLEFInherent"] + d["slmrInherent"]

    if temp < 5:
        d["sriskInherent"] = 1
    elif temp == 5:
        d["sriskInherent"] = 2
    elif temp == 6:
        d["sriskInherent"] = 3
    elif temp == 7:
        d["sriskInherent"] = 4
    elif temp > 7:
        d["sriskInherent"] = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY RISK")

    return d

#Function to calculate overall risk
def overallRisk(d):
    #overall risk variable
    d["ovrInherent"] = max(d["priskInherent"], d["sriskInherent"])

    """
    if priskInherent == 1 and sriskInherent == 1:
        ovrInherent = 1
    elif priskInherent == 1 and sriskInherent == 2:
        ovrInherent = 2
    elif priskInherent == 1 and sriskInherent == 3:
        ovrInherent = 3
    elif priskInherent == 1 and sriskInherent == 4:
        ovrInherent = 4
    elif priskInherent == 1 and sriskInherent == 5:
        ovrInherent = 5
    elif priskInherent == 2 and sriskInherent == 1:
        ovrInherent = 2
    elif priskInherent == 2 and sriskInherent == 2:
        ovrInherent = 2
    elif priskInherent == 2 and sriskInherent == 3:
        ovrInherent = 3
    elif priskInherent == 2 and sriskInherent == 4:
        ovrInherent = 4
    elif priskInherent == 2 and sriskInherent == 5:
        ovrInherent = 5
    elif priskInherent == 3 and sriskInherent == 1:
        ovrInherent = 3
    elif priskInherent == 3 and sriskInherent == 2:
        ovrInherent = 3
    elif priskInherent == 3 and sriskInherent == 3:
        ovrInherent = 3
    elif priskInherent == 3 and sriskInherent == 4:
        ovrInherent = 4
    elif priskInherent == 3 and sriskInherent == 5:
        ovrInherent = 5
    elif priskInherent == 4 and sriskInherent == 1:
        ovrInherent = 4
    elif priskInherent == 4 and sriskInherent == 2:
        ovrInherent = 4
    elif priskInherent == 4 and sriskInherent == 3:
        ovrInherent = 4
    elif priskInherent == 4 and sriskInherent == 4:
        ovrInherent = 4
    elif priskInherent == 4 and sriskInherent == 5:
        ovrInherent = 5
    elif priskInherent == 5 and sriskInherent == 1:
        ovrInherent = 5
    elif priskInherent == 5 and sriskInherent == 2:
        ovrInherent = 5
    elif priskInherent == 5 and sriskInherent == 3:
        ovrInherent = 5
    elif priskInherent == 5 and sriskInherent == 4:
        ovrInherent = 5
    elif priskInherent == 5 and sriskInherent == 5:
        ovrInherent = 5
    else:
        print("INVALID OUTPUT FOR OVERALL RISK")
    """

    return d

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                TRANSLATION FROM INT TO STRING                                                     #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function for translating primary risk integer values to strings
def translatePrisk(d):
    if d["priskInherent"] == 1:
        print("Primary Risk: INHERENT=Very Low")
    elif d["priskInherent"] == 2:
        print("Primary Risk: INHERENT=Low")
    elif d["priskInherent"] == 3:
        print("Primary Risk: INHERENT=Medium")
    elif d["priskInherent"] == 4:
        print("Primary Risk: INHERENT=High")
    elif d["priskInherent"] == 5:
        print("Primary Risk: INHERENT=Very High")
    else:
        print("ERROR IN PRIMARY RISK TRANSLATION")

#Function for translating secondary risk integer values to strings
def translateSrisk(d):
    if d["sriskInherent"] == 1:
        print("Secondary Risk: INHERENT=Very Low")
    elif d["sriskInherent"] == 2:
        print("Secondary Risk: INHERENT=Low")
    elif d["sriskInherent"] == 3:
        print("Secondary Risk: INHERENT=Medium")
    elif d["sriskInherent"] == 4:
        print("Secondary Risk: INHERENT=High")
    elif d["sriskInherent"] == 5:
        print("Secondary Risk: INHERENT=Very High")
    else:
        print("ERROR IN OVERALL RISK TRANSLATION")

#Function for translating overall risk integer values to strings
def translateOrisk(d):
    if d["ovrInherent"] == 1:
        print("Overall Risk: INHERENT=Very Low")
    elif d["ovrInherent"] == 2:
        print("Overall Risk: INHERENT=Low")
    elif d["ovrInherent"] == 3:
        print("Overall Risk: INHERENT=Medium")
    elif d["ovrInherent"] == 4:
        print("Overall Risk: INHERENT=High")
    elif d["ovrInherent"] == 5:
        print("Overall Risk: INHERENT=Very High")
    else:
        print("ERROR IN PRIMARY RISK TRANSLATION")

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                    DISPLAY FUNCTIONS                                                              #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function for handeling output
def display(d):
    print("                         ")
    print("                         ")
    print("++++++++++       OUTPUT         ++++++++++")
    print("                         ")
    print("                         ")
    print("Probability of Action Deterrence: INHERENT=" + str(d["padInherent"]) + " CONTROLS=" + str(d["padControls"]) + " RESIDUAL=" + str(d["padResidual"]))
    print("Resistance Strength Vulnerability: INHERENT=" + str(d["rsvInherent"]) + " CONTROLS=" + str(d["rsvControls"]) + " RESIDUAL=" + str(d["rsvResidual"]))
    print("Contact Frequency Avoidance INHERENT=" + str(d["cfaInherent"]) + " CONTROLS=" + str(d["cfaControls"]) + " RESIDUAL=" + str(d["cfaResidual"]))
    print("Threat Capability OWASP=" + str(d["tcOWASP"]))
    print("Threat Event Frequency: INHERENT=" + str(d["tefInherent"]))
    print("Vulnerability: INHERENT=" + str(d["vulInherent"]))
    print("Secondary Loss Probability %=" + str(d["slpPer"]))
    print("Primary Loss Event Frequency: INHERENT=" + str(d["plefInherent"]))
    print("Primary Loss Magnitude Responsive INHERENT=" + str(d["plmrInherent"]) + " CONTROLS=" + str(d["plmrControls"]) + " RESIDUAL=" + str(d["plmrResidual"]))
    print("Secondary Loss Magnitude Responsive INHERENT=" + str(d["slmrInherent"]) + " CONTROLS=" + str(d["slmrControls"]) + " RESIDUAL=" + str(d["slmrResidual"]))
    print("Secondary Loss Event Frequency: INHERENT=" + str(d["sLEFInherent"]))
    translatePrisk(d)
    translateSrisk(d)
    translateOrisk(d)

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                      DRIVING FUNCTIONS                                                            #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function to handle all steps of FAIR analysis
def FAIR(d):
    d = residual(d)
    print("[][][][][][][]")
    d = threatEventFrequency(d)
    print("[X][][][][][][]")
    d = vulnerability(d)
    print("[X][X][][][][][]")
    d = primaryLossEventFrequency(d)
    print("[X][X][X][][][][]")
    d = primaryRisk(d)
    print("[X][X][X][X][][][]")
    d = secondaryLossEventFrequency(d)
    print("[X][X][X][X][X][][]")
    d = secondaryRisk(d)
    print("[X][X][X][X][X][X][]")
    d = overallRisk(d)
    print("[X][X][X][X][X][X][X]")

    return d

#Main driving function
def main():
    print("++++++++++       INITIALIZED         ++++++++++")
    d = input_test()
    print("++++++++++       COMPUTING         ++++++++++")
    d = FAIR(d)
    print("++++++++++       COMPLETE!        ++++++++++")
    display(d)

#______________________________________________________________________________________________________________________________________#

main()