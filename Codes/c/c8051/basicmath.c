/*Trying to get the hang of C through trying out it's basic math functions.*/
/*Standard Input/Output Library.*/
#include <stdio.h>
/*Main function.*/
int main ()
{
	/*Print code introduction.*/
	printf("This is an attempt to practice the use of all of the basic mathematical operations in C.\n");
	/*Set up two integer variables for two and three.*/
	int two = 2;
	int three = 3;
	/*Print the contents of the variables for mathematics, 
	 *notice the (%d) enables you to print integer variables.*/
	printf("Here are the contents of the variables representing the numbers %d", two);
	printf(" and %d", three);
	printf(".\n");
	/*Addition example:*/
	/*Here is an example of creating an integer variable that depends on the values of two other variables.*/
	int five  = two + three;
	printf("This is the example of addition, %d", two);
	printf(" plus %d", three);
	printf(" equals %d", five);
	printf(".\n");
	/*Subtraction example:*/
	int negativeone = two - three;
	printf("This is the example of subtraction, %d", two);
	printf(" minus %d", three);
	printf(" equals %d", negativeone);
	printf(".\n");
	/*Multiplication example:*/
	int six = two * three;
	printf("This is the example of multiplication, %d", two);
	printf(" times %d", three);
	printf(" equals %d", six);
	printf(".\n");
	/*Modulus example:*/
	int one = three % two;
	printf("This is the example of modulus division, the remainder of %d", three);
	printf(" divided by %d", two);
	printf(" is %d", one);
	printf(".\n");
	/*Division Example*/
	/*Set up a floating-point variables.*/
	float twof = 2;
	float threef = 3;
	float twothirds = twof / threef;
	/*Notice the (%f) enables you to print floating-point variables.*/
	printf("This is the example of division, %f", twof);
	printf(" divided by %f", threef);
	printf(" equals %f", twothirds);
	printf(".\n");
	/* example:*/
}
