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