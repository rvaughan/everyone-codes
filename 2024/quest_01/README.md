# Quest 01 : The Battle for the Farmlands

This folder contains a solution for quest 1.

## Problem Description

The green farmlands of Algorithmia are in constant danger from creatures hiding in the dark. It would be wise to include some fun in the mission, so the first challenge of the tournament is protecting the important crops from destruction.

Each brave knight is given a specific piece of land to protect, but the job isn't just about fighting magical creatures. **The battle requires using healing potions, which must be planned ahead of time.** The Council of Wizards, who are always observing and judging, will evaluate competitors based on the use of healing potions.

The goal is to defeat all enemies while using the **fewest number of potions possible**. Therefore, your potion plan must be executed with accuracy and insight. Luckily, the kingdom's smartest spies have gathered a list of incoming creatures for each area. You also know exactly how many potions are needed for each type of creature:

- **Ancient Ant (A**): Not very dangerous. Can be managed **without using any potions**.
- **Badass Beetle (B)**: A big and strong bug that requires **1 potion** to defeat.
- **Creepy Cockroach (C)**: Fast and aggressive! This creature requires **3 potions** to defeat it.

With this knowledge, you must **order the exact number of potions** that need to be made for your mission.

**Example based on the following notes:**
```ABBAC```

Each creature is shown by a single letter, leading to this sequence of battles:

- **No potions** are needed for the first **A** (Ancient Ant).
- **1 potion** is needed for the first **B** (Badass Beetle).
- **1 potion** is needed for the second **B** (Badass Beetle).
- **No potions** are needed for the next **A** (Ancient Ant).
- **3 potions** are needed for the last monster, **C** (Creepy Cockroach).

In total, you need to order: 0 + 1 + 1 + 0 + 3 = **5** potions.

### Part 1

What is the exact number of potions that need to be prepared for your battle?

**Solution:** 1339

### Part 2

Round two begins! A new area awaits, bringing with it a new list of foes, and a familiar but formidable opponent:

- **Diabolical Dragonfly (D)**: A fast and tricky enemy, hard to hit. This creature requires **5 potions** to defeat it.

This time, however, the battles become more challenging. According to the kingdom's spies, the enemies **sometimes join forces in pairs**, making them tougher to defeat.

When two monsters pair up, you will need **one more potion per creature** than in a one-on-one fight.

Your list remains a single line of creatures, but now you must interpret it in pairs. The **x symbol shows an empty spot** where no monster appears, so for these pairs your calculations should follow the same rules as for individual battles.

**Example based on the following notes:**

`AxBCDDCAxD`

After splitting into pairs, the battle sequence looks like this:

```
Ax BC DD CA xD
```

- The **Ax** pair requires **no potions** because a single Ancient Ant remains weak as before.
- The **BC** pair requires **6 potions** which is 2 for the Badass Beetle and 4 for the Creepy Cockroach because they are attacking together.
- The **DD** pair requires **12 potions** which is 6 per Diabolical Dragonfly instead of the usual 5 since they are attacking together.
- The **CA** pair requires **5 potions** which is 4 for the Creepy Cockroach and 1 for the Ancient Ant.
- The **xD** pair requires **5 potions** because no additional potion is needed for a single Diabolical Dragonfly.

In total, you must order: 0 + 6 + 12 + 5 + 5 = **28** potions.

**Solution:** 5567

### Part 3

The final round is here, and, as expected, it is the most challenging of all! Although no new enemies have appeared, they have grown wiser and realized their strength in numbers.

In this ultimate challenge, you will not just face pairs, but also **groups of three**! For these tough battles, you will need **2 extra potions per creature** compared to fighting them one-on-one.

**Example based on the following notes:**

`xBxAAABCDxCC`

Once the battles are split into their respective groups, they will unfold as follows:

`xBx AAA BCD xCC`

In total, you must order: 1 + 6 + 15 + 8 = **30** potions.

**Solution:** 27722