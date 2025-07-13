/* Recreating the first example program from chapter 3 of asm for rpi */

	.global _start

_start:
	mov x0, #26
	mov x7, #1
	svc 0
