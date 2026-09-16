# Didn't put any error handling to make it less intimidating :)
# function initialization here btw

callCount = 0

def coinRow_bruteforce(coins, i=0, _is_root=True):

    global callCount  # use the module-level call counter
    if _is_root:
        callCount = 0  # reset counter for a fresh run

    callCount += 1  # increment every entry incl. base cases.

    # -- Step 1 - Base case --
    # if we've reached the end of the list, meaning no coins remain.
    if i >= len(coins):
        return 0, []

    # -- Step 2 - Choice 1: take the current coin--
    # take coins[i], and lock out coins[i+1], then recurse starting from coins[i+2]
    valAfter, coinsTake = coinRow_bruteforce(coins, i + 2, _is_root=False)
    totalTake = coins[i] + valAfter
    pathTake = [coins[i]] + coinsTake

    # -- Step 2.5 - Choice 2: Skip the current coin
    # skip coins[i] and evaluate the adjacent coin at coins[i+1]
    totalSkip, pathSkip = coinRow_bruteforce(coins, i + 1, _is_root=False)

    # -- Step 3 - Decision --
    if totalTake > totalSkip:
        bestVal, bestPath = totalTake, pathTake
    else:
        bestVal, bestPath = totalSkip, pathSkip

    # starts recursion at the start of the list (i = 0)
    if _is_root:
        return bestVal, bestPath, callCount

    return bestVal, bestPath


# Function in action
coin_list = [5, 1, 9, 10, 9, 2]
maxValue, selected, callsTotal = coinRow_bruteforce(coin_list)

print(f"Coin Row:             {coin_list} (Length n = {len(coin_list)})")
print(f"Total:                Php {maxValue}")
print(f"Selected Coins:       {selected}")
print(f"Total Function Calls: {callsTotal}")