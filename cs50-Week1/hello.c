#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int i;
    int j;
    int k;
    int height=get_int("Height:");

    for (i=1; i <= height; i++)
        {

            for(k = height-i ; k >= 0; k--){
                printf(" ");
            }

            for (j=1; j <= i; j++)
            {
            printf("#");

            }
            printf("\n");
        }

}