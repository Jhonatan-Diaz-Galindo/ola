import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1,10,100)
y = np.log2(x)
y2 = np.tan(x)


plt.subplot(1, 2, 1) #Filas, Columnas, Index

font1 = {'family':'serif','color':'red','size':40}
font2 = {'family':'serif','color':'blue','size':10}

plt.plot(x,y,"#4CAF50",linewidth = '2.5')
plt.legend(["Log2(x)"])
plt.title("Log2(x)", fontdict = font2)
plt.xlabel("x", fontdict = font2)
plt.ylabel("Log2(x)", fontdict = font2)
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(x,y2,"#8577cb",linewidth = '2')
plt.legend(["Tan(x)"])
plt.title("Tan(x)", fontdict = font2)
plt.xlabel("x", fontdict = font2)
plt.ylabel("Tan(x)", fontdict = font2)
plt.suptitle("Graficas :D")
plt.tight_layout()
plt.grid()
plt.show()
