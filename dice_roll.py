import random
import time
import matplotlib.pyplot as plt
import statistics as stats
import csv

sides = int(input("How many sides does your dice have? "))
attempts = int(input("How many attempts can the player take? "))
dices = int(input("How many dices you want to throw in each attempt? "))
sleep = input("Do you want to add time delay between rolls? (y/n) ")
save = input("Do you want to save the results to a CSV file? (y/n) ")

results = []
sum_results = []

for i in range(attempts):
    roll = [random.randint(1, sides) for i in range(dices)]
    print("Rolling the dice...")
    if sleep == 'y':
        time.sleep(1)
    print("The dices landed on", roll)
    sum_results.append(sum(roll))
    results.extend(roll)
    if sleep == 'y':
        time.sleep(1)
    print("Next roll!")

plt.hist(results, bins=sides)
plt.xlabel("Dice Roll")
plt.ylabel("Frequency")
plt.title("Dice Roll Outcomes")
plt.show()

sum_freq = {}
for i in sum_results:
    if i in sum_freq:
        sum_freq[i] += 1
    else:
        sum_freq[i] = 1

sum_freq = {k: (v/attempts)*100 for k, v in sum_freq.items()}

plt.bar(sum_freq.keys(), sum_freq.values())
plt.xlabel("Sum of Dice Rolls")
plt.ylabel("Percentage (%)")
plt.title("Sum of Dice Rolls Distribution")
plt.show()

mean = stats.mean(results)
median = stats.median(results)
stdev = stats.stdev(results)

print("Mean of dice rolls:", mean)
print("Median of dice rolls:", median)
print("Standard deviation of dice rolls:", stdev)

#CDF
results.sort()
results_cdf = [len(results[:i])/len(results) for i in range(1, len(results) + 1)]
plt.plot(results, results_cdf)
plt.xlabel("Dice Roll")
plt.ylabel("CDF")
plt.title("CDF of Dice Rolls")
plt.show()

if save == 'y':
    with open('dice_rolls.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Roll', 'Sum'])
        for i in range(attempts):
            writer.writerow([roll, sum_results[i]])
    print("Results saved to dice_rolls.csv")
else:
    print("Results not saved.")

print("All attempts taken. Thank you for playing!")
