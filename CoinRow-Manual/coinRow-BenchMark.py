import random
import time
import matplotlib.pyplot as plt
import os

#bruteforce
def coin_row_bruteforce(coins, i=0):

    if i >= len(coins):
        return 0
    take = coins[i] + coin_row_bruteforce(coins, i + 2)
    skip = coin_row_bruteforce(coins, i + 1)
    return max(take, skip)

#greedy approach
def coin_row_greedy(coins):
    indexed = [(val, idx) for idx, val in enumerate(coins)]
    indexed.sort(reverse=True) 

    locked = [False] * len(coins)
    total = 0
    for val, idx in indexed:
        if not locked[idx]:
            total += val
            locked[idx] = True
            if idx > 0:
                locked[idx - 1] = True
            if idx < len(coins) - 1:
                locked[idx + 1] = True
    return total

#dynamic progarming
def coin_row_dp(coins):
    n = len(coins)
    if n == 0:
        return 0
    if n == 1:
        return coins[0]

    dp = [0] * n
    dp[0] = coins[0]
    dp[1] = max(coins[0], coins[1])

    for i in range(2, n):
        dp[i] = max(coins[i] + dp[i - 2], dp[i - 1])
    return dp[-1]


# BENCHMARK 
n_sizes = list(range(4, 25, 2))

bf_times, greedy_times, dp_times = [], [], []
bf_space, greedy_space, dp_space_table, dp_space_opt = [], [], [], []

for n in n_sizes:
    # Generate random coin values between 1 and 20
    test_coins = [random.randint(1, 20) for _ in range(n)]

    # --- Benchmark Brute Force ---
    start = time.perf_counter()
    coin_row_bruteforce(test_coins)
    bf_times.append(time.perf_counter() - start)
    bf_space.append(n) 

    # --- Benchmark Greedy ---
    start = time.perf_counter()
    # Run multiple iterations to get stable timing for fast operations
    for _ in range(100):
        coin_row_greedy(test_coins)
    greedy_times.append((time.perf_counter() - start) / 100)
    greedy_space.append(n)  # Needs locked array + indexed list of size n

    # --- Benchmark Dynamic Programming ---
    start = time.perf_counter()
    for _ in range(100):
        coin_row_dp(test_coins)
    dp_times.append((time.perf_counter() - start) / 100)
    dp_space_table.append(n)  # DP array of size n
    dp_space_opt.append(2)  # Space-optimized DP requires only 2 variables


plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
os.makedirs("./CoinRow-Manual/img", exist_ok=True)

plt.style.use(
    "seaborn-v0_8-whitegrid"
    if "seaborn-v0_8-whitegrid" in plt.style.available
    else "default"
)


c_bf = "#E6A100"  
c_greedy = "#E04848"  
c_dp = "#2EB872" 
c_dp_opt = "#16693C" 


# 1. TIME COMPLEXITY GRAPH
fig_time, ax1 = plt.subplots(figsize=(7, 5))

ax1.plot(
    n_sizes,
    bf_times,
    marker="o",
    color=c_bf,
    linewidth=2.2,
    label=r"Brute Force: $O(1.618^n)$",
)
ax1.plot(
    n_sizes,
    greedy_times,
    marker="s",
    color=c_greedy,
    linewidth=2.0,
    label=r"Greedy: $O(n \log n)$",
)
ax1.plot(
    n_sizes,
    dp_times,
    marker="^",
    color=c_dp,
    linewidth=2.0,
    label=r"Dynamic Programming: $O(n)$",
)

ax1.set_yscale("log")
ax1.set_title(
    "Empirical Execution Time (Log Scale)", fontsize=13, weight="bold", pad=12
)
ax1.set_xlabel("Number of Coins ($n$)", fontsize=11)
ax1.set_ylabel("Execution Time in Seconds (log)", fontsize=11)
ax1.legend(frameon=True, facecolor="white", edgecolor="#ddd")

fig_time.tight_layout()
fig_time.savefig(
    "./CoinRow-Manual/img/coin_row_time_complexity.png", dpi=300, bbox_inches="tight"
)
plt.close(fig_time)

# 2. SPACE COMPLEXITY GRAPH
fig_space, ax2 = plt.subplots(figsize=(7, 5))

# Apply small visual offsets so all 3 lines remain visible
ax2.plot(
    n_sizes,
    [x + 0.4 for x in bf_space],
    linestyle="--",
    color=c_bf,
    linewidth=2.0,
    label=r"Brute Force: $O(n)$ stack depth",
)
ax2.plot(
    n_sizes,
    greedy_space,
    linestyle=":",
    color=c_greedy,
    linewidth=2.5,
    label=r"Greedy: $O(n)$ tracking arrays",
)
ax2.plot(
    n_sizes,
    [x - 0.4 for x in dp_space_table],
    linestyle="-.",
    color=c_dp,
    linewidth=2.0,
    label=r"DP (Table): $O(n)$ array",
)
ax2.plot(
    n_sizes,
    dp_space_opt,
    linestyle="-",
    color=c_dp_opt,
    linewidth=2.5,
    label=r"DP (Optimized): $O(1)$ scalar vars",
)

ax2.set_title("Auxiliary Memory Footprint", fontsize=13, weight="bold", pad=12)
ax2.set_xlabel("Number of Coins ($n$)", fontsize=11)
ax2.set_ylabel("Auxiliary Storage / Stack Depth (units)", fontsize=11)
ax2.set_ylim(0, 30)
ax2.legend(frameon=True, facecolor="white", edgecolor="#ddd")

fig_space.tight_layout()
fig_space.savefig(
    "./CoinRow-Manual/img/coin_row_space_complexity.png", dpi=300, bbox_inches="tight"
)
plt.close(fig_space)

print("Both charts successfully saved in ./CoinRow-Manual/img/")