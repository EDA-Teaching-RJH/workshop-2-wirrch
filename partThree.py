def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Charge £{charge:.2f}")



def pounds_to_float(d):
    d = float(d.strip("£"))
    return d

def percent_to_float(p):
    p = float(p.strip("%"))/100
    return p

main()
