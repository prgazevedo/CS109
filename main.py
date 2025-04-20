import random
from tqdm import tqdm

N_TRIALS =1000000
TARGET_SUM = 2



def main():
    print("Welcome to the simulation Game!")
    n_events =0
    for i in tqdm(range(1,N_TRIALS+1)):
        if roll_dice()==TARGET_SUM:
            n_events +=1
        if i % 10000 == 0:
            print(f"Probability after iteration: {i} is {n_events/i}")

    print(f"Final estimated probability of rolling a {TARGET_SUM} is {n_events / N_TRIALS:.5f}")

    
  
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1 + dice2

if __name__ == "__main__":
    main()