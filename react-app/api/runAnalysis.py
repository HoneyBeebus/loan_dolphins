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
    d["tefResidual"] = 0
    
    #temporary variable to hold sum
    temp1 = d["padInherent"] + d["cfaInherent"]
    temp2 = d["padResidual"] + d["cfaResidual"]


    if temp1 < 5:
        d["tefInherent"] = 1
    elif temp1 == 5:
        d["tefInherent"] = 2
    elif temp1 == 6:
        d["tefInherent"] = 3
    elif temp1 == 7:
        d["tefInherent"] = 4
    elif temp1 > 7:
        d["tefInherent"] = 5
    else:
        print("INVALID OUTPUT FOR THREAT EVENT FREQUENCY")

    if temp2 < 5:
        d["tefResidual"] = 1
    elif temp2 == 5:
        d["tefResidual"] = 2
    elif temp2 == 6:
        d["tefResidual"] = 3
    elif temp2 == 7:
        d["tefResidual"] = 4
    elif temp2 > 7:
        d["tefResidual"] = 5
    else:
        print("INVALID OUTPUT FOR THREAT EVENT FREQUENCY")
    
    return d


#Function to calculate vulnerability
def vulnerability(d):
    #vulnerability variable
    d["vulInherent"] = 0
    d["vulResidual"] = 0

    if d["tcOWASP"] == 1:
        if d["rsvInherent"] == 1:
            d["vulInherent"] = 3
        elif d["rsvInherent"] == 2:
            d["vulInherent"] = 2
        elif d["rsvInherent"] == 3:
            d["vulInherent"] = 1
        elif d["rsvInherent"] == 4:
            d["vulInherent"] = 1
        elif d["rsvInherent"] == 5:
            d["vulInherent"] = 1
    elif d["tcOWASP"] == 2:
        if d["rsvInherent"] == 1:
            d["vulInherent"] = 4
        elif d["rsvInherent"] == 2:
            d["vulInherent"] = 3
        elif d["rsvInherent"] == 3:
            d["vulInherent"] = 2
        elif d["rsvInherent"] == 4:
            d["vulInherent"] = 1
        elif d["rsvInherent"] == 5:
            d["vulInherent"] = 1
    elif d["tcOWASP"] == 3:
        if d["rsvInherent"] == 1:
            d["vulInherent"] = 5
        elif d["rsvInherent"] == 2:
            d["vulInherent"] = 4
        elif d["rsvInherent"] == 3:
            d["vulInherent"] = 3
        elif d["rsvInherent"] == 4:
            d["vulInherent"] = 2
        elif d["rsvInherent"] == 5:
            d["vulInherent"] = 1
    elif d["tcOWASP"] == 4:
        if d["rsvInherent"] == 1:
            d["vulInherent"] = 5
        elif d["rsvInherent"] == 2:
            d["vulInherent"] = 5
        elif d["rsvInherent"] == 3:
            d["vulInherent"] = 4
        elif d["rsvInherent"] == 4:
            d["vulInherent"] = 3
        elif d["rsvInherent"] == 5:
            d["vulInherent"] = 2
    elif d["tcOWASP"] == 5:
        if d["rsvInherent"] == 1:
            d["vulInherent"] = 5
        elif d["rsvInherent"] == 2:
            d["vulInherent"] = 5
        elif d["rsvInherent"] == 3:
            d["vulInherent"] = 5
        elif d["rsvInherent"] == 4:
            d["vulInherent"] = 4
        elif d["rsvInherent"] == 5:
            d["vulInherent"] = 3

    if d["tcOWASP"] == 1:
        if d["rsvResidual"] == 1:
            d["vulResidual"] = 3
        elif d["rsvResidual"] == 2:
            d["vulResidual"] = 2
        elif d["rsvResidual"] == 3:
            d["vulResidual"] = 1
        elif d["rsvResidual"] == 4:
            d["vulResidual"] = 1
        elif d["rsvResidual"] == 5:
            d["vulResidual"] = 1
    elif d["tcOWASP"] == 2:
        if d["rsvResidual"] == 1:
            d["vulResidual"] = 4
        elif d["rsvResidual"] == 2:
            d["vulResidual"] = 3
        elif d["rsvResidual"] == 3:
            d["vulResidual"] = 2
        elif d["rsvResidual"] == 4:
            d["vulResidual"] = 1
        elif d["rsvResidual"] == 5:
            d["vulResidual"] = 1
    elif d["tcOWASP"] == 3:
        if d["rsvResidual"] == 1:
            d["vulResidual"] = 5
        elif d["rsvResidual"] == 2:
            d["vulResidual"] = 4
        elif d["rsvResidual"] == 3:
            d["vulResidual"] = 3
        elif d["rsvResidual"] == 4:
            d["vulResidual"] = 2
        elif d["rsvResidual"] == 5:
            d["vulResidual"] = 1
    elif d["tcOWASP"] == 4:
        if d["rsvResidual"] == 1:
            d["vulResidual"] = 5
        elif d["rsvResidual"] == 2:
            d["vulResidual"] = 5
        elif d["rsvResidual"] == 3:
            d["vulResidual"] = 4
        elif d["rsvResidual"] == 4:
            d["vulResidual"] = 3
        elif d["rsvResidual"] == 5:
            d["vulResidual"] = 2
    elif d["tcOWASP"] == 5:
        if d["rsvResidual"] == 1:
            d["vulResidual"] = 5
        elif d["rsvResidual"] == 2:
            d["vulResidual"] = 5
        elif d["rsvResidual"] == 3:
            d["vulResidual"] = 5
        elif d["rsvResidual"] == 4:
            d["vulResidual"] = 4
        elif d["rsvResidual"] == 5:
            d["vulResidual"] = 3

    return d

