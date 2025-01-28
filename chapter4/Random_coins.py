# import random

# def randomCoin():
#     """Generate a list of 100 random coin flips ('H' or 'T')."""
#     coin = []
#     for _ in range(100):
#         coin.append('H' if random.randint(0, 1) == 0 else 'T')
#     return coin

# def hasStreak(coinList):
#     """Check if there is at least one streak of 6 consecutive 'H' or 'T'."""
#     currentStreak = 1

#     for i in range(1, len(coinList)):
#         if coinList[i] == coinList[i - 1]:
#             currentStreak += 1
#             if currentStreak == 6:
#                 return True  # A streak of 6 is found
#         else:
#             currentStreak = 1  # Reset streak if the coin changes

#     return False  # No streak of 6 found

# # Main Experiment
# streakCount = 0  # Count experiments with at least one streak
# for _ in range(10000):  # Perform 10,000 experiments
#     coin = randomCoin()
#     if hasStreak(coin):
#         streakCount += 1

# # Calculate percentage
# chance_of_streak = streakCount/100
# print(f'The chances of a streak of 6 are approximately {chance_of_streak:.2f}%')

    #step-1 create a list of 100 flipped coins either head or tail
    #step-2 find how many steaks of 6 head or tails are there in this list of coin
    #step-3 do this 10000 times and finally display it in precentage
    #without funtions
    # import random, time
    # start_time = time.time()
    # streakCounts=0
    # for _ in range(10000):
    #     coins=[]
    #     coins=['H' if random.randint(0,1)==0 else 'T' for _ in range(100)]
    #     currentStreak=1

    #     for i in range(1,len(coins)):
    #         if coins[i] == coins[i-1]:
    #             currentStreak+=1
    #             if currentStreak==6:
    #                 streakCounts+=1
    #                 break
    #         else:
    #             currentStreak=1
    # print(f'Chances are: {streakCounts/100}')
    # end_time = time.time()  # Record the end time
    # print(f"Runtime: {end_time - start_time:.4f} seconds")
import random
def randomCoins():
    coins=[]
    coins=list(random.choices(['H','T'], k=100))
    return coins
def Streaks(coinList):
    currentStreak=1
    for i in range(len(coinList)):
        if coinList[i]== coinList[i-1]:
            currentStreak+=1
            if currentStreak==6:
                return True
        else:
            currentStreak=1
    return False
steak=0
for _ in range(10000):
    coins = randomCoins()
    if Streaks(coins):
        steak+=1
print(f'chances are:{steak/100}%')
        






                
            

