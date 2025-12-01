import matplotlib.pyplot as plt
overs = [5,10,15,20]
india_scores = [50,75,145,180]
australia_scores = [40,65,130,160]
plt.plot(overs,india_scores,label="India",marker='o',linestyle='-',color='blue')
plt.plot(overs,australia_scores,label="Australia",marker='s',linestyle='-',color='red')
plt.xlabel("Overs")
plt.ylabel("Scores")
plt.title("Cricket match scores")
plt.legend()
plt.grid(True)
plt.show()