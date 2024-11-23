# Quest 08 : A Shrine for Nullpointer

This folder contains a solution for quest 8.

## Problem Description

### Part 1

As you well know, the knights of the Order of the Golden Duck are also exceptional architects. The next challenge pertains to their architectural skills.
The priests wish to erect a new shrine in honor of the god Nullpointer, the protector of the lost. They are certain that **the structure must be symmetrical, with precisely one highest point**, but they cannot decide on the material and exact shape.

The first proposal is a **pyramid-shaped structure** made of stone blocks. From the highest point of such a structure, the **height decreases by one block down for every block to the side**. The algorithm for planning such a shrine is as follows:

- Place one block at the location where the center of the structure will be, ensuring the shrine always has a single highest point.
- Determine the thickness of the subsequent layer. For a pyramid, **the thickness of all layers will always be 1**.
- Begin adding the new layer by placing blocks on the ground to the right and left of the structure. Add new blocks to all columns that existed in the previous layer.
- Continue adding subsequent layers following the same principles.

An example construction plan, with layered blocks marked by numbers, could look like this:
 
```
                                  4
                     3           434
          2         323         43234
 1   >   212   >   32123   >   4321234 
```

The first layer contains a single block of stone. The second layer contains 3 blocks, the third is made of 5 blocks, and for completing the forth, 7 blocks are needed.

The number of blocks for such a structure is limited, but the priests have a considerable quantity at their disposal. The king has also agreed to order **an additional number of blocks** to ensure that all layers are completed and the structure is perfectly symmetrical.

The knights wonder **how wide (in number of blocks)** the final structure will be and **how many additional blocks** they must order to achieve a fully symmetrical shrine.

**Example based on the following notes:**

```
13
```

Your note is a single number - available number of blocks: 13

With that many blocks, the following shrine can be built:

```
   #
 #####
#######
```

To complete the final layer, an **additional 3 blocks** must be ordered, marked with $ below:

```
   $
  $#$
 #####
#######
```

The final structure's width is **7 blocks**.

Your final answer is a product of multiplying the number of missing blocks by the target width. 3 * 7 = **21**

Determine the final width of the shrine and the number of additional blocks needed to complete the final layer.

**What is the result of multiplying the number of missing blocks by the target width?**

Solution: **10025324**

### Part 2

Sadly, a shrine of this shape would be neither original nor impressive compared to its height... One of the knights proposes that only the thickness of the layers needs to be changed. The idea involves generating the layers' thicknesses recursively. This sounds like something worthy of the glory of the god of the lost!

Start with a layer thickness of 1, and calculate the thickness of the subsequent layers as follows:

- Multiply the thickness of the previous layer by the current number of priests of Nullpointer: `(your notes)`.
- Take the remainder of dividing the result by the number of current priest acolytes: ```1111```.
- You have the thickness of the subsequent layer ready to use.

Marble is proposed as the material, of which the priests have a large supply, totalling `20240000` blocks.

The king will, of course, still fulfil his promise to order additional blocks to complete the build, so your task essentially remains unchanged.

You are counting the priests of the god, Nullpointer, noting down the total number and starting calculations of the king's expenses. **The final answer is still a multiplication of the number of blocks needed to complete the last layer by the final width of the shrine.**

**Example based on the following notes:**

`3`

Assuming only 3 priests of Nullpointer (your notes), `5` priest acolytes for simplicity (instead of the actual number: 1111), and `50` blocks are available, the calculation of layer thickness would be as follows:

```
layer                   thickness
1                       1
2      (1 * 3) mod 5 =  3
3      (3 * 3) mod 5 =  4
4      (4 * 3) mod 5 =  2
5      (2 * 3) mod 5 =  1
```

An example construction plan, with layered blocks marked by numbers, looks like this:

``` 
                                                 5
                                  4             545
                                 444            444
                     3           434            434
                    333          333           53335
                    333         43334          43334
                    333         43334          43334
          2        33233        33233          33233
         222       32223        32223         5322235
         222       32223       4322234        4322234
 1   >   212   >   32123   >   4321234   >   543212345 
```

Blocks needed for completing each layer:

```
layer    blocks
1        1
2        9
3        20
4        14
5        9
```

Constructing such 5 layered shrine would require 1 + 9 + 20 + 14 + 9 = **53 blocks**, so the king needs to buy 3 additional blocks.

The final structure's width is 9 blocks, so the answer is 3 * 9 = **27**.

Determine the final width of the shrine and the number of additional blocks needed to complete the last layer.

**What do you get if you multiply these two numbers?**