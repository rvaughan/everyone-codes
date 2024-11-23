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

Solution: **142665228**

### Part 3

Everyone agrees that the final shape is almost perfect! It's just a matter of adjusting the parameters slightly and ensuring there are empty spaces for the worshippers to place their offerings. After a brief debate, the finally chosen idea is as follows:

Layers are planned in almost the same way as before, but with different parameters.
Start with a layer thickness of 1, and calculate the thickness of the subsequent layers as follows:

- Multiply the thickness of the previous layer by the current number of **high priests of Nullpointer**: `(your notes)`.
- Take the remainder of dividing the result by the number of current **high priest acolytes**: `10`.
- Add the number of current **high priest acolytes**: `10` to the result to ensure the minimal thickness of the layers.
- You have the thickness of the subsequent layer ready to use.

After designing the shrine as before, layer by layer, it is time to calculate how many bottom blocks in each column should be left as empty space, according to the following rules:

**The blocks forming the upper frame of the shrine cannot be removed to prevent the structure from collapsing.**
Adjacent blocks are connected on the side planes, not diagonally. An example shrine and the blocks forming the upper frame of the shrine are shown below:
```
     #                   #
    ###                 ###
    ###                 # #
    ###                 # #
   #####               ## ##
   #####       >       #   #
   #####               #   #
   #####               #   #
  #######             ##   ##
  #######             #     #
 #########           ##     ##
```
To calculate the **number of blocks that should be left as empty space in a specific column**:

- Multiply the number of **high priests**: `(your notes)` by the current width of the shrine base.
- Multiply the result by the height of this column.
- Take the remainder of dividing the result by the number of current **high priest acolytes**: `10`.
- Now you know how many bottom blocks should be left as empty for given column.

**If you repeat that process for all columns, you can finally calculate how many block are needed for building the shrine of that size.**

The final chosen material is the most ubiquitous metal in the land of Algorithmia - platinum. The priests have amassed a supply of `202400000` blocks of it.

Additionally, the width of the structure does not matter, as the king's advisors (who are, of course, knights of the Order) have already allocated the edge of the Memory Stack Desert as the building site. **It is only necessary to calculate the number of blocks the king should provide to fully complete the shrine.**

Your goal is, of course, to minimise the king's expenses, so you need to find a plan for the shrine that utilises all available platinum supplies while ensuring minimal cost for the king at the same time.

**Example based on the following notes:**

`2`

Assuming only 2 high priests `(your notes)`, `5` high priest acolytes for simplicity (instead of the actual number: 10), and `160` blocks are available, the calculation of layer thickness would look as follows:

```
layer                      thickness
1                          1
2      (1 * 2) mod 5 + 5 = 7
3      (7 * 2) mod 5 + 5 = 9
4      (9 * 2) mod 5 + 5 = 8
5      (8 * 2) mod 5 + 5 = 6
```

An example construction plan is shown below. The shrine is represented as the number of blocks per column (or column heights, in other words), as it’s too tall to be fully visualised.
```
layers    thickness of           width              column heights
total     the last added layer
1         1                      1                       [ 1]
2         7                      3                    [7][ 8][7]
3         9                      5                [9][16][17][16][9]
4         8                      7            [8][17][24][25][24][17][8]
5         6                      9        [6][14][23][30][31][30][23][14][6]
```
Removing bottom blocks from a 5 layered shrine looks as follows:

- The shrine width is 9 blocks.
- The first and the last columns with a height of [6] blocks stays untouched as they are part of the upper frame of the shrine.
- For the columns with a height of [14], 2 blocks are removed: `(2 * 9) * 14 mod 5 = 2` 
- For the columns with a height of [23], 4 blocks are removed: `(2 * 9) * 23 mod 5 = 4`
- Columns with a height of [30] stay untouched: `(2 * 9) * 30 mod 5 = 0`
- For the middle column with a height of [31], 3 blocks are removed: `(2 * 9) * 31 mod 5 = 3`

In total, 15 bottom blocks should be left as empty, so constructing a full 5 layered shrine requires **162** blocks, which means the king needs to purchase an additional **2** blocks.

Below you can find a few more examples for the same parameters as above, illustrating how many platinum blocks would be needed to build a completed shrine with a given number of layers:
```
layers  blocks
2       19
3       67
4       115
5       162
6       239
7       353
8       491
9       569
10      690
16      1885
32      7601
64      30655
128     123131
256     491005
512     1964801
1024    7863295
2048    31461371
4096    125820925
```

**How many platinum blocks at minimum should the king provide to ensure that the shrine design can be completed?**
