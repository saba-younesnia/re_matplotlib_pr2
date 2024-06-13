import matplotlib.pyplot as plt
import numpy as np

v_anbar=int(input('hajm anbar: '))
v_gandom=int(input('hajm gandom: '))
v_jo=int(input('hajm jo'))

v_khali=v_anbar-(v_gandom+v_jo)

vs=[]
vs.append(v_khali)
vs.append(v_gandom)
vs.append(v_jo)

vs_ar=np.array(vs)

mylabels=["khali'"+str(v_khali)+"'",'gandom','jo']
myexplode=[0.3,0,0]
plt.pie(vs_ar,labels=mylabels,explode=myexplode)
plt.show()