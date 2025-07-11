/* This is the first part of the  second example in chapter 3 of asm for rpi */

	.global _start

_start:
	mov r0, #65 
	bal _part2
