#algorithm for calculating key point C_plants, the exit concentration at the plant zone
#import directories

#parameters

import numpy as np

mol_vol = 22.4 #m^3/kmol
MWco2 = 44.01 #kg/kmol
#intake g/m2-hr
def C_plants(C_in, area, height, airchanges, intake, C_co2):
    vol = area*height
    
    #find volume consumed
    mcons = intake*area/1000 
    ncons = mcons/MWco2 #kmol/hr
    vcons = ncons * mol_vol #m3/hr

    vout = airchanges*area*height
    vfeed = vout+vcons

    #solve linear system
    A = [[1,1],[440, C_co2]]
    b = [[vfeed],[vfeed*C_in]]
    X = np.linalg.inv(A).dot(b)
    vair = X[0][0]
    vco2 = X[1][0]

    velocity = (vout/3600)/area #m/s
    #find outlet co2 ppm at st.st.
    C_out = (vfeed*C_in - vcons*1e6)/vout
    return C_out, vol, velocity, vair, vco2, mcons
