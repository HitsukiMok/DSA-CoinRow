# Running this repo locally

> This little guide is for anyone who wants to run the Python files on their own machine :3

The project itself only needs Python. The benchmark script is the only one that needs an extra library (`matplotlib`) because it creates the graphs.

---

## 1. Get the project into your machine

If you have Git installed, open PowerShell or a terminal in the folder where you want the project to live, then run:

```powershell
git clone <repository-link-here>
cd PyTest
```

Alternatively, you can download the repository as a ZIP file from GitHub, extract it, then open a terminal inside the extracted `PyTest` folder. Both works just fine.

---

## 2. Install `uv`

`uv` is basically what we'll use instead of manually installing Python packages with `pip`. It can also grab a compatible Python version for you if your machine does not have one yet.

For Windows, open PowerShell and run:

```powershell
winget install --id=astral-sh.uv -e
```

After it finishes, close PowerShell, open it again, then make sure it worked:

```powershell
uv --version
```

> If `winget` is not available in your machine, you can install `uv` from [its official installation guide](https://docs.astral.sh/uv/getting-started/installation/), then come back here.

---

## 3. Run the algorithms

Make sure your terminal is currently inside the project folder (`PyTest`). The three main scripts do not need any external package, so you can run them right away:

```powershell
uv run python .\CoinRow-Manual\coinRow-GS.py
uv run python .\CoinRow-Manual\coinRow-BF.py
uv run python .\CoinRow-Manual\coinRow-DP.py
```

Each command will print the coin row, its chosen coins, and the final total. Feel free to open any of the files and change this line if you want to test your own values:

```python
coin_list = [5, 1, 9, 10, 9, 2]
```

> Heads up for Brute Force: keep the list reasonably small. It checks every valid possibility, so a bigger list gets slow really quickly. That's the whole point of the comparison lol.

---

## 4. Run the benchmark and regenerate the graphs

The benchmark needs `matplotlib` to make the charts. `uv` can install it only for this command, so you do not need to touch `pip`:

```powershell
uv run --with matplotlib python .\CoinRow-Manual\coinRow-BenchMark.py
```

When it is done, it will update these images:

* `CoinRow-Manual/img/coin_row_time_complexity.png`
* `CoinRow-Manual/img/coin_row_space_complexity.png`

The script may take a little bit because it intentionally runs Brute Force multiple times with increasingly larger coin rows.

---

## Quick troubleshooting

* **`uv` is not recognized:** close and reopen your terminal after installing it. If it still does not show up, restart your machine or follow the official installation guide above.
* **You are getting a "file not found" error:** make sure you opened the terminal inside the main `PyTest` folder before running the commands.
* **The benchmark feels stuck:** it is probably calculating the larger Brute Force cases. Give it a moment, or reduce the final number in `n_sizes` inside `coinRow-BenchMark.py`.

And that's pretty much it. Have fun poking around with the algorithms :)
