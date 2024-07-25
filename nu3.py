import seaborn as sns
import matplotlib.pyplot as plt

#DISPLOT, Використання: Візуалізація розподілу числової змінної з опціями для гістограми, KDE та ECDF


tips = sns.load_dataset("tips")
sns.displot(tips["total_bill"], kde=True)
plt.title("Displot of Total Bill with KDE")
plt.show()

#HISTPLOT, Використання: Візуалізація розподілу числової змінної у вигляді гістограми.
sns.histplot(tips["total_bill"], bins=20)
plt.title("Histplot of Total Bill")
plt.show()

#KDEPLOT ,Використання: Оцінка щільності для числової змінної.
sns.kdeplot(tips["total_bill"], shade=True)
plt.title("KDEplot of Total Bill")
plt.show()

#ECDFPLOT, Використання: Емпірична функція розподілу для числової змінної.
sns.ecdfplot(tips["total_bill"])
plt.title("ECDFplot of Total Bill")
plt.show()

#REGPLOT, Використання: Візуалізація регресійної лінії для двох числових змінних.
sns.regplot(data=tips, x="total_bill", y="tip")
plt.title("Regplot of Total Bill vs Tip")
plt.show()

#CATPLOT, Використання: Візуалізація даних для категоріальних змінних з різними типами графіків (точкові, смужкові, ящикова діаграма тощо).
sns.catplot(data=tips, x="day", y="total_bill", kind="box")
plt.title("Catplot of Total Bill by Day")
plt.show()


#SWARMPLOT, Використання: Відображення всіх спостережень числової змінної разом з категоріальною змінною, уникаючи перекриття точок.

sns.swarmplot(data=tips, x="day", y="total_bill")
plt.title("Swarmplot of Total Bill by Day")
plt.show()
