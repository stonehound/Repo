/*This is practice using all of the functions from the math library in C.*/
#include <math.h>
#include <stdio.h>

int main()
{
	/*Ceil() Example:*/
	printf("This is the Ceil() example:\n");
	/*Here is an example of a double precision floating-point variable.*/
	double fivesevenths = 5/7;
	/*To input double precision floating-point variable into the printf() function, use (%.1lf).*/
	printf("Rounding up %.1lf, gets you %.1lf.\n", fivesevenths, ceil(fivesevenths));
	/*Floor() Example:*/



	return 0;
}
