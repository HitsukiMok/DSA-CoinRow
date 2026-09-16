# Didn't put any error handling to make it less intimidating :)
# function initialization here btw


def coinRow_greedy(coins):
    # -- Step 1 - Tag coins with their og indices --
    # Because sorting jumbles everything up, we need to remember where each coin originally sat
    OGindexed_coins = [(val, idx) for idx, val in enumerate(coins)]

    # -- Step 2 - Sort largest to smallest --
    # for simplification, i just utilized python's .sort function here to quickly sort the list in descending order
    OGindexed_coins.sort(reverse=True)

    locked = [False] * len(coins)
    chosen_with_indices = []
    totalValue = 0
    checksMade = 0

    # -- Step 3 - Grab what we can --
    for val, idx in OGindexed_coins:
        checksMade += 1

        # If this coin hasn't been locked out by an adjacent neighbor
        if not locked[idx]:
            # get it
            totalValue += val
            chosen_with_indices.append((idx, val))

            # lock this coin and its adjacent coins
            locked[idx] = True
            if idx > 0:
                locked[idx - 1] = True
            if idx < len(coins) - 1:
                locked[idx + 1] = True

    # Sort chosen coins back to their original left-to-right order
    chosen_with_indices.sort(key=lambda item: item[0])
    selectedCoins = [val for idx, val in chosen_with_indices]

    return totalValue, selectedCoins, checksMade


#function in action
coin_list = [5, 1, 9, 10, 9, 2]
maxValue, selected, totalChecks = coinRow_greedy(coin_list)

print(f"Coin Row:             {coin_list} (Length n = {len(coin_list)})")
print(f"Greedy Total:         Php {maxValue}")
print(f"Selected Coins:       {selected}")
print(f"Coins Inspected:      {totalChecks} (fast but super short-sighted)")