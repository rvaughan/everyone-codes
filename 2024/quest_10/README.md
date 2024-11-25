# Quest 10 : Shrine Needs to Shine

This folder contains a solution for quest 10.

## Problem Description

### Part 1

The group of knights vying for entry into the Order of the Golden Duck now find themselves in the Memory Stack Desert, where construction has already begun on the shrine dedicated to the god, Nullpointer. It turns out that the shrine will be **adorned with numerous runic symbols**, adding to its magnificence!

Most of the symbols are engraved by mages using a spell, but there are also spots marked with dots that still need to be filled in a very specific way. Knights receive their own samples to practice this process.

Each sample is an 8 by 8 grid. The corners of the grid are marked with `*` , and these spots **cannot contain runic symbols**. The lines connecting the corners are engraved with runic symbols, leaving a **4 by 4 empty square in the centre**. This empty area must be filled in with the missing runic symbols, but it must be done in a very specific manner.

**Each empty space marked with** `.`  **must be filled with a runic symbol that appears both in the row and the column of the 8 by 8 grid to which the space belongs**. There is always exactly one matching symbol. Once all the missing symbols are filled in, we can read a **runic word by transcribing the symbols row by row from left to right, starting from the top**. There cannot be two identical symbols in the runic word.

Your goal is to find the runic word hidden in your sample grid: `(your notes)`.

**Example based on the following notes:**
```
**PCBS**
**RLNW**
BV....PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
```
For the first field marked with a dot, the corresponding row contains symbols BVPT, and the column contains PRFG. The only symbol that appears in both the row and the column is P:
```
**PCBS**
**RLNW**
BVP...PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
```
By following the same rules, you can find other missing symbols:
```
**PCBS**
**RLNW**
BVPT..PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
```

```
**PCBS**
**RLNW**
BVPTB.PT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
```

```
**PCBS**
**RLNW**
BVPTBVPT
CR....HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
```

```
**PCBS**
**RLNW**
BVPTBVPT
CRR...HZ
FL....JW
SG....MN
**FTZV**
**GMJH**
```
   ...   
```
**PCBS**
**RLNW**
BVPTBVPT
CRRCZHHZ
FLFLJWJW
SGGMNSMN
**FTZV**
**GMJH**
```
Finally, you can read the runic word: PTBVRCZHFLJWGMNS
```
**PCBS**
**RLNW**
BVPTBVPT
CRRCZHHZ
FLFLJWJW
SGGMNSMN
**FTZV**
**GMJH**
```
**What runic word will be formed upon solving your sample grid?**

Solution: **FMRPJNBTDWKQCZLH**

### Part 2

You find the runic word, which allows you to proceed with the training on constructing a shrine.

Each runic word obtained in the manner described above has its own power, which is calculated as follows:

- Each symbol has a **base power**, determined alphabetically: A:1, B:2, C:3, D:4, E:5, F:6, G:7, H:8, I:9, J:10, K:11, L:12, M:13, N:14, O:15, P:16, Q:17, R:18, S:19, T:20, U:21, V:22, W:23, X:24, Y:25, Z:26.
- Each symbol occupies an **individual position in the word, starting from 1**.
- The **effective power** of a symbol is equal to its base power multiplied by its position in the word.
- The power of the entire word is the **sum of the effective powers of all the symbols**.

In the second round of the task, the challengers receive a stack of training samples `(your notes)`. Your goal is to identify all the runic words and **calculate the sum of their powers**.

**Example:**

For the example runic word from the previous part, `PTBVRCZHFLJWGMNS`, the power is calculated as follows:

1 * 16 (P) + 2 * 20 (T) + 3 * 2 (B) + ... + 16 * 19 (S) = **1851**.

**What is the total power of all the runic words on your training samples?**

Solution: **194554**

### Part 3

Your training is complete, so you can join the builders of the shrine!

It turns out that covering the shrine with runic words serves not only a decorative purpose but they are also a functional feature. In the construction, each individual platinum block contains a 6 by 6 grid of symbols on one side, the centre part of the 8 by 8 grid you worked on. The remaining symbols are placed on adjacent blocks. Thus, the previous **8 by 8 grids have shared parts between multiple blocks**. The runic words that you obtain permanently bind together all nine blocks covered with at least one symbol from the 8 by 8 grid that produced them, ensuring the entire structure is securely held by the ancient power of the runes!

