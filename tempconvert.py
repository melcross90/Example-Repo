"""
A fucntion to convert celcius temps to fahrenheit
"""

def ctof(ctemp):
    """
    Convert celsius to fahrenheit
    using the formula
    (0°C × 9/5) + 32 = 32°F
    """

    ftemp = (ctemp * 9/5) + 32
    
    return ftemp

def main():
    print(ctof(-40), "should be -40")
    print(ctof(0), "should be 32")


if __name__ == "__main__":
    main()
