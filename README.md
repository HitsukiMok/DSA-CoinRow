<div align="center">
<h1>Data Structures and Algorithm - Coin Row Problem</h1>
<h5>Algorithm Analysis for the Coin Row Problem</h5>

<h6><a href="Google colab notebook link here" > [Cloud version] Google Colab Notebook</a></h6>
</div>

---

## Problem

Given that a row of N coins with **positive values**:

<p align="center"> $C_1 , C_2, C_3, ..., C_n$</p>

The goal we need to achieve is to ensure that:
<ul>
    <li>Selected coins <b>HAVE</b> the <b><i>MAXIMUM TOTAL VALUE</i></b></li>
    <li><b>NO</b> two selected coins are <i>adjacent</i></li>
</ul>


Throughout this repository (or report, take it as you will lol) we'll be messing with this set of numbers using a list:

<p align="center"> $[ 5 , 1 , 9 , 10 , 9 , 2]$</p>

This repo will also only utilize Python for the programming and analysis of the Space-Time Complexity.

> If you want a cool challenge, you can always try shooting your shot in translating the code to other languages :3, do not hesitate to shoot a message if you want further clarification or if you dont understand bits of the concept.

---
## Solution

Honestly there are probably multiple algorithms I didn't know that you can use to solve this problem. However, I'll only be focusing on 3 strategies.

Always keep in mind that there are no "better" or all-size-fits-all algorithm, it always depends on the problem and your approach.

In this case, the 3 strategies we will use are:

<!-- no toc -->
  - [Greedy Approach](#greedy-approach)
  - [Brute Force Approach](#brute-force-approach)
  - [Dynamic Programming](#dynamic-programming)

This repo will go in-depth with each approach including the computation for the Space-Time Complexity then put these three against each other and help you understand why <b>Dynamic Programming Approach</b> is the most optimal strategy out them.

---
### Greedy Approach
##### [Click me for the code](./CoinRow-Manual/coinRow-GS.py)

Greedy Approach or Greedy Algorithm is where we will automatically collects the largest non-adjacent numbers in the list and claim it as the maximum value.

By itself, is probably what people would use to get the maximum value of a list. Unfortunately, this algorithm is very short-sighted.

To see what I mean, you can run the code in this repo o

---
### Brute Force Approach


---
### Dynamic Programming


---
### Greedy vs Brute Force vs Dynamic


---
### Conclusion