import matplotlib.pyplot as plt
import numpy as np

# Bar chart =circular chart divided into slices to show percentages of the total.
# Good for visualising distribution among categories.

categories = ["First years","Second years", "Final years"]
values =np.array([500,434,280])

colors =["Green","Yellow","red"]

plt.pie(values, labels = categories,
                autopct ="%1.1f%%",
                 colors = colors ,
                 explode=[0,0,0.2],
                shadow = True
                 )



plt.title("Collage")

plt.show()