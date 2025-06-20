# An Alternative Way to Perform Fitch Cheney's Five Card Trick

This repository demonstrates an alternative approach to performing Fitch Cheney's Five Card Trick .

## Method

The method is as follows:

- We assign each subset of 4 cards a parity, and for each subset of 5 cards, we determine which card should be removed. To do this efficiently, we use a greedy algorithm: start by finding an element whose removal results in a previously undecided subset of 4 cards. Once such a subset is found, we mark it as decided and assign it a parity based on the value of the removed card modulo 2. Then, we propagate this decision upward by marking all supersets (subsets of 5) that include this 4-card set as "decided," making them all map to this specific 4-card subset. This allows us to eliminate many 5-card subsets early on, improving both performance and compactness. Ultimately, we use 197,276 out of the 270,725 possible 4-card combinations (from a standard 52-card deck).
- Once we determine which card to remove from each 5-card subset, the assistant hides that exact card. The parity of the resulting 4-card subset then becomes known, allowing the magician to narrow the search space from 48 remaining cards down to either the odd-numbered or even-numbered cards — halving the possibilities to just 24.
- To encode one of 24 possible outcomes, we use permutations of the 4 visible cards. Since there are 4! = 24 different ways to arrange 4 distinct cards, the magician can determine the hidden card by identifying the permutation's index relative to a sorted order of those 4 cards. He then selects the corresponding card from the narrowed-down list of 24 possibilities.

To improve efficiency, the assignment process is split into two steps: one for subsets of 5 where all elements are odd or all are even, and another for mixed subsets. While edge cases like this don't appear in a standard 52-card deck, this distinction ensures robustness if the code is later generalized.

The program produces two lookup tables as output:

Subsets of 4 cards along with their assigned parities (for the magician).
Subsets of 5 cards along with the card to be removed (for the assistant).

## Usage

As it was already mentioned, the process is split into 2 parts:

1. `even_odd.py` to decide even-only or odd-only subsets of 5 cards
2. `complex_cases.py` to decide mized subsets of 5 cards

After running these files consecutively you may optionally check the result, especially if you modified anything. For that purpose use `check.py`. When you run it you'll see these logs or similar:

```plaintext
decided4 has 249900 items
decided5 has 2598960 items
```

Note that `complex_cases.py` logs the number of processed subsets of 5 cards every 100000 iterations.
