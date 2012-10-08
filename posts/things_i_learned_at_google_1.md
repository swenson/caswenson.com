Things I've Learned At Google, Part One
=======================================

I've spent the past 19 months working as a software engineer at Google. They have adopted a lot of great practices, some completely their own, and I certainly learned a lot from working them. I thought I would share some of the particular insights I had while working there.

This first post will be about software engineering. Shortly, I'll post another about general workplace stuff.

First, an overall thought: Google was definitely the most professional place I've worked in terms of software engineering. However, just like any software engineering methodologies, their software engineering Kool-Aid is good, but you don't want to drink all of it.

Code reviews are a must.
------------------------

Prior to Google, I had done very little formal code review as most projects we were simply "too busy" to "take time out" to do them. They are not even a little bit optional at Google: every change to the codebase must undergo at least one person's review, and possibly many more depending on the exact nature of the change and the person making it. At first, I was very skeptical about this, but I learned that there is so much much value in having this formal process, for a multitude of reasons.

1. First, if you have a small team, code reviews are a good way to keep up with what other people on your project are doing, both on a personal level ("Jane is working on feature X"), as well as understanding what the code does. This means that it will be easier for you to make a modification to the codebase, if it is necessary, or even to take ownership of it should something happen (i.e., team member moves on).
2. Code reviews don't take as long as you think.
3. Code reviews significantly increase the quality of the code produced, both in readability, but in catching bugs and poor design decisions. Perhaps not as much as true pair programming, but with a lot fewer of the disadvantages.
4. Unfortunately, code reviews have one downside: it is often tricky to work on two different reviews on the same part of the codebase at the same time. This depends heavily on your version control system &mdash; distributed version control systems, like git, tend to support this pretty well. But even so, there is some cost in terms of "mental swap space", as sometimes it is difficult to focus on an entirely different change until you hear back on your pending change. The best way to avoid this is make sure your team prioritizes reviewing code above pretty much all else, so that your other team members aren't waiting on you. (Code reviews are a bit like a turn-based game, and when it is the other person's turn, it can seem like it takes forever.) I always tried to have a spare project to work on that I could hack on a little while waiting.

IDEs are worth it for large projects.
-------------------------------------

Prior to Google, I despised IDEs. I still don't have a lot of love for them, but reusing Google's extensive codebase in my own code finally broke me out of my IDE-less existence: there is simply *too much* code to try to wrangle without features like autoimport, name completion, refactoring, etc. I chose Eclipse, because I was doing Java work and Eclipse is well-supported inside Google. As slow as Eclipse is, it saved me a lot of time hunting through docs looking for the right class, with the right class name, the right function name method, etc.: I could just tab-complete my way to freedom a lot of the time.

Build systems still suck.
-------------------------

Google has their own build system that integrates with, well, everything. But it still sucks. Not as much as autotools, SCons, Makefiles, but it still sucks. Where, oh where, is the build system of my dreams?
Python and other untyped languages make life harder for large projects.

For small projects or stuff that I am doing by myself, I love Python. The time it saves me is tremendous. However, nothing is more frustrating than programming with a large, unknown codebase in Python. I would often see code like this, even in a well-manicured codebase:

<pre>
def ReadFromDatabase(self, query, metadata):
  """Perform the query on the database."""
  ...
</pre>

So... what is query? A string? What is its format? Could it be a tuple, a list? What is metadata? Essentially, the only answers to these questions were to go digging through documentation, look for other code that calls that function, read through the function itself. And sometimes I just don't have time to go on a coding adventure: I want to call the method and go on with my day. Java, for all of its faults, at least tells you the type information of the parameters, so I have a strong hint for my adventure. This might involve navigating factories, factoryfactories, and all other kinds of abominations, but at least I would have a good start.

It Should Be Easy To Run Your Program.
--------------------------------------

Google programmers love command-line flags. They sprinkle them everywhere. The problem is: they often specify the default values elsewhere, perhaps in a script that only runs in production. It can make running a program locally difficult, which in turns makes testing and debugging hard. The moral I learned is that it should be dead simple to build, run, and test your program. Hunting around for documentation on the perfect incantation magic is a real bummer.

Test *ALL* the things.
----------------------

Before Google, I hadn't really practiced a lot of TDD. Sure, when I had a small piece of code that had very well-defined inputs and outputs, and if I had time, I would create some doctests (in Python) or the equivalent elsewise, but it was never a priority. At Google, good testing is the state religion. If it doesn't have tests, it doesn't exist. No excuses. I don't care how complex the code is: it has to be tested. Writing the tests firsts often helps, but doesn't always make sense.
