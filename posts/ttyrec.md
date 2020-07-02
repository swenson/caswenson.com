# ttyrec conversion

I'm an armchair fan of [NetHack](http://www.nethack.org) and other roguelikes, though I don't play them too much.
I've always wondered why there wasn't, say, a NetHack screensaver that would just play through the game, since it seemed to be ripe for screensavering.

I'd found some pieces of tools that might do the job around the Internet: [TTY "recordings" of NetHack ascensions](http://nethack.wikia.com/wiki/Notable_ascensions) (essentially, replaying through the terminal sequences while they are playing), [pyte](https://github.com/selectel/pyte) (a Python terminal emulator), and [images2gif](https://pypi.python.org/pypi/images2gif) (a mostly working animated GIF maker).

It's *almost* there, so I wrote the missing piece that takes the screen buffer (as a matrix of character codes) and converts it to an image using an [old  DOS bitmap font](http://en.wikipedia.org/wiki/Code_page_437#mediaviewer/File:Codepage-437.png), and then all of the glue code to make it all work together.
I sped up the results by 5&times; or so, and then run the whole thing through ImageMagick in the end to shrink the animated GIF.

I open sourced the whole thing as [ttyrec2gif](https://github.com/swenson/ttyrec2gif). It produces nice GIFs like:

<img src="images/out00001.gif" alt="Sample nethack screensaver animated GIF" />

There's one last piece: how to actually turn this into a screen saver.

In OS X, it's a matter of writing a little Quartz Composer program to randomly pick GIFs from a directory and play them as movies. This has hard-coded paths in it, because I haven't figured out how to make OS X screen saver configuration parameters, so I'll just post a screen shot of what the program looks like:

<img src="images/nethack-screensaver_-_Editor_2014-10-19_11-38-46.png" alt="Quartz Composer screenshot of my screensaver app."/>

(Having Quartz pick a random GIF and then reload and pick another one after 5 minutes is a fun challenge. The best solution I came up with involved using a wave generator that, when rounded, would trigger an event only when it reached its apex, and this triggered a sampler to resample and pick a new random GIF. Kind of a Rube Goldberg way of doing it, but it was fun.)

Anyway, at the very least, there are some cool GIFs out there to look at now.
I'm considering doing a big run and converting a more runs into GIFs, but it's very time-consuming (it takes many hours to convert a game to an animated GIF for now).
