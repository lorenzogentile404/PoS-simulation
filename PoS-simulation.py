from random import choices
import copy

miners_coins = [1,1,1,3,2]
print("Miners coins: " + str(miners_coins))
total_coins = sum(miners_coins)
miners_indexes = list(range(0,len(miners_coins)))
reward = 1
rounds = 1000

miners_coins_over_rounds = [miners_coins]

for r in range(0, rounds):
    winning_probabilities = [c/total_coins for c in miners_coins]
    w = choices(miners_indexes, winning_probabilities)[0]
    print("Miner " + str(w) + " wins round " + str(r) + " and receives " + str(reward) + " coins.")
    miners_coins = copy.deepcopy(miners_coins)
    miners_coins[w] += 1
    print("Miners coins: " + str(miners_coins))    
    miners_coins_over_rounds.append(miners_coins) 

import matplotlib.pyplot as plt

x = list(range(0, rounds + 1))

for m in miners_indexes:
    y = [e[m] for e in miners_coins_over_rounds]
    plt.plot(x, y)

plt.xlabel("Rounds")
plt.ylabel("Miners coins")     
plt.show()