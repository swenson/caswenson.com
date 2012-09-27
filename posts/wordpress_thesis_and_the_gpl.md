Wordpress, Thesis, and the GPL
==============================
There's been <a href="http://mixergy.com/chris-pearson-matt-mullenweg/">some hubbub</a> going around the web about Wordpress potentially suing a developer for breaching the GPL.

The quick run-down: Wordpress is licensed under <a href="http://en.wikipedia.org/wiki/GNU_General_Public_License">GPL2</a>. Thesis is a premium Wordpress theme.

The debate really boils down to: does the GPL require Thesis to be also licensed under the GPL?

The answer: <strong>almost</strong> not, but maybe.

I'll save you some reading.  Clause 2 of GPL2:

<blockquote>
&hellip; If identifiable sections of that work are not derived from the Program,
and can be reasonably considered independent and separate works in
themselves, then this License, and its terms, do not apply to those
sections when you distribute them as separate work. &hellip;
</blockquote>

IANAL, but this says, quite clearly, if it is not derived from GPL code <strong>and</strong> can be reasonably considered independent, then the GPL does not apply.

The question is, what does "independent" mean in this sentence.  Does it mean independent in the sense that it can run without it?  Or does it mean the code does not have any code in common with the GPL code?

It's unclear.  I am inclined to the second viewpoint, because the first has a lot of nasty ramifications.  However, some people, including <a href="http://www.gnu.org/licenses/gpl-faq.html#GPLPluginsInNF">the FSF</a>, appear to believe in the first viewpoint (roughly speaking).

Ugh.  Software licensing sucks.  This is why I use the <a href="http://en.wikipedia.org/wiki/MIT_License">MIT License</a>.  Mostly because I like putting some kind of license on the code, and this seems one of the least restrictive ones.