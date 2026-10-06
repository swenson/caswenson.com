# A Rust RISC-V Disassembler

When I was working on [Caliptra](https://caliptra.io), an open source silicon root of trust, I needed a Rust RISC-V disassembler to embed in our emulator to help with debugging. There was some Rust source code out there (such as Oxide Computer Company's [disc-v](https://github.com/oxidecomputer/disc-v) source) but it was unlicensed, not published as a crate, as out of date. So at the time, I just redid the work of converting the same underlying C library to Rust (with some automation, but mostly by hand), and let it sit in the Caliptra's repositories, as I never really had time to polish it and publish a crate, and the Caliptra project probably didn't want to maintain that crate.

Fast forward to now, when I potentially need that same disassembler again, but still no great RISC-V disassembly crate exists. But! The Caliptra source I made before is open source! I can just fork it, clean it up a bit, and repackage it, and I can publish it myself (with appropriate attribution and licensing).

In the age of AI, there are far fewer excuses for not cleaning up that code, publishing it, and keeping it up-to-date. As the [Oxide folks would say](https://oxide-and-friends.transistor.fm/episodes/engineering-rigor-in-the-llm-age), let's use the AI tools to add more rigor and maintainability to our open source.

Now live at [https://crates.io/crates/disc-v/](https://crates.io/crates/disc-v/) -- many thanks to the folks I worked with on the Caliptra project for all of the work done on that open source module.