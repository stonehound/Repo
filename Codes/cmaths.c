//This is a C code to test the functions within the math.h library.
#include <stdio.h>
#include <math.h>
//Main loop:
int main()
{
	//Set up integer variables.
	int two = 2;
	int three = 3;
	int four = 4;
	int eight  = two * four;
	//Print product of two and four.
	printf("The product of %d and %d, is %d", two, four, eight);
	printf("\n");
	//Print square root of eight, notice that the sqrt() function will take an int value and product a float.
	printf("The square root of the product is %f", sqrt(eight));
	printf("\n");

	return 0;
}
