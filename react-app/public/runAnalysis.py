# Sript to run FAIR analysis


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

#Function to calculate threat event frequency
def threatEventFrequency():
    global tefInherent = 0
    if 





#Function to handle all steps of FAIR analysis
def FAIR():
    threatEventFrequency()
    vulnerability()
    primaryLossEventFrequency()
    primaryRisk()
    secondaryLossEventFrequency()
    secondaryRisk()
    overallRisk()
    display()
    
def main()
    print("++++++++++       INITIALIZED     ++++++++++")
    InputTEST()