#Function to calculate primary loss event frequency
def primaryLossEventFrequency(d):
    #primary loss event frequency variable
    d["plefInherent"] = 0
    d["plefResidual"] = 0

    #temporary variable to hold sum
    temp1 = d["tefInherent"] + d["vulInherent"]
    temp2 = d["tefResidual"] + d["vulResidual"]

    if temp1 < 5:
        d["plefInherent"] = 1
    elif temp1 == 5:
        d["plefInherent"] = 2
    elif temp1 == 6:
        d["plefInherent"] = 3
    elif temp1 == 7:
        d["plefInherent"] = 4
    elif temp1 > 7:
        d["plefInherent"] = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY LOSS EVENT FREQUENCY")

    if temp2 < 5:
        d["plefResidual"] = 1
    elif temp2 == 5:
        d["plefResidual"] = 2
    elif temp2 == 6:
        d["plefResidual"] = 3
    elif temp2 == 7:
        d["plefResidual"] = 4
    elif temp2 > 7:
        d["plefResidual"] = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY LOSS EVENT FREQUENCY")

    return d

#Function to calculate primary risk
def primaryRisk(d):
    #primary risk variable
    d["priskInherent"] = 0
    d["priskResidual"] = 0

    #temporary variable to hold sum
    temp1 = d["plefInherent"] + d["plmrInherent"]
    temp2 = d["plefResidual"] + d["plmrResidual"]
    
    if temp1 < 5:
        d["priskInherent"] = 1
    elif temp1 == 5:
        d["priskInherent"] = 2
    elif temp1 == 6:
        d["priskInherent"] = 3
    elif temp1 == 7:
        d["priskInherent"] = 4
    elif temp1 > 7:
        d["priskInherent"] = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY RISK")

    if temp2 < 5:
        d["priskResidual"] = 1
    elif temp2 == 5:
        d["priskResidual"] = 2
    elif temp2 == 6:
        d["priskResidual"] = 3
    elif temp2 == 7:
        d["priskResidual"] = 4
    elif temp2 > 7:
        d["priskResidual"] = 5
    else:
        print("INVALID OUTPUT FOR PRIMARY RISK")

    return d

