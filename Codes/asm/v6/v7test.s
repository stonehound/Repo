/* Test assmebly on ARMv7 */

	.global _start
_start:
	mov x0, #65
	mov x7, #1
	svc 0
