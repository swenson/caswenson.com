Flash and Hosting
=================
I am considering spending some time to properly learn Flash CS3 and ActionScript, in order to write a game, possibly based on an old BBS game I was very fond of, called <a href="http://en.wikipedia.org/wiki/Lords_of_Cyberspace">Lords of Cyberspace</a> (some more info available at <a href="http://everything2.com/index.pl?node_id=1687694">Everything2</a>).  For some reason, I seem to be the only person that cares about the game, as evidenced by the fact that I wrote both of those articles on it.

I was able to get the actual game working on a demo copy of MajorBBS running under <a href="http://www.dosbox.com/">DOSbox</a> on my MacBook Pro.  (BTW, DOSbox is an amazing product that allows you play classic MS-DOS games under OS X.)

In addition to that, <a href="http://www.thursdaybram.com">Thursday</a> and I have come up with a possible idea for a web-based service.  The site will probably be created in something like Ruby on Rails, Django, <a href="http://webpy.org/">web.py</a>, or whatever technology comes across tomorrow, and it may require a bit of bandwidth (enough to worry about bandwidth allotments less than 100GB a month).

I have had a hard time finding a hosting service that makes me happy.  Here's what I would like:

<ul>
<li><b>Cheap.</b> Obviously, as inexpensive as I can get away with.  Especially since it will likely be months before this is actually out of testing and we start selling the service.</li>
<li><b>Full RoR/Django/bleeding edge whatever support.</b> Self-explanatory.</li>
<li><b>Shell access.</b> I don't understand how some providers can have Ruby on Rails support but without shell access but some do (like GoDaddy, who hosts this blog).</li>
<li><b>100+GB per month transfer.</b>  But I would like to be able to easily upgrade this by a few times before moving to dedicated hosting (ha).  Storage to go along with that is also necessary.</li>
</ul>

Storage isn't a bit less of a concern, the more I think about it, because I can always use something like <a href="http://aws.amazon.com/s3">Amazon S3</a> (and this may alleviate some bandwidth concerns as well), which is pretty reasonable.

So far, I like <a href="http://hostingwizard.com/site5/">Site5</a> (but feels almost too good to be true) and <a href="http://www.crucialp.com/web-hosting/">Crucial Paradigm</a> (despite their dumb name, but their plans don't have the most storage or space, though S3 might alleviate some of this, and they look like they know what they are doing).

Anybody have any experience, good or bad, with hosting providers that provide web services support?