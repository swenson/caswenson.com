Assembly language programming under OS X with NASM
==================================================
One of my favorite passions from my teenage days was assembly language programming.  Don't laugh.

It embodies a lot of my favorite things about programming: I have total control, it is clean and simple, and it is just and fast and functional as I am capable of making it.  The only thing standing in the way of me and world domination is how well I can program.

Well, with some minor exceptions.  Having a decent assembler is really key, and for x86 architectures, there are many choices.  If you are hacking a small function together to support some higher-level language, then maybe you can get by using <a href="http://en.wikipedia.org/wiki/Microsoft_Macro_Assembler">MASM</a> (for Windows/DOS), or, if you really hate yourself, <a href="http://en.wikipedia.org/wiki/GNU_Assembler">gas</a> (for every platform).

But, if you intend to spend some time programming in assembly and not hating every minute of it, then you need to use <a href="http://en.wikipedia.org/wiki/Netwide_Assembler">NASM</a>, probably the best assembler for the x86 family, ever (or possibly <a href="http://en.wikipedia.org/wiki/Yasm">Yasm</a>, a NASM clone that I have no experience with).

So, this past week I was interested in playing some more with NASM, and so I thought that I would see how what I could do under OS X (I previously worked primarily in DOS).  Unfortunately, assembly language support in OS X is fairly hampered if you want follow its <a href="http://developer.apple.com/mac/library/DOCUMENTATION/DeveloperTools/Conceptual/LowLevelABI/130-IA-32_Function_Calling_Conventions/IA32.html#//apple_ref/doc/uid/TP40002492-SW4">standard calling conventions</a> for 32-bit x86 code.  The innocuous-looking statement "The stack is 16-byte aligned at the point of function calls" seems innocent, but is a nightmare if you using external calls.

Basically, this means that you have to keep very close track of your stack size when calling functions.  And even worse is that your stack never enters your function correctly aligned: the return address is always 4 bytes long, meaning you are always 12 bytes off when you start.

What this means is that I may have to use a VM with Linux to have any fun with assembly language programming again.

If anyone is interested, here is a quick NASM file I threw together that demonstrates how to use NASM on OS X to call glibc functions.  I tested it with the latest NASM (2.07) on Snow Leopard (you'll probably need XCode installed to get this to work).  This program prints "Hello World", allocates some memory using <code>malloc</code>, uses that memory to write 10 letters of the alphabet on the screen (using <code>printf</code>), <code>free</code>s the memory, and returns.

<pre name="code" class="nasm">
;
; Basic OS X calls to glibc
;
; compile with:
; nasm -g -f macho malloc.asm
; gcc -o a.out malloc.o
;
 
; glibc stuff
extern _puts, _printf, _malloc, _free
 
; static data
segment .data
 
hello_world_str db "Hello world!", 10, 0
int_str db "Address %x", 10, 0
 
; code
segment .text
 
global _main
 
_main:
        push ebp ; setup the frame
        mov  ebp, esp
 
        sub  esp, 4 ; align the stack
        push dword hello_world_str
        call _puts
        add  esp, 4
 
        ; malloc 16 bytes
        push  dword 16
        call  _malloc
        add  esp, 4
 
        ; check if the malloc failed
        test  eax, eax
        jz    fail_exit
         
        sub   esp, 0xC ; align the stack
        mov   ebx, eax
        push  ebx
        push  dword int_str
        call  _printf
        add   esp, 8
        add   esp, 0xC
 
        ; print "A\nB\n..."     
        mov   [ebx], dword 0xD41 ; 'A\n'
 
        mov   edi, 10
        push  ebx
_loop:
        call  _puts
        inc  dword [ebx] 
        dec  edi 
        jnz  _loop
 
        add  esp, 4
         
        ; free the malloc'd memory
        push  ebx
        call  _free
        add  esp, 4
        add  esp, 4 ; cleanup the stack 
        pop  ebp
        ret
         
fail_exit:
        mov  eax, 1
        pop  ebp
        ret
</pre>

The output should look something like this:

<pre>Hello world!
 
Address 100130
A
B
C
D
E
F
G
H
I
J
</pre>

Am I the only one who likes assembly language programming these days?