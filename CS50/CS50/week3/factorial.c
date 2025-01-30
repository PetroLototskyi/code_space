#include <cs50.h>
#include <stdio.h>

int factorial (int number);
int main (void)
{
    // ptomt for number
    int n=get_int("Type a number: ");
    printf ("%i\n", factorial(n));

}

int factorial (int number)
{
    if (number ==1)
    {
        return 1;
    }
    else
    {
        number*=factorial(number -1);
    }
    return number;
    /*
    int solution =number;
    for (int i=number-1; i>0; i-- )
    {
        solution=solution*i;
    }
    */
}