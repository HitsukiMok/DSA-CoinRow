#Didn't put any error handling to make it less intimidating :)
#function initialization here btw

def dynamicProgramming(coins):
    n = len(coins) #n = number of elements in the list

    #refers to the F(1) = C[1]
    #If there's only one coin, then taking it is negligible
    if n == 1:
        return coins[0], [coins[0]]

    #-- Step 1 - DP Table Initialization --
    #dp[i] represents the maximum value possible by only looking at coins[0...i]
    dp = [0] * n


    #-- Step 2 - Base Cases Definition --
    #For coin[0], you only have one coin available so it will be the maximum value
    dp[0] = coins[0]


    #For coin[1], you can take coin[0] OR coin[1] but never both. Therefore pick the larger number.
    dp[1] = max(coins[0], coins[1]) #max() basically takes the largest value out of the parameters included.


    #-- Step 3 - Filling the Table (Recurrence Relation) --
    # In every coin[i], test the two choices.
    for i in range(2 , n):
        #Option 1: Take coin[i]
        #However you won't be able to pick coin[i-1]
        #So what we'll do is add the best score from 2 spots back (dp[i-2])
        coinTake = coins[i] + dp[i - 2]

        #Option 2: Skip coin[i]
        #Gain 0 from coin i, best score will be carried over from dp[i-1]
        coinSkip = dp[i-1]

        #Store on what coin has the higher value
        dp[i] = max(coinTake, coinSkip)

    #-- [OPTIONAL] Step 4: Backtrack (to find out what coins won) --
    #Tracing backwards to see what choices the program made.

    coinsChosen = []
    i = n-1

    while i>= 0:
        if i == 0:
            #If the first coin was taken
            coinsChosen.append(coins[0])
        elif i == 1:
            #reached the second coin and check if which coin won
            if dp[1] == coins[1]:
                coinsChosen.append(coins[1])
            else:
                coinsChosen.append(coins[0])
            break
        elif dp[i] == coins[i] + dp[i - 2]:
            #if dp[i] matches the take_coin's formula then it is selected
            coinsChosen.append(coins[i])
            i -= 2 #jump to skip the adjacent element
        else:
            #dp[i] == dp[i-1], coin[i] was skipped.
            i -=1

    coinsChosen.reverse()

    return dp[-1], coinsChosen


#Function in action

coin_list = [5,1,9,10,9,2]

maxTotal, selected = dynamicProgramming(coin_list)
print(f"Coin Row:       {coin_list}")
print(f"Max Value:      Php {maxTotal}")
print(f"Selected Coins: {selected}")