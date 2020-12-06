# Day 6 [Problem page](https://adventofcode.com/2020/day/6)

----
Note: the input file you download will be different to mine ("input.txt" in this folder), but I included it here just in case you want to test the code without participating on Advent of Code.

----

### Part 1

For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

```
abcx
abcy
abcz
```

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

```
abc

a
b
c

ab
ac

a
a
a
a

b
```

This list represents answers from five groups:

- The first group contains one person who answered "yes" to 3 questions: a, b, and c.
- The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
- The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
- The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
- The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

> This asks to count the number of unique count of char in the group

### Part 2

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?

> count the duplicates.