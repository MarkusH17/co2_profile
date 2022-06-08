#algorithm for calculating key point C_plants, the exit concentration at the plant zone
#import directories

#parameters


mol_vol = 22.4 #m^3/kmol
MWco2 = 44.01 #kg/kmol

plant_height = 1.5 #m
intake = 2.5 #g/m2-hr

def C_plants(C_in, area, height, airchanges, intake):

    vol = area*height

    vin = airchanges*vol/3600 #m3/s

    mol_in = vin*(C_in/1e6)/mol_vol #kmol/s

    mass_in = mol_in*MWco2 #kg/s

    mass_gen = intake*area/3600/1000 #kg/s

    mass_out = mass_in - mass_gen #kg/s

    mol_out = mass_out/MWco2 #kmol/s

    C_plant = mol_out*mol_vol*1e6/vin 

    velocity = vin/area #m/s

    return C_plant, vol, velocity