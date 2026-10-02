import matplotlib.pyplot as plt

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
savings = [20, 35, 15, 50, 45]

plt.figure(figsize=(8, 5))

plt.plot(weeks, savings, color='green', marker='o', linestyle='--', linewidth=2, label='Weekly Savings')

plt.title('My Savings Progress (Line Graph)', fontsize=14, fontweight='bold')
plt.xlabel('Weeks', fontsize=12)
plt.ylabel('Savings ($)', fontsize=12)

plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.show()

plt.figure(figsize=(8, 5))

plt.bar(weeks, savings, color='orange', edgecolor='darkorange', alpha=0.85)

plt.title('My Savings Progress (Bar Chart)', fontsize=14, fontweight='bold')
plt.xlabel('Weeks', fontsize=12)
plt.ylabel('Savings ($)', fontsize=12)

plt.show()
