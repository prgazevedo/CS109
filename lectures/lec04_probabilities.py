import math

def probability_not_seeing_someone(n_total, n_special, k_sample):
    """
    Calculates the probability of NOT selecting anyone from a specific group
    when drawing a random sample from a larger population.
    """
    numerator = math.comb(n_total - n_special, k_sample)
    denominator = math.comb(n_total, k_sample)
    return numerator / denominator

def main():
    print("Welcome to the probability calculator!")
    n_total = int(input("Enter the total number of individuals: "))
    n_special = int(input("Enter the number of individuals in the special group: "))
    k_sample = int(input("Enter the number of individuals to be sampled: "))

    prob_not_seen = probability_not_seeing_someone(n_total, n_special, k_sample)

    # Pedagogical explanation
    print()
    print(f"We want to know the probability of NOT selecting anyone from a group of {n_special} people")
    print(f"when randomly choosing {k_sample} people from a total population of {n_total}.")
    print()
    print(f"The probability that NONE of the selected individuals are from the special group is:")
    print(f"\n  ➤ Probability = {prob_not_seen:.4f}  (or {prob_not_seen * 100:.2f}%)")
    print("Done")
