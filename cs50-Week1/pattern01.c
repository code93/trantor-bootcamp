#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int i;
    int j;
    int height=get_int("Height:");

    for(i=0; i< height; i++){
        for(j=0; j<= i; j++){
            printf("#");
        }
        printf("\n");
    }
}