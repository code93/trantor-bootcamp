#include <stdio.h>
#include <math.h>
#include <cs50.h>

 float getValue(void);
 int coins(int cents);


int main(void)
{

float owed = getValue();
int cents = round(owed * 100);
printf("%d\n", coins(cents));

}


float getValue(void)
{
    float change;
    do
    {
        change = get_float("Change owed: ");
    }
    while (change < 0.00);
return change;
}

int coins(int cents)
{
    int count = 0;

    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents -= 25;
            count++;
        }
        else if (cents >= 10)
        {
            cents -= 10;
            count++;
        }
        else if (cents >= 5)
        {
            cents -= 5;
            count++;
        }
        else
        {
            cents -= 1;
            count++;
        }
    }
    return count;
}