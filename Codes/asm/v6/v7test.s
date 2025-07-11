/* Test assmebly on ARMv7 */

	.global _start
_start:
	mov w0, 65
	mov w7, 1
	svc 0
