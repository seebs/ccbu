# Python debug exercise

This is a really simple puzzle. What makes it interesting is trying to
do it with a few constraints.

## Setting the stage

This is a very naive linked list implementation in Python, which
has the fancy feature of implementing cycle detection, so it doesn't
run forever if a list has a cycle. It uses a pretty standard algorithm
for this.

Do NOT start by looking at the test cases, or running the code. Just
read linked_list.py.

I'll tell you this much: The test cases provide 100% test coverage.
Every line in this is executed in tests, the tests all get the results
they expect, and the results they expect are correct. The tests are
not *wrong*.

### Question 1: What's the bug?

You might have spotted it already. If so, cool! But there's more.
If not, have a look at `exception.txt`. Does this give you a hint
as to what the bug might be?

### Question 2: What's wrong with the tests?

Again, *don't* look at the tests yet. Can you tell what's wrong with
them? They have to cover at least a few cases, or the coverage wouldn't
be 100%. So what do you know they *are* testing? And given that there's
a way to reach an exception, what do you know they *aren't* testing?

### Question 3: Is the reported exception correct?

Once you have an understanding of the bug, look at the exception
provided again. Is this exception *possible* as reported? (Hint:
if it were, I wouldn't be asking.)

### Question 4: So how did we get this exception?

If you assume the exception isn't correct, then... How did this
exception get generated? Imagine that you're a maintainer on this
code and someone has sent you this exception. What happened?

Answers in ANSWERS.md.
