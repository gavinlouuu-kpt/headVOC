# Ideal Gas (L*atm/mol*K)
R = 0.0821

# Temperature (K)
K = 298.15

# Total pressure (atm)
tATM = 1

# i.e., VOC diluted in water
h_2oRho = 1000 # density of water (g/L)
h_2oMW = 18.01528 # molecular weight of water (g/mol)
h_2oVP = 0.0313 # vapor pressure of acetone (atm) at 25 Degree C

h_20Vol = 0.05 # volume of water (L)

def PPMtoConcMole(ppm, mw):
    # Convert concentration (ppm) to (mg/m^3) and to mol/L
    mgm3 = ppm / 1000000
    Conc = mgm3 / mw
    return Conc

def concToPP(Conc, R, K):
    # Convert concentration (moles) to partial pressure with ideal gas constant (L*atm/mol*K) and temperature (K)
    VPP = Conc * R * K
    return VPP

def molFractionPP(VPP, VP, tATM):
    # Convert partial pressure to mole fraction with total pressure (atm)
    X = VPP / (VP/tATM)
    return X

def volToMass(vol, rho):
    g = vol * rho
    return g

def massToMoles(mass, mw):
    n = mass / mw
    return n

def VPPtoMoleFraction(VPP, VP, tATM):
    # Convert partial pressure to mole fraction with total pressure (atm)
    X = VPP / (VP/tATM)
    return X

def molFractionToMole(X, n2):
    # Calculate moles of the volatile compound with mole fraction and total moles of the volatile compound
    n1 = (X * n2)/(1-X)
    return n1

def volToMole(vol, rho, mw):
    # Convert volume (L) to moles with density (g/L) and molecular weight (g/mol)
    # used to calculate water mole with a given volume
    mass = volToMass(vol, rho)
    moles = massToMoles(mass, mw)
    return moles
    
def moleToMass(n, mw):
    # Convert moles to mass with molecular weight (g/mol)
    mass = n * mw
    return mass

def massToVol(mass, rho):
    # Convert mass to volume with density (g/L)
    vol = mass / rho
    return vol

def main():
    # Calculate amount of acetone required to reach 1PPM with 50ml of water
    # Calculate moles of water in the system
    h_2oMoles = volToMole(h_20Vol, h_2oRho, h_2oMW)

    # Acetone
    aRho = 791 # density of acetone (g/L)
    aMW = 58.08 # molecular weight of acetone (g/mol)
    aVP = 0.304 # vapor pressure of acetone (atm) at 25 Degree C
    
    # Calculate concentration of acetone in moles
    cM = PPMtoConcMole(1, aMW)

    # Calculate partial pressure of acetone
    VPP = concToPP(cM, R, K)
    X = molFractionPP(VPP, aVP, tATM)
    n1 = molFractionToMole(X, h_2oMoles)
    mass = moleToMass(n1, aMW)
    vol = massToVol(mass, aRho)
    print(f"{vol} L of acetone is required to reach 1PPM with 50ml of water")

if __name__ == "__main__":
    main()