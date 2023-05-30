import math

x=1
y=1
senx = math.sin( math.radians(x))
senx2 = senx*senx
seny = math.sin( math.radians(y))
seny2 = seny*seny

cosx = math.cos(math.radians(x))
cosx2 = cosx*cosx
cosy = math.cos(math.radians(y))
cosy2 = cosy*cosy


if (senx2-seny2 == cosy2-cosx2 ):
    print("true")
else:
    print("false")