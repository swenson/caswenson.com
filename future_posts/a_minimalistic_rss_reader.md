A Minimalistic RSS Reader
-------------------------
Saddened by the demise of Google Reader a few months ago, I completely gave up on RSS feeds and just cut myself off from the world.

A few days ago, I finally decided it was time to move on. Unfortunately, I haven't been super pleased with the options available out there.
Plus, I realized I didn't want to get burned again when they inevitably close and break my heart.

So, like dozens of other people, I just decided to write my own RSS feed reader.

One user
========

One fundamental design decision I made early on is that this system would only support one user, and so I can throw out 95% of the complexity of designing the system right off the bat.

Examples:

* No security. I can throw web page up under an Apache proxy with SSL and basic auth to allow only me in. I don't need to mess with logins or anything.
* No database. The entire state of the program will just be written out as a JSON blob periodically and read in on startup.
* No frills. I only use a few basic features, so I'm only going to implement those. This also means that the page looks incredibly ugly.

Open
====

I wrote it in Go (requires 1.1+) and open sourced it at https://github.com/swenson/littlereader under the MIT license.
Feel free to use it, adapt it, whatever.

It's not finished, but it has nearly every feature I need right now.