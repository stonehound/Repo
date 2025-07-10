/* Test assembly code, first example in chapter 3 of asm for rpi */

	.global _start
_start:
	MOV R0, #65
	MOV R7, #1
	SWI 0
