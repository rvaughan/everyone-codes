# Quest 07 : Not Fast but Furious

This folder contains a solution for quest 7.

## Problem Description

### Part 1

Counting, searching, analysing data... it's time for action! Every knight must be in peak physical condition, just like their steed. Together, they should form a seamless team, and the upcoming tournament event will undoubtedly test this as it's time for **the chariot races**!

The races are conducted in groups. However, this is no ordinary race, and it's not about who reaches the finish line first. All participants move at exactly the same speed. The competition is focused on **collecting magical essence** from the Debugging Spirits Forest.

Each chariot is equipped with a special device for gathering essence from the surrounding area, and **the device has a power level that determines how many units of essence can be collected from the current segment** of the track. Every device follows an individual predefined plan to adjust the power accordingly, which consists of the following actions:

- `+`  increase power by one
- `-`  decrease power by one
- `=`  maintain the same power

If the last action of the plan has been executed and the race is still ongoing, the device simply repeats the actions, starting from the beginning of the list.

**Each device starts with an initial power of 10** and executes an action just before entering the next segment of the track. The power of the device can never fall below zero. If the current power during an action is zero and the action is to decrease power, nothing happens to the device, but the action is still considered executed.

The test round for the squires will soon begin, providing an excellent opportunity to ensure you understand all the rules. Each participant can choose any plan from the provided list. The track length is: **10 segments**. Your task is to **determine the ranking of the plans**, from the one that collects the most essence to the one that collects the least.

Example based on the following notes:

```
A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+
```

First, you can repeat each action plan to cover the entire duration of the race (10 segments):

```
    1   2   3   4   5   6   7   8   9  10
A   +   -   =   =   +   -   =   =   +   -
B   +   =   -   +   +   =   -   +   +   =
C   =   -   +   +   =   -   +   +   =   -
D   =   =   =   +   =   =   =   +   =   =
```

Next, based on that list, you can calculate the device's power for each segment.

```
    1   2   3   4   5   6   7   8   9  10
A  11  10  10  10  11  10  10  10  11  10
B  11  11  10  11  12  12  11  12  13  13
C  10   9  10  11  11  10  11  12  12  11
D  10  10  10  11  11  11  11  12  12  12
```

Based on this, you can calculate the total essence gathered with each plan:

- A  11 + 10 + 10 + 10 + 11 + 10 + 10 + 10 + 11 + 10 = **103**
- B  11 + 11 + 10 + 11 + 12 + 12 + 11 + 12 + 13 + 13 = **116**
- C  10 + 9 + 10 + 11 + 11 + 10 + 11 + 12 + 12 + 11 = **107**
- D  10 + 10 + 10 + 11 + 11 + 11 + 11 + 12 + 12 + 12 = **110**

The final ranking of the action plans after 10 segments is as follows: **BDCA**.

**What is the ranking of the squires' action plans after 10 segments?**