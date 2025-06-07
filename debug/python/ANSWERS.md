# Answers

### Question 1: What's the bug?

We don't check whether l_fast.next is None before advancing.
This was a much easier bug to conceal in Go, where the type checker
knew only that next was a `*LinkedList`; in Python, thanks to
pyright, I had to introduce the `_next` property and misexplain
why it exists. Note that the complaint is right, though; Pyright
will complain that `l_slow` can be None after moving to `l_slow.next`,
even though actually if we got that far it's guaranteed safe.

### Question 2: What's wrong with the tests?

The failure can occur only if we have a non-cyclic list with an
odd length. The tests must be testing cyclic lists (otherwise the
return False for the cycle detection wouldn't be covered), and must
be covering cases where we find the value, or where we fall off
the end of a list. So probably the error is just not testing on
odd-length lists.

### Question 3: Is the reported exception correct?

It's not. Line 42 is the access at the top of the loop, right under
`while l_fast is not None:` and cannot produce this exception. The
exception would have to be on line 47.

### Question 4: So how did we get this exception?

The exception traceback is from a different version of the code. (It
really did work out by accident; the traceback would be correct for
an earlier version before I added the `_next` trick.)

You might think this question seems unfair. A week after the first
time I built an example of this exercise, we got a report with a
stack traceback, and the customer even sent us the version string
of the program, which included its git commit. The code failing didn't
exist in that commit. I don't think they did this on purpose, but
you can never trust that people reporting a bug are actually using
the version of the thing they're claiming to in the bug report. People
make mistakes. They also lie for really weird reasons you can't
reasonably anticipate.
