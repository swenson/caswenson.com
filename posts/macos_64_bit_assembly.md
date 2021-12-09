[DATE]: # (2018-02-06)

# 64-bit assembly language programming under macOS with NASM

Just a quick follow-up to a [previous post on 32-bit assembly language programming for OS X](http://caswenson.com/2009_09_26_assembly_language_programming_under_os_x_with_nasm.html).

I've had a fair amount of interest in this post, surprisingly, so I thought I would update it for the 64-bit Intel world we live in now.
The biggest change is that the calling convention now uses registers instead of the stack [by
default](https://courses.cs.washington.edu/courses/cse378/10au/sections/Section1_recap.pdf), and we
use the `r*` 64-bit registers instead of the `e*` 32-bit registers.

A huge source of annoyance for me is the way we pass pointers to data.
Now, in macOS, it is necessary for local data pointers to relative to the instruction pointer,
which is most easily accomplished using `rel your_data_here` and using `lea` instead of a
bare `mov`.
This can also be accomplished using the `DEFAULT REL` directive, which says that
all addresses in `lea` should be `rel`.

<pre name="code" class="nasm">
BITS 64
DEFAULT REL ; RIP-relative addressing by default
;
; Basic OS X calls to glibc
;
; compile with:
; nasm -g -f macho64 malloc64.asm
; gcc -o a.out malloc64.o
;

; glibc stuff
extern _puts, _printf, _malloc, _free

; static data
section .data

hello_world_str db "Hello world!", 10, 0
int_str db "Address %llx", 10, 0

; code
section .text

global _main

_main:
        ; save registers and align stack
        push rbp
        push r12
        push rbx

        lea  rdi, [hello_world_str]
        call _puts

        mov  rdi, 16
        call _malloc

        ; check if the malloc failed
        test rax, rax
        jz   fail_exit
        mov  rbx, rax

        xor  rax, rax
        mov  rsi, rbx
        lea  rdi, [int_str]
        call _printf

        ; print "A\nB\n..."
        mov [rbx], word 0xD41 ; 'A\n'

        mov r12, 10
_loop:
        mov  rdi, rbx
        call  _puts
        inc  qword [rbx]
        dec  r12
        jnz  _loop

        ; free the malloc'd memory
        mov  rdi, rbx
        call _free

        xor rax, rax
        pop rbx
        pop r12
        pop rbp
        ret

fail_exit:
        mov rax, 1
        pop rbx
        pop r12
        pop rbp
        ret
</pre>

The output should look something like this:

<pre>
Hello world!

Address 100200000
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
