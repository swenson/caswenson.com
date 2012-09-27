Gentoo Linux FTW?
=================
<span style="float: right; margin: 3px"><img src="http://m.caswenson.com/images/gentoo-logo.png" /></span>For the past 6 years or so, <a href="http://www.gentoo.org/">Gentoo</a> has been my preferred distribution of Linux on the server side<sup>*</sup> for many reasons.

But, that doesn't stop me from laughing uncontrollably at Gentoo's <a href="http://uncyclopedia.wikia.com/wiki/Gentoo">Uncyclopedia</a> entry.  Pull quote from the top:

<blockquote>“Stop staring at my output; you have no life!”<br />  ~ GCC on Gentoo users </blockquote>

I have to admit — Gentoo is Linux at its most pretentious and obnoxious.  Maybe I'm an elitist, but I still use and love it.

Why?  What keeps me <tt>emerge</tt>-ing year after year?

<ul>
<li>I <strong>know</strong> Gentoo.  I've been working with it for years, and when things go wrong, I know where to look and how to fix it.  This is also partially due to the fact that it has (arguable, and in my opinion) one of the simplest overall system designs.  I don't need a GUI to fix it, which is really handy for my remote installs where I won't even install a GUI.</li>
<li>It's fast.  The rumors are true — if you know what you are doing and you take some time to do it, you can build a very fast system.</li>
<li>Upgradeable.  The whole system can be easily brought up to speed by resyncing and emerging world.  The only thing you ever have to reboot for is a kernel change, and you'll never have to reinstall to upgrade "versions".  Gentoo doesn't have versions.</li>
<li>Up/downgradeable.  If I want a custom-built version of, say, apache built, I can easily build such a thing and install it.  If it is completely broken, I can easily uninstall it.  And, 99% of the time, I won't ever have to open up the source and run <tt>./configure --prefix=/opt/apache2 && make && sudo make install</tt> to do it, and I won't have to just hope that it won't clobber my files.</li>
</ul>

The first point is one primary reason I don't switch: I am locked in.  I would maybe try Debian or Ubuntu for a server setup, but I'd be shaking in my boots waiting for something to break and not knowing where to start fixing the problem.

My biggest complaint about Gentoo?  It doesn't deal well with bleeding edge Ruby gems.  Meaning, Gentoo tries to install Ruby packages like Gentoo packages, but Gentoo packages are not always up-to-date or complete for all of the gems that are out there.  So, there tend to be version problems and weird configuration errors if you start maintaining your own gem install somewhere.  I'm not really sure whose fault this problem is.

Aside from this minor fault and the reputation that Gentoo gets for being elistist and complicated, I will be sticking to strange, bloated Pacman for the foreseeable future.

<br />
<hr />

<sup>*</sup> My preferred distribution for desktop?  Mac OS X. :) Sorry Linux, you just don't feel as smooth and silky in my hands with a GUI.  The slick GUI that OS X gives me beats any minor incompatibility problems I have, or the fact that OS X uses strange broken BSD versions of some command-line tools, like <tt>sed</tt>.