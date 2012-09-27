Algorithm styling?
==================
So I've started to come across the algorithm-heavy portion of the book, and starting to come across some issues.  Specifically, how should I properly typeset algorithms?

My requirements are that the algorithms should be
<ul>
	<li>Clean</li>
	<li>Precise</li>
	<li>Not heavy with obscure symbols</li>
	<li>Generic</li>
</ul>

This means things like the Knuth style (as he uses in <em>The Art of Computer Programming</em>, which is widely copied) and the Cormen, et al. style (as used in the monolithic <em>Algorithms</em>, 2nd ed., also widely copied are out).  Knuth's still has some good pointers, but it seems like there is too much there (such as a small summary of the step at the beginning, along with step numbers with the letter of the algorithm in front).  I like how verbose he is: others seem too compact.  And with Cormen, there is too much use of symbols, and computer programming pseudo-code.

My current solution is some kind of hybrid between normal prose text and a normal algorithmic style, though I avoid using symbols like &larr; and &lfoor;<em>x</em>&rfloor; in exchange for phrasing like &quot;Set <em>x</em> to ...&quot;, even more so than Knuth.  Though computer scientists and strong programmers might find the way a bit clunky, I find breaking every step down into more discrete steps, with explanations at each step to be potentially helpful to a confused reader.  However, I also want things to be minimalistic when possible: the meat appears immediately, so that it is possible to stream through it with your eyes very quickly.

For example, let's take a simple algorithm, computing the sequence 1 + 2 + 3 + &hellip; + <em>n</em>, in each of the three methods.

Cormen, et al., might write:



<blockquote>
<div style="font-variant: small-caps;">Sum-to-n(<em>n</em>)</div><br />
&emsp;1&emsp; <em>x</em> &larr; 1</em><br />
&emsp;2&emsp; <em>s</em> &larr; 1</em><br />
&emsp;3&emsp; <b>While</b> <em>x</em> &le; <em>n</em><br />
&emsp;4&emsp;&emsp;<em>x</em> &larr; <em>x</em> + 1<br />
&emsp;5&emsp;&emsp;<em>s</em> &larr; <em>s</em> + x<br />
&emsp;6&emsp;<b>Return</b> <em>s</em>
</blockquote>

Whereas a Knuthian way might be:

<blockquote>
<b>Algorithm A</b> (adding the series of <em>m</em> numbers).  This algorithm outputs the sum of all the integers between 1 and <em>n</em>.

&emsp;K1. [<em>Initialize</em>.]. Set <em>x</em> &larr; 1, <em>s</em> &larr; 1.<br />
&emsp;K2. [<em>Test for loop end</em>.]. If <em>x</em> = <em>n</em>, terminate.  The sum will be <em>s</em>.<br />
&emsp;K3. [<em>Loop through</em>.]. Set <em>x</em> &larr; <em>x</em> + 1, <em>s</em> &larr; <em>s</em> + <em>x</em>.<br />
&emsp;K4. [<em>Repeat</em>.]. Go back to K2.<br />
</blockquote>

My proposed way is similar, but with a little less <em>stuff</em> in it:

<blockquote>
The following algorithm illustrates how to sum up the integers from 1 to <em>n</em>, inclusive of 1 and <em>n</em>.

&emsp;1. Set <em>x</em> = 1, and <em>s</em> = 1.  These will represent the current number to be added and the working sum, respectively.<br />
&emsp;2. If <em>x</em> = <em>n</em>, then we can stop, and the sum will be <em>s</em>.<br />
&emsp;&emsp;(a) Set <em>x</em> = <em>x</em> + 1, <em>s</em> = <em>s</em> + <em>x</em>. We are incrementing the counter variable <em>x</em> and updating our sum.<br />
&emsp;&emsp;(b) Go back to step 2.<br />
</blockquote>

Out of the above, Knuth's looks best on this web page, but I think that mine can look better with wide margins, and provides for a little less ambiguity.

And happy belated 4th of July to everyone!