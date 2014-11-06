# So You Want To Learn Crypto, Part 1

Cryptography and cryptanalysis are topics that fascinate many people, but it's a tricky area to get into.
There's heavy jargon that takes serious studying to get a grasp on.
So, I thought I would list a few resources, recommendations, and maybe even explain a little bit myself.


## Some resources to get you started

* [lvh](https://twitter.com/lvh) has a video from PyCon 2013 called [Crypto 101](http://pyvideo.org/video/1778/crypto-101).
This talk goes through a lot of material in a very short amount of time, so don't worry if not everything clicks.
Instead, I'd pick something that interests you, like hash functions or AES, and dive further into that one topic. If you try to tackle too many subjects at once, it might be overwhelming.
* Once you've figured out some areas you actually like, you can start digging in in that particular field.
* There are some great books on cryptography that you'll probably want to read eventually, so I'll go ahead and list some of them here:
   * Modern Cryptanlysis by Swenson. Obviously, I'm a bit biased here, but I have some decent introduction sections to many areas of cryptography and cryptanalysis with lots of examples in Python, and there are far worse places to start. I focus primarily on block ciphers (like AES) and public key cryptography (like RSA).
   * Applied Cryptography by Schneier. Extremely dated, but still has some useful stuff. A lot of block and stream cipher stuff.
   * Practical Cryptography by Schneier. A good companion to Applied Cryptography that is a bit more updated, with lots of focus on understanding and correctly using cryptography.
   * Algorithmic Cryptanalysis by Joux. One of the newest books, and chock full of good stuff, with a focus on public key cryptography, stream ciphers, and lattices. This one's probably one of the most advanced cryptography books on the market.
 
This list is not comprehensive: it's probably best to just look at all of the available books, glance through some of the pages and the table of contents, and see if the style, approach, and depth meet your interests.

## I know the basics, what next?

Once you know Crypto 101 and you want to dive into Crypto 201, where do you go?

One great next step is to work on [The Matasano Crypto Challenges](http://cryptopals.com/).
Not only will you have to learn a lot to complete them, but you'll have real experience making and breaking codes.
I think this is a great next-step for a would-be crypto enthusiast.
(And this is even a great step for cryptographers on any level &mdash; I certainly had fun doing them.)

There are some Coursera courses on Cryptography taught by Dan Boneh ([Cryptography I](https://www.coursera.org/course/crypto) and [Cryptography II](https://www.coursera.org/course/crypto2)).
I haven't taken them, but the instructor is top-notch, and the syllabi are solid.

## This part confuses me. Help!

I'm going to have some more blog posts in the near future clearning up some areas that I've seen be particularly sticky for some people.
In particular, I know that there are some sticky points in finite fields, RSA, and hashing that I think I can help clarify.