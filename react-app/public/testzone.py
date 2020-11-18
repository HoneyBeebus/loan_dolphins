def dict_pop():
    dict = {
        # padInherent = Probability of Action Deterrence Inherent = cell C36
        "padInherent": input("Probability of Action Deterrence Inherent: "),
        # padControls = Probability of Action Deterrence Controls = cell D36
        "padControls": input("Probability of Action Deterrence Controls: "),
        # rsvInherent = Resistance Strength Vulnerability Inherent = cell G36
        "rsvInherent": input("Resistance Strength Vulnerability Inherent: "),
        # rsvControls = Resistance Strength Vulnerability Controls = cell H36
        "rsvControls": input("Resistance Strength Vulnerability Controls: "),
        # cfaInherent = Contact Frequency Avoidance Inherent = cell C31
        "cfaInherent": input("Contact Frequency Avoidance Inherent: "),
        # cfaControls = Contact Frequency Avoidance Controls = cell D31
        "cfaControls": input("Contact Frequency Avoidance Controls: "),
        # tcOWASP = Threat Capability OWASP = cell H31
        "tcOWASP": input("Threat Capability OWASP: "),
        # slpPer = Secondary Loss Probability % = cell R26
        "slpPer": input("Secondary Loss Probability %: "),
        # plmrInherent = Primary Loss Magnitude Responsive Inherent = cell H21
        "plmrInherent": input("Primary Loss Magnitude Responsive Inherent: "),
        # plmrControls = Primary Loss Magnitude Controls = cell I21
        "plmrControls": input("Primary Loss Magnitude Controls: "),
        # slmrInherent = Secondary Loss Magnitude Responsive Inherent = cell L21
        "slmrInherent": input("Secondary Loss Magnitude Responsive Inherent: "),
        # slmrControls = Secondary Loss Magnitude Responsive Controls = cell M21
        "slmrControls": input("Secondary Loss Magnitude Responsive Controls: ")
    }

    return dict

def main():
    dict = dict_pop()
    print(dict)
