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