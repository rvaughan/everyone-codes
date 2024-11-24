# Quest 09 : Sparkling Bugs

This folder contains a solution for quest 9.

## Problem Description

### Part 1

The sun has just set, so the city-dwellers are also heading for a well-deserved rest. You're just returning home when suddenly you notice a very bright shooting star. Except, this star isn't falling but... rising upwards! Upon reaching the highest point possible, the star splits into dozens, maybe even hundreds of smaller stars, each flying in a different direction until they vanish. After a while, another shooting star appears, followed by another, and another! You manage to pinpoint the origin. It's the **Headquarters of Pyromancers** near the market. You wonder where these bursts are coming from. Curiosity takes you to the source of the light.

The closer you get to the building, the brighter your surroundings become. It seems that mysterious objects are shining on the ground and are being launched into the sky by a trebuchet. You manage to squeeze through a crowd of onlookers and see a pyromancer in a slightly singed apron loading glowing spheres onto the trebuchet, which soon soar high into the air to burst into tiny sparks. What a spectacle!

The pyromancer is very eager to explain how it works. It turns out that the spheres are loaded with... beetles. **Each beetle has numerous shiny dots made of a sparkling substance** on its shell. When the sparkball (as the pyromancer calls it) reaches its highest point, it breaks apart, releasing the beetles, which, by rapidly fluttering their wings, scatter the glowing powder in all directions!

To achieve the **desired brightness effect**, you simply need to apply the right **number of dots** to the beetles, gather them into a sparkball, and launch them into the air. The pyromancer even has special **stamps** prepared that can apply several dots at once, but **each beetle can be stamped only once**.

There are 4 available stamps with the following numbers of dots: `1, 3, 5, 10`.

It would be good to devise a way to stamp the beetles in such a way as to use **as few of them as possible for the desired brightness** in order to preserve some precious insects for future spectacles. Unfortunately, no one has come up with an efficient method yet, so the stamping process has become disorganized and inefficient. Of course, you step up to solve this problem!

The pyromancer hands you a list of what is needed to be prepared for the next showcase: `(your notes)`.

Example based on the following notes:
```
2
4
7
16
```
Your notes is a list of sparkballs, or to be more precise, **a list of brightnesses** you want to achieve. You have to calculate the **minimum number of beetles you need to stamp for each ball** and sum them up to get the **total number of beetles needed for the whole list**.

By looking at the example above, the optimal way to accomplish this requires:

- **2 beetles** for constructing the first ball with brightness `2` (two 1-dot stamps)
- **2 beetles** for brightness `4` (one 1-dot stamp and one 3-dot stamp)
- **3 beetles** for brightness `7` (two 1-dot stamps and one 5-dot stamp)
- **3 beetles** for brightness `16` (one 1-dot, one 5-dot, and one 10-dot stamp)

The **minimum number of beetles** you need for this sparkballs list is: 2 + 2 + 3 + 3 = **10**.

**What is the minimum number of beetles you need to stamp to construct all sparkballs from the list?**

Solution: **12740**

### Part 2

The next day, the tournament participants are invited to the Headquarters of the Pyromancers. It turns out that the task involves sparkballs and devising the most efficient method to utilize the beetles. It seems that the pyromancer you met the previous evening did not have time to inform his colleagues that you had already solved this problem. Well... Good for you!

**The available stamps have changed** to the following: `1, 3, 5, 10, 15, 16, 20, 24, 25, 30`. Also, the list of sparkballs to be constructed is much longer now, but the core problem remains the same, so you feel very well prepared for this quest.

Example based on the following notes:
`
33
41
55
99
`
The optimal way to construct this sparkballs requires:

- **2 beetles** for constructing the first ball with brightness  `33`  ( 30 + 3 )
- **2 beetles** for brightness  `41`  ( 25 + 16 )
- **2 beetles** for brightness  `55`  ( 30 + 25 )
- **4 beetles** for brightness  `99`  ( 30 + 30 + 24 + 15 )

The minimum number of beetles you need for this sparkballs list is: 2 + 2 + 2 + 4 = *10*.

**What is the minimum number of beetles you need to stamp to construct all the sparkballs on the list?**

Solution: **5018**

### Part 3

In the evening, you encounter the same pyromancer again in the market, showcasing a light show, and you thank him for his assistance in the tournament. It turns out he has another problem to solve.

The sparkballs have caught the attention of the king himself, and he has placed an order for a display of gargantuan size! The brightnesses he wants are so high that there is no way to pack so many beetles in a single sphere, but the pyromancer has an idea. He wants to simply **tie two sparkballs together** and launch them into the air.

To achieve the target brightnesses from the king's list, each sparkball needs to be **split into two spheres**, but to keep the whole effect symmetric, they should have similar brightnesses. **The maximum difference in brightness between such sparkball pairs is** `100` dots. Any differences greater than this would ruin the final effect.

The pyromancer also constructed some **additional stamps**, so you can place many more dots on a single beetle! The full list of available stamps is now as follows: `1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101`.

Example based on the following notes:
`
156488
352486
546212
`
The best way to split the first brightness into two sparkballs is by using  `775`  beetles to create a sparkball with brightness  `78275` , and another  `775`  beetles to create a sparkball with brightness  `78213` , which sums up to the target brightness:  `156488` . The brightness difference between those sparkballs is: `78275 - 78213 = 62`, which is within the acceptable range.

The best way to split the second brightness is by using  1745  beetles for brightness of  `176245`  and another  `1745`  beetles for brightness of  `176241` , which sums up to the target brightness: `352486` . The brightness difference between those sparkballs is: `176245 - 176241 = 4`, which is within the acceptable range.

The best way to split the third brightness is by using  `2705`  beetles for brightness of  `273156`  and  `2704`  beetles for brightness of  `273056` , which sums up to the target brightness: `546212` . The brightness difference between those sparkballs is: `273156 - 273056 = 100`, which is at the edge of the acceptable range but still counted as valid.

The minimum number of beetles you need for this sparkballs list is 775 + 775 + 1745 + 1745 + 2705 + 2704 = **10449**.

**What is the minimum number of beetles you need to stamp to fulfil the king's order?**