/*Trying to create a function that will print the fibonacci sequence up to the input ter.m*/
# include  <math.h>
# include <stdio.h>
/*Defining fibonacci function.*/
int fibonacci(int t)
{
	if(t == 0)
		return 0;
	else if(t == 1)
		return 1;
	else
		return fibonacci(t - 1) + fibonacci(t - 2);
}
/*The main calling of printf and the fibonacci function.*/
int main()
{
	printf("This is the fibonacci sequence function test.\n");
	printf("The first term of the fibonacci sequence is %d", fibonacci(0));
	printf(".\n");
	printf("The second term in the fibonacci sequence is %d", fibonacci(1));
	printf(".\n");
	printf("The third term in the fibonacci sequence is %d", fibonacci(2));
	printf(".\n");
	printf("The fourth term in the fibonacci sequence is %d", fibonacci(3));
	printf(".\n");
	printf("The fifth term in the fibonacci sequence is %d", fibonacci(4));
	printf(".\n");
	printf("The sixth term in the fibonacci sequence is %d", fibonacci(5));
	printf(".\n");
	printf("The seventh term in the fibonacci sequeence is %d", fibonacci(6));
	printf(".\n");
	printf("The eighth term in the fibonacci sequence is %d", fibonacci(7));
	printf(".\n");
	printf("The twentieth term in the fibonacci sequence is %d", fibonacci(19));
	printf(".\n");
}
