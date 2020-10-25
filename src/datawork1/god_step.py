# %%
from scipy.stats import norm

# standard deviation
σ = 2

# x_vector
# 出力方法: norm.rvs(loc=0, scale=σ, size=100)
x_vector = [ 0.97252126, -1.02857293,  2.96798839,  1.47954639,  2.30302219, -1.21060869,
 -1.46308383, -1.19825432,  2.65524597, -1.89158445, -5.24198605,  1.49584387,
 -2.71088748,  2.92155221, -0.52350717,  0.44152937,  3.25705198, -0.94330086,
 -0.35604657 ,-1.48691923, -1.84730759,  0.50064446, -1.73283193,  5.45063192,
 -3.30627077 ,-0.86070975, -1.83234121, -2.10483574,  1.48524602, -0.17839841,
 -1.84079194 , 1.47733652,  0.23209943,  3.49824027, -0.32226888 ,-0.73641755,
  2.43629933 , 4.87255961, -1.51680118,  0.59512955,  1.28052823, -1.19394742,
  2.12664706, -0.13472907,  1.57779377, -3.34138681,  0.56851281,  3.03781297,
  1.84683858,  1.58927038, -0.08621639,  2.01407721,  4.23310237, -1.43257848,
 -1.47116265,  0.18713404, -0.23128959, -1.4125921 , -1.12555011, -1.93983723,
  0.20074949,  1.33572009, -0.61086426,  3.25571033, -0.34183091,  2.6904788,
  0.73024895, -1.15627096, -0.86144379,  0.45065554, -1.21541943, -1.78069194,
  0.77409194,  2.23162412,  0.86026099, -2.4032598 , -0.08027198, -1.97009748,
  2.5540492 , -3.65098597, -1.57648085,  1.74108577, -0.20204982,  3.46591631,
 -0.99954631, -0.17025599,  0.32465933, -1.43176868,  2.59616454, -0.26855989,
 -1.02343448, -0.39121392, -0.22566713, -0.71610917,  1.10114593,  0.63067561,
 -3.67979022,  1.29563936,  0.61756682, -0.28089019]

μ = 0

# Ridual
# 出力方法
u = -1.23582094330468

b1 = 3

def getOutcome(b2):

    y_vector = []
    for x in x_vector:
        y = b1 + b2*x + u
        y_vector.append(y)
    return y_vector

def getXVector():
    return x_vector

def getRisual():
    return u

def getMean():
    return μ

def getSigma():
    return σ




## I don't know how to adgust b1 and b2.

# %%
