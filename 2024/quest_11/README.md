# Quest 11 : Biological Warfare

This folder contains a solution for quest 11.

## Problem Description

### Part 1

The next tournament competition takes place in a very peculiar location, the Biological Weapons District. Unconventional and cunning warfare methods are a specialty of the Knights of the Order.

One such method involves breeding Omnivorous Termites. Their strength lies not only in their ability to eat literally anything, including the enemy's weaponry, but also in their **rapid population growth** rate. Just a few suitable specimens sent near the enemy's castle can ensure that, within a short time, no trace of it will remain.

However, for breeding purposes, it is crucial to consciously control the population size. Through years of work, **the life cycle of the entire species has been identified**. All individuals have been categorized, and for each category, **the appearance of the next generation has been determined**.

Each individual **converts into a new generation** every day. You have noted down all conversions `(your notes)`. The new individuals are also capable of converting the following day, so the overall population can grow extremely quickly, but it can also be very accurately predicted. This is precisely what the next tournament task involves. **You start with a single** `A` category termite, and you have to **calculate the overall population after 4 days**, based on the conversion notes.

Example based on the following notes:
```
A:B,C
B:C,A
C:A
```
You start with a single `A` termite.

After the first day, it converts into `B` and `C` category termites, so the population looks as follows: `B,C`

After the second day, each termite converts again, so the population grows to **3**: `C,A,A`

After the third day, the population counts **5** termites: `A,B,C,B,C`, and after the fourth day, **8** termites: `B,C,C,A,A,C,A,A`.

**What will be the termite population count on the 4th day?**

Solution: **36**

### Part 2

The second round takes place in an even more hostile environment, the Infestation Lab. This time, however, the Knights have perfected their Omnivorous Termites, and they come in a new strain with distinct conversion patterns. These new termites, starting from a single category `Z` termite, grow in a completely different way than the previous strain, but the general rules remain the same. Your goal is to predict the population count on the 10th day.

**What will be the termite population count on the 10th day?**

Solution: **152844**

### Part 3

The final round presents a new, intricate challenge. A newly engineered strain of termites has been developed for an upcoming combat mission. The knights must now **investigate how the initial termite types affect the overall population after 20 days** of growth.

Your task is to **determine which initial termite types will yield the largest and smallest populations on the 20th day, and then calculate the difference** between these two population sizes.

**Example based on the following notes:**
```
A:B,C
B:C,A,A
C:A
```
Starting with a single `A` termite results in a population of **330205** on day 20.

Starting with a single `B` termite results in a population of **444092** on day 20.

Starting with a single `C` termite results in a population of **175277** on day 20.

You can calculate the population difference by subtracting the smallest number from the largest: `444092 - 175277` = **268815**

**What is the population difference on the 20th day?**

Solution: **1786744062694**