The task still involves **calculating the total power of all the runic words**, but this time you are provided with a section of an actual wall of blocks from the shrine to deal with `(your notes)`. **Not every 8 by 8 block will yield a runic word**, but it is certain that securing the entire wall of blocks into a cohesive structure is possible.

**An additional challenge is the presence of** `?` **signs that represent runic symbols that you must deduce during your work**. For each `?` symbol, there is always only one runic symbol that matches. Identify all possible runic words and provide their combined power.

**Example based on the following notes:**
```
**XFZB**DCST**
**LWQK**GQJH**
?G....WL....DQ
BS....H?....CN
P?....KJ....TV
NM....Z?....SG
**NSHM**VKWZ**
**PJGV**XFNL**
WQ....?L....YS
FX....DJ....HV
?Y....WM....?J
TJ....YK....LP
**XRTK**BMSP**
**DWZN**GCJV**
```
If we were to separate the given section into individual platinum blocks, it would look as follows:
```
* *XFZB* *DCST* *

* *LWQK* *GQJH* *
? G....W L....D Q
B S....H ?....C N
P ?....K J....T V
N M....Z ?....S G
* *NSHM* *VKWZ* *

* *PJGV* *XFNL* *
W Q....? L....Y S
F X....D J....H V
? Y....W M....? J
T J....Y K....L P
* *XRTK* *BMSP* *

* *DWZN* *GCJV* *
```
Solving the top-left block using the previously learned rules unlocks almost all of the symbols you need:
```
**XFZB**
**LWQK**
?GLWG.WL
BS.SHBH?
P?PJ.KKJ
NMN.ZMZ?
**NSHM**
**PJGV**
```
For the first dot from the top, the only symbol that does not yet have a pair in the associated row and column is `V`, so the dot must be replaced with the symbol V, as must the associated question mark.
```
**XFZB**
**LWQK**
VGLWGVWL
BS.SHBH?
P?PJ.KKJ
NMN.ZMZ?
**NSHM**
**PJGV**
```
Based on the same reasoning, the second dot must be an `X`, the third must be a `Q`, and the last must be an `F`.
```
**XFZB**
**LWQK**
VGLWGVWL
BSXSHBHX
P?PJ.KKJ
NMN.ZMZ?
**NSHM**
**PJGV**
```
```
**XFZB**
**LWQK**
VGLWGVWL
BSXSHBHX
PQPJQKKJ
NMN.ZMZ?
**NSHM**
**PJGV**
```
```
**XFZB**
**LWQK**
VGLWGVWL
BSXSHBHX
PQPJQKKJ
NMNFZMZF
**NSHM**
**PJGV**
```
Solving the next block to the right is now simple, as we have already found the missing symbol represented by the `?` sign. The completed words are highlighted below:
```
**XFZB**DCST**
**LWQK**GQJH**
VGLWGVWL....DQ
BSXSHBHX....CN
PQPJQKKJ....TV
NMNFZMZF....SG
**NSHM**VKWZ**
**PJGV**XFNL**
WQ....?L....YS
FX....DJ....HV
?Y....WM....?J
TJ....YK....LP
**XRTK**BMSP**
**DWZN**GCJV**
```
```
**XFZB**DCST**
**LWQK**GQJH**
VGLWGVWLDQWLDQ
BSXSHBHXXCNHCN
PQPJQKKJVKJTTV
NMNFZMZFGFSZSG
**NSHM**VKWZ**
**PJGV**XFNL**
WQ....?L....YS
FX....DJ....HV
?Y....WM....?J
TJ....YK....LP
**XRTK**BMSP**
**DWZN**GCJV**
```
You could try solving the bottom blocks to add more brilliance to the shrine, but unfortunately, they are not solvable. The section of the wall is stable anyway, as the two blocks with runic words securely hold all the neighbouring blocks together.

In summary, we have 2 runic words with powers **1900** and **1989** so the total power for this part is 1900 + 1989 = **3889**.

**Find as many runic words as possible on your wall section. What is the sum of their total power?**

Solution: **212032**