# Quest 02 : The Runes of Power

This folder contains a solution for quest 2.

## Problem Description

### Part 1

The knights of the Order of the Golden Duck don superb armour and weapons, each adorned with mysterious symbols. While some of these may be mere decorative ornaments, many are powerful combinations of **runic symbols** that endow the items with extraordinary properties. Each aspiring knight must master these symbols to fully harness their magical powers. Such mastery demands knowledge and patience, for even the slightest error can lead to unforeseen consequences.

The day of the exam is fast approaching, and you feel confident in your preparation. After all, you have studied diligently throughout the night! As the candidates gather in the grand, circular hall, you see the object of your test: a knight's helmet. Though it appears ancient, the magical runes inscribed along its lower edge still glow with a bright, mystic light.

Your task is to **count all the runic words** within the inscription on the helmet. Fortunately, the task is simpler than anticipated; a note beside the helmet lists all the possible runic words that may appear. With these in hand, you begin the task of counting.

**Example based on the following notes:**

```
WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE
```

The possible runic words, based on the first line are: **THE**, **OWE**, **MES**, **ROD**, and **HER**.

The inscription to examine reads: AWAKEN *THE* P**OWE**R ADORNED WITH **THE** FLA**MES** BRIGHT IRE.

The sentence contains **4 runic words** (highlighted): THE, OWE, another THE, and MES.
 
Other examples for the same WORDS list as above:

- **THE** FLAME SHIELDED **THE** HEART OF **THE** KINGS: **3 runic words**
- P**OWE** PO WER P **OWE** R: **2 runic words**
- **THER**E IS **THE** END: **3 runic words** (THE and HER overlap)

What is the number of runic words engraved on the helmet?

Solution: **36**

### Part 2

Congratulations! Your correct answer allows you to advance to the next chamber. This time, your challenge centers around a colossal shield, worn down over time and scarred from countless battles. Yet, despite its age, the runic symbols etched upon it remain as vivid and clear as ever.

The list of potential runic words is still at your disposal, but it has grown considerably longer. However, **the objective of the task has changed**. This time, your focus is not on counting the runic words, but rather on counting the **runic symbols** that make up those words inscribed on the shield.

The inscription sprawls across the shield in **many individual lines**, each demanding careful interpretation. Moreover, these inscriptions can be read from left to right or from right to left, meaning you must **search for runic words in both directions**.

**Example based on the following notes:**

```
WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ
```

For this inscription, counting the runic symbols proceeds as follows:

- AWAKEN *THE* P**OWE** A**DOR**NED WITH **THE** FLA**MES** BRIGHT IRE: **15** runic symbols
- **THE** FLAME SHIELDED **THE** HEART OF **THE** KINGS: **9** runic symbols
- P**OWE** PO WER P **OWE** R: **6** runic symbols
- **THER**E IS **THE** END: **7** runic symbols
- **QAQAQ**: **5** runic symbols (two QAQ words overlap each other)

Thus, the final count is: 15 + 9 + 6 + 7 + 5 = **42** runic symbols

What is the number of runic symbols engraved on the shield that form runic words?

Solution: 5202

### Part 3

You advance carefully to the final examination chamber, where a set of **scale armour** awaits the candidates. This armour, unlike anything you've encountered before, is covered in scales, each etched with a runic symbol. The scales are meticulously arranged in a rectangular grid, with the **right edge seamlessly connected to the left**, forming an unbroken loop.

In this challenge, neighbouring scales can form runic words both horizontally and vertically: left to right, right to left, top to bottom, bottom to top. Your task remains as it was before: to find all the runic words hidden within the armour and **count the number of scales that compose them**.

**Example based on the following notes:**

```
WORDS:THE,OWE,MES,ROD,RODEO

HELWORLT
ENIGWDXL
TRODEOAL
```

After identifying and highlighting all the runic words, the armour looks like this:

```
**HE**LW**O**RL**T**
ENIG**W**DXL
T**RODEO**AL
```

Counting the highlighted symbols gives the final answer: **10 scales**

What is the number of scales on the armour that form runic words?

Solution: **11547**
