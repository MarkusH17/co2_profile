#algorithm for calculating key point C_plants, the exit concentration at the plant zone
#import directories

#parameters
area = 7500 #m^2
height = 8 #m
vol = area*height

vin = 3*vol/3600 #m^3/s (3 air change /hr)
mol_vol = 22.4 #m^3/kmol
MWco2 = 44.01 #kg/kmol

plant_height = 1.5 #m
intake = 2.5 #g/m2-hr

def C_plants(C_in):

    mol_in = vin*(C_in/1e6)/mol_vol #kmol/s

    mass_in = mol_in*MWco2 #kg/s

    mass_gen = intake*area/3600/1000 #kg/s

    mass_out = mass_in - mass_gen #kg/s

    mol_out = mass_out/MWco2 #kmol/s

    return mol_out*mol_vol*1e6/vin #ppm