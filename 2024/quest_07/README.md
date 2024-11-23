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

Solution: **EHBKGDAJF**

### Part 2

It's time for the knights' races!

Unlike the squires, they race on specially designed tracks that **also affect the devices' behaviour**, often disrupting planned actions. The track is organized as a closed loop of segments, allowing knights to complete multiple laps. Knights **start from segment S** and proceed in a clockwise direction (to the right when viewed from above).


The terrain of the track is marked as follows:

- `=`  does not alter the execution of the plan
- `+`  forces the device to **increase the power by one**, ignoring the current action
- `-`  forces the device to **decrease the power by one**, ignoring the current action
- `S`  start and finish segment, does not alter the execution of the plan

The first action is executed (and the first essence is gathered) at the first segment after S. The last action and last essence gathering for the loop occur at the S segment. In other words, S is the segment from which everyone starts, but it is also the last segment of the track's loop.

The race is set for 10 loops.

Example based on the following notes:

```
A:+,-,=,=
B:+,=,-,+
C:=,-,+,+
D:=,=,=,+
```

For the sample plans above and the track as below:

```
S+===
-   +
=+=-+
```

the actual actions for the first loop (taking into account the race track) will be as follows:

```
      1   2   3   4   5   6   7   8   9  10  11  12
track +   =   =   =   +   +   -   =   +   =   -   S
A     +   -   =   =   +   +   -   =   +   -   -   =
B     +   =   -   +   +   +   -   +   +   =   -   +
C     +   -   +   +   +   +   -   +   +   -   -   +
D     +   =   =   +   +   +   -   +   +   =   -   +
```

Device power for each segment:

```
      1   2   3   4   5   6   7   8   9  10  11  12
A    11  10  10  10  11  12  11  11  12  11  10  10
B    11  11  10  11  12  13  12  13  14  14  13  14
C    11  10  11  12  13  14  13  14  15  14  13  14
D    11  11  11  12  13  14  13  14  15  15  14  15
```

Total essence gathered:

- A  11 + 10 + 10 + 10 + 11 + 12 + 11 + 11 + 12 + 11 + 10 + 10 = **129**
- B  11 + 11 + 10 + 11 + 12 + 13 + 12 + 13 + 14 + 14 + 13 + 14 = **148**
- C  11 + 10 + 11 + 12 + 13 + 14 + 13 + 14 + 15 + 14 + 13 + 14 = **154**
- D  11 + 11 + 11 + 12 + 13 + 14 + 13 + 14 + 15 + 15 + 14 + 15 = **158**

The ranking of the action plans after one loop is: **DCBA**.

The final ranking of the action plans after 10 loops is also **DCBA**, with a total essence gathered:

```
A : 1290
B : 3640
C : 3700
D : 4280
```

The racetrack for the first round is shown below:

```
S-=++=-==++=++=-=+=-=+=+=--=-=++=-==++=-+=-=+=-=+=+=++=-+==++=++=-=-=--
-                                                                     -
=                                                                     =
+                                                                     +
=                                                                     +
+                                                                     =
=                                                                     =
-                                                                     -
--==++++==+=+++-=+=-=+=-+-=+-=+-=+=-=+=--=+++=++=+++==++==--=+=++==+++-
```

**What is the final ranking of action plans after 10 loops?**

Solution: **EGDBFAIKJ**

### Part 3

You have advanced to the final duel! The general rules remain unchanged, but the racetrack is much more complex. Each knight must **make their action plan**, making sure it is precisely **11 actions long**, consisting of:

- 5 actions of  `+` 
- 3 actions of  `-` 
- and the remaining 3 as `=`

For example, a valid action plan could be `+-=+-=+-=++`

Your rival knight declares their strategy first, allowing you to quickly make a note of it.

**The duel is set for 2024 loops.**

Victory is almost guaranteed, but just in case, you decide to compare a few plans… and to ensure that you are more than prepared **you consider all possible plans!**

The racetrack for the final duel is shown below:

```
S+= +=-== +=++=     =+=+=--=    =-= ++=     +=-  =+=++=-+==+ =++=-=-=--
- + +   + =   =     =      =   == = - -     - =  =         =-=        -
= + + +-- =-= ==-==-= --++ +  == == = +     - =  =    ==++=    =++=-=++
+ + + =     +         =  + + == == ++ =     = =  ==   =   = =++=
= = + + +== +==     =++ == =+=  =  +  +==-=++ =   =++ --= + =
+ ==- = + =   = =+= =   =       ++--          +     =   = = =--= ==++==
=     ==- ==+-- = = = ++= +=--      ==+ ==--= +--+=-= ==- ==   =+=    =
-               = = = =   +  +  ==+ = = +   =        ++    =          -
-               = + + =   +  -  = + = = +   =        +     =          -
--==++++==+=+++-= =-= =-+-=  =+-= =-= =--   +=++=+++==     -=+=++==+++-
```

**How many different winning action plans can you prepare?**

Solution: **6373**