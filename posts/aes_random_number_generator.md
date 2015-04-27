# An simple AES-based random number generator

When browsing through some stack traces doing Go development, I noticed that Go had done something rather
clever in their codebase: on x86-64 processors, they used
[the AES instruction set](http://en.wikipedia.org/wiki/AES_instruction_set)
[to build a hash function](https://github.com/golang/go/blob/7a4a64e8f3dc14717695e53c7560992789f8bc9e/src/runtime/asm_amd64.s#L874).

The more I've thought about it, the more this is potentially quite brilliant.
AES, the block cipher, compounds multiple rounds of mixing data together, shuffling bits around, and
transforming it.
For the past several years, all Intel and AMD processors have supported doing an AES round in
a single instruction.

Hashing and random number generation use the same sort of principles as AES is based on: basically,
shuffle bits around and transform them.
AES gets cryptographic strength by doing this many times in a row (usually 10+).

However, if we are building a [hash table](http://en.wikipedia.org/wiki/Hash_table) or generating random numbers for simulations (or other non-cryptographic uses), then we don't need the full cryptographic strength of AES.
But, we can still leverage the AES instruction set to build some fast random number generators and hashes.

For starters, I've gone ahead and written [an AES-based random number generator](https://github.com/swenson/aesrng) that performs a single round of AES as its core, and iterates to produce more random numbers.

In practice, it is about twice as fast as the [Mersenne Twister](http://en.wikipedia.org/wiki/Mersenne_twister).

I think that the biggest reason that most people haven't done this is that it's a relatively new feature, and
doing CPUID detection to make sure that the AES instruction set is available at runtime is kind of annoying.
At the very least, this library has those pieces already written.

Some caveats:

* The quality of random numbers produced is not as high as the mersenne twister (they don't *quite* pass the [dieharder](http://www.phy.duke.edu/~rgb/General/dieharder.php) test suite).
  They're not terrible either; they're just not as good.
* This only works on relatively modern x86-64 processors.
  To detect support, you can use the included `cpuid.h` to call `intel_has_feature(INTEL_FEATURE_AES)`
  to see if the `CPUID` instruction indicates support for the AES instruction set.
* It's very probably that more performance or better numbers could be created.
  I used a fairly straightforward seed and random number generator.

I've also been experimenting with an AES-based hash function that is extremely similar to this.
There is an equivalent test set to the Diehard tests for hash functions, called [SMHasher](https://code.google.com/p/smhasher/).

Unfortunately, my preliminary results are not encouraging: AES instructions are possibly slower
than the Murmur3 algorithm when tuned to pass the SMHasher tests.
With only 1 or 2 rounds of encryption used, my AES hash function does not seem to pass the
SMHasher suite, though it does after 3 or 4 rounds.
Unfortunately, these extra rounds make the performance not quite as competitive.

I'm still tinkering with the AES-based hash function though to try to make it faster
or hash better. I'll report back with my findings.
