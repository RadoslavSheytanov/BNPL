import matplotlib.pyplot as plt

reasons = ['Avoiding credit cards', 'Try before buying', 'Buy expensive items', 'Interest-free', 'Spread the cost', 'Easy & convenient']
percentages = [5, 28, 30, 39, 41, 44]


plt.figure(figsize=(10, 8))  
bars = plt.barh(reasons, percentages, color='blue')

plt.xlabel('Percentage (%)')
plt.title('Why do merchants use BNPL services?')
plt.xlim(0, 50)  


for bar, value in zip(bars, percentages):
    plt.text(value + 1, bar.get_y() + bar.get_height()/2, str(value) + '%', va='center')


plt.figtext(0.1, 0.01, 'Survey data from Finder.com', fontsize=10, color='gray')


plt.show()

# IMPORTANT: TO COMPILE THE GRAPH GO TO ----> https://python-fiddle.com/examples/matplotlib
