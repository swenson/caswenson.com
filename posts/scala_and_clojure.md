Scala and Clojure
=================

My primary language for the past few months has been Scala, with some occasionaly bouts of Java.

I've also started to learn Clojure. The company I am working for is into the JVM stack, and these languages are both based on the JVM.

As a long-time Java programmer, I appreciate the cleanliness of Scala, and I've grown pretty comfortable with it over the past few months. It's sort of the language that Java really wanted to be when it grew up: all that OO goodness that we love, but without so many mistakes as Java has, and with a helpful smattering of functional programming.

That said, Scala has some flaws, including some fairly deep ones.

* IDE support is pretty terrible. I tried to use Eclipse and IntelliJ early on, and they were both incredibly broken. I've never gotten them to work well. I just use Sublime Text 2 these days, and I find that Scala is a clean enough language that this isn't too big of a deal.
* Implicits are just a bad idea. The standard library uses them sparingly and fairly well, but this is such a dangerous feature. (For those of you who don't know Scala, implicit functions are used to automatically convert an object of one type to another, under the hood.) It makes sense in a few limited cases, but I groan when I see them now.
* The standard fundamental data types are wasteful and have poor performance. The `List` and `Map` data types are optimized for adding things to them, but in doing so create lots of extra copies and have very poor access properties. `List`, the most fundamental structure, is a damned linked list! This makes me want to cry. `OpenHashMap` is better, at least.

That said, I much prefer Scala to Java at this point.

Clojure, on the other hands, I am much newer to, and don't have nearly as solid experience with yet, so take my points with a grain of salt.

Clojure's obsession with immutability is nice from the point-of-view of thread-safety and (theoretical, yet mostly unrealized) concurrency, but at a high cost. Its memory footprint seems to be the worst of the JVM languages, and it defaults to using reflection for most method calls, so it is significantly slower. (Even with proper type annotations, it is slower.)

Furthermore, I think Clojure is just fundamentally harder to read. I've done my fair share of Lisp programming in the past, and I think that Lisp is just a lot less natural to read, probably because we spend so much time with infix languages.

Plus, I would posit that Clojure's premise is doomed to failure. A Lisp that doesn't support tail-call optimization and proper recursion seems broken. (And yes, I know about `loop`/`recur`, but that is essentially a functional for-loop.) Scala does some rudimentary TCO, though it doesn't always tell you the function you wrote can use it.

The biggest plus for Clojure is that it is JVM (which is also a weakness). It's a plus because it means you can take advangate of the Java ecosystem (logging, libraries, experience, etc.). Which is probably the primary reason we are using it instead of some other functional languages.

That said, I will be spending quite a bit of time this year learning both in greater detail, so perhaps I will update with further opinions on them.

(I'm also thinking about getting more into Go this year, and perhaps finally learning Erlang.)