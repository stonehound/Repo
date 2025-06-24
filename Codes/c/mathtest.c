//This is a C code to test functions from the math.h library.  
#include <stdio.h>
#include <math.h>

//Main loop:
int main()
{
printf("This is a C code meant to practice using the functions found within the math.h library.\n");
//Create variables.
printf("The first step is to create some variables to use as inputs for the functions.\n");
printf("Here we create integer varaibles for 2, 3, 4, 2 times 3, and -3.\n");
int two = 2;
int three = 3;
int four = 4;
int eight = two*four;
int negthree = -3;

float ftwo = 2;
float fthree = 3;
float fnegthree = -3;
printf("Some functions only accept floating point variable inputs, so here are examples such a variables for %f, %f, and %f.\n", ftwo, fthree, fnegthree);

printf("While C is predefined in C as 'M_PI', with a value %f, but can be approximated as acos(0) = %f.\n", M_PI, 2*acos(0));
float pi = 2*acos(0);

printf("Now we'll begin testing the various functions in the m ath.h library:\n");
//Print the product of two and four.
printf("The product of %d and %d is %d.\n", two, four, eight);

//Find the square root of eight.
printf("The square root of %d is %f.\n", eight, sqrt(eight)); 

//Find the cube root of eight.
printf("The cube root of %d is %f.\n", eight, cbrt(eight));

//Round the square root of eight up and down.
printf("The square root of %d rounded up is %f.\n", eight, ceil(sqrt(eight)));
printf("The square root of %d rounded down is %f.\n", eight, floor(sqrt(eight)));

//Find the absolute value of negative three.
printf("The absolute value of %f is %f.\n", fnegthree, fabs(fnegthree));

//Find the truncated version of pi.
printf("The truncated version of %f, is %f.\n", pi, trunc(pi));

//Find the nearest integer to pi. Returns a float.
printf("The nearest integer to %f, represented as a float, is %f.\n", pi, nearbyint(pi));

//Find the nearest integer to pi. Returns an int. This is also a means of converting a float to an int.
printf("The nearest integer to %f, represented as an int, is %d.\n", pi, lround(pi));

//Find the remainder of (pi/3).
printf("The remainder of dividing %f by %f is %f.\n", pi, fthree, remainder(pi, fthree));
printf("The remainder of dividing %f by %f is %f.\n", fthree, ftwo, remainder(fthree, ftwo));
printf("The remainder of dividing %d by %d in %f.\n", four, three, remainder(four, three));

return 0;
}

