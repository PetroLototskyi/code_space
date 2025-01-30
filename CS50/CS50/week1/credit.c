#include <cs50.h>
#include <stdio.h>

int main(void)
{

    long number, remainder;
    int modulo, sumEven = 0, sumOdd = 0, count = 0, verdict, befoLast;
    //Promt for input card number
    do
    {
        number = get_long("Number: ");
    }
    while (number <= 0);

    //Calculating of two sums (od and even)
    do
    {
        modulo = number % 10;
        remainder = number / 10;
        if (remainder < 100 && remainder > 10)
        {
            befoLast = remainder;
        }
        /* printf("Modulo is: %i\n", modulo);
        printf("Remainder is: %li\n", remainder); */
        number = remainder;
        //Calculation the sum of odd numbers
        if (count % 2 == 0)
        {
            sumOdd += modulo;
        }
        //Calculating the sum of Even numbers whick are *2
        else
        {
            // printf("Modulo is: %i\n", modulo);
            if (modulo < 5)
            {
                sumEven += modulo * 2;
            }
            //In case mpodule of number *2 is >9 the perfor this calculation
            else
            {
                sumEven += (modulo * 2) % 10 + (modulo * 2) / 10;
            }
        }
        count++;
    }
    while (remainder > 0);

    // printf("SumEven is: %i\n", sumEven);
    // printf("SumOdd is: %i\n", sumOdd);

    //Check if cad has legit number
    verdict = (sumEven + sumOdd) % 10;
    // printf("Verdict is: %i\n", verdict);
    if ((verdict == 0 && modulo == 4) && (count == 16 || count == 13))
    {
        printf("VISA\n");
    }
    else if ((verdict == 0 && count == 15) && (befoLast == 34 || befoLast == 37))
    {
        printf("AMEX\n");
    }
    else if (verdict == 0 && count == 16 && modulo == 5 && befoLast % 10 != 0 && befoLast % 10 < 6)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }


    // int secondNumber=befoLast%10;
    // for (int i=0; i<number; i++)
    // printf("Count is: %i\n", count);
    // printf("Before Last is: %i\n",befoLast);
    // printf("Second number is: %i\n",secondNumber);
}