#Function to calculate secondary loss event frequency
def secondaryLossEventFrequency(d):
    #secondary loss event frequency variable
    d["sLEFInherent"] = 0
    d["sLEFResidual"] = 0

    #temporary variable to hold sum
    temp1 = d["slpPer"] + d["plefInherent"]
    temp2 = d["slpPer"] + d["plefResidual"]

    if temp1 < 5:
        d["sLEFInherent"] = 1
    elif temp1 == 5:
        d["sLEFInherent"] = 2
    elif temp1 == 6:
        d["sLEFInherent"] = 3
    elif temp1 == 7:
        d["sLEFInherent"] = 4
    elif temp1 > 7:
        d["sLEFInherent"] = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY LOSS EVENT FREQUENCY")

    if temp2 < 5:
        d["sLEFResidual"] = 1
    elif temp2 == 5:
        d["sLEFResidual"] = 2
    elif temp2 == 6:
        d["sLEFResidual"] = 3
    elif temp2 == 7:
        d["sLEFResidual"] = 4
    elif temp2 > 7:
        d["sLEFResidual"] = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY LOSS EVENT FREQUENCY")

    return d

#Function to calculate secondary risk
def secondaryRisk(d):
    #secondary risk variable
    d["sriskInherent"] = 0
    d["sriskResidual"] = 0

    #temporary variable to hold sum
    temp1 = d["sLEFInherent"] + d["slmrInherent"]
    temp2 = d["sLEFResidual"] + d["slmrResidual"]

    if temp1 < 5:
        d["sriskInherent"] = 1
    elif temp1 == 5:
        d["sriskInherent"] = 2
    elif temp1 == 6:
        d["sriskInherent"] = 3
    elif temp1 == 7:
        d["sriskInherent"] = 4
    elif temp1 > 7:
        d["sriskInherent"] = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY RISK")

    if temp2 < 5:
        d["sriskResidual"] = 1
    elif temp2 == 5:
        d["sriskResidual"] = 2
    elif temp2 == 6:
        d["sriskResidual"] = 3
    elif temp2 == 7:
        d["sriskResidual"] = 4
    elif temp2 > 7:
        d["sriskResidual"] = 5
    else:
        print("INVALID OUTPUT FOR SECONDARY RISK")

    return d

#Function to calculate overall risk
def overallRisk(d):
    #overall risk variable
    d["ovrInherent"] = max(d["priskInherent"], d["sriskInherent"])
    d["ovrResidual"] = max(d["priskResidual"], d["sriskResidual"])

    return d

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                TRANSLATION FROM INT TO STRING                                                     #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function for translating primary risk integer values to strings
"""
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
"""
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
    print("Threat Event Frequency: INHERENT=" + str(d["tefInherent"]) + " RESIDUAL=" + str(d["tefResidual"]))
    print("Vulnerability: INHERENT=" + str(d["vulInherent"]) + " RESIDUAL=" + str(d["vulResidual"]))
    print("Secondary Loss Probability %=" + str(d["slpPer"]))
    print("Primary Loss Event Frequency: INHERENT=" + str(d["plefInherent"]) + " RESIDUAL=" + str(d["plefResidual"]))
    print("Primary Loss Magnitude Responsive INHERENT=" + str(d["plmrInherent"]) + " CONTROLS=" + str(d["plmrControls"]) + " RESIDUAL=" + str(d["plmrResidual"]))
    print("Secondary Loss Magnitude Responsive INHERENT=" + str(d["slmrInherent"]) + " CONTROLS=" + str(d["slmrControls"]) + " RESIDUAL=" + str(d["slmrResidual"]))
    print("Secondary Loss Event Frequency: INHERENT=" + str(d["sLEFInherent"]) + " RESIDUAL=" + str(d["sLEFResidual"]))
    print("Primary Risk: INHERENT=" + str(d["priskInherent"]) + " RESIDUAL=" + str(d["priskResidual"]))
    print("Secondary Risk: INHERENT=" + str(d["sriskInherent"]) + " RESIDUAL=" + str(d["sriskResidual"]))
    print("Overall Risk: INHERENT=" + str(d["ovrInherent"]) + " RESIDUAL=" + str(d["ovrResidual"]))

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                      TRANSLATING FUNCTIONS                                                            #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
# translate long names to short names
def translate_to_short(d):
    return {
		"cfaInherent": d["contactFrequencyAvoidanceInherent"],
		"cfaControls": d["contactFrequencyAvoidanceControls"],
		"padInherent": d["probabilityOfActionDeterrenceInherent"],
		"padControls": d["probabilityOfActionDeterrenceControls"],
		"tcOWASP": d["threatCapability"],
		"rsvInherent": d["resistanceStrengthVulnerabilityInherent"],
		"rsvControls": d["resistanceStrengthVulnerabilityControls"],
		"plmrInherent": d["primaryLossMagnitudeResponsiveInherent"],
		"plmrControls": d["primaryLossMagnitudeResponsiveControls"],
		"slmrInherent": d["secondaryLossMagnitudeResponsiveInherent"],
		"slmrControls": d["secondaryLossMagnitudeResponsiveControls"],
		"slpPer": d["secondaryLossProbability"]
	}

# translate short names to long names
def translate_to_long(d):
    return {
        "contactFrequencyAvoidanceInherent": d["cfaInherent"],
		"contactFrequencyAvoidanceControls": d["cfaControls"],
		"probabilityOfActionDeterrenceInherent": d["padInherent"],
		"probabilityOfActionDeterrenceControls": d["padControls"],
		"threatCapability": d["tcOWASP"],
		"resistanceStrengthVulnerabilityInherent": d["rsvInherent"],
		"resistanceStrengthVulnerabilityControls": d["rsvControls"],
		"primaryLossMagnitudeInherent": d["plmrInherent"],
		"primaryLossMagnitudeControls": d["plmrControls"],
		"secondaryLossMagnitudeInherent": d["slmrInherent"],
		"secondaryLossMagnitudeControls": d["slmrControls"],
		"secondaryLossProbabilty": d["slpPer"],
        # new
        "probabilityOfActionDeterrenceResidual": d["padResidual"],
        "contactFrequencyAvoidanceResidual": d["cfaResidual"],
        "primaryLossMagnitudeResidual": d["plmrResidual"],
        "secondaryLossMagnitudeResidual": d["slmrResidual"],
        "threatEventFrequencyInherent": d["tefInherent"],
        "threatEventFrequencyResidual": d["tefResidual"],
        "vulnerabilityInherent": d["vulInherent"],
        "vulnerabilityResidual": d["vulResidual"],
        "primaryLossEventFrequencyInherent": d["plefInherent"],
        "primaryLossEventFrequencyResidual": d["plefResidual"],
        "primaryRiskInherent": d["priskInherent"],
        "primaryRiskResidual": d["priskResidual"],
        "secondaryLossEventFrequencyInherent": d["sLEFInherent"],
        "secondaryLossEventResidual": d["sLEFResidual"],
        "secondaryRiskInherent": d["sriskInherent"],
        "secondaryRiskResidual": d["sriskResidual"],
        "overallRiskInherent": d["ovrInherent"],
        "overallRiskResidual": d["ovrResidual"]
    }

#___________________________________________________________________________________________________________________________________#

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#
#                                                      DRIVING FUNCTIONS                                                            #
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-#

#Function to handle all steps of FAIR analysis
def FAIR(d):
    d = translate_to_short(d)
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
    d = translate_to_long(d)
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

if __name__ == '__main__':
    main()