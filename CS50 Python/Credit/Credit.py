#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //variables
    char strcredit[100];
    long credit = 0;
    //initial function - ask user
    while(credit == 0){
        credit = get_long("Credit/Debit Card Number: ");
        sprintf(strcredit, "%ld", credit); //convert long to string thanks to stackoverflow
    }

    char first = strcredit[0];
    char second = strcredit[1];
    long x = credit;
    int len = 0;
    if(x>=10000000000000000)
        len = 17;
    else if(x>=1000000000000000)
        len = 16;
    else if(x>=100000000000000)
        len = 15;
    else if(x>=10000000000000)
        len = 14;
    else if(x>=1000000000000)
        len = 13;
    else if(x>=100000000000)
        len = 12;
    else if(x>=10000000000)
        len = 11;
    else if(x>=1000000000)
        len = 10;
    else if(x>=100000000)
        len = 9;
    else if(x>=10000000)
        len = 8;
    else if(x>=1000000)
        len = 7;
    else if(x>=100000)
        len = 6;
    else if(x>=10000)
        len = 5;
    else if(x>=1000)
        len = 4;
    else if(x>=100)
        len = 3;
    else if(x>=10)
        len = 2;
    else
        len = 1;

    char last = strcredit[len-1];

    if(first == '4'){
        if(len == 13 || len == 16)
            if(last == '3'){
                printf("INVALID\n");
            }
            else{
                printf("VISA\n");
            }
        else
            printf("INVALID\n");
    }
    else if(first == '5'){
        if(second == '1' || second == '2' || second == '3' || second == '4' || second == '5'){
            if(len == 16)
                printf("MASTERCARD\n");
            else
                printf("INVALID\n");
        }
        else{
            printf("INVALID\n");
        }
    }
    else if(first == '3'){
            if(second == '4' || second == '7'){
                if(len == 15)
                    printf("AMEX\n");
                else
                    printf("INVALID\n");
            }
            else{
                printf("INVALID\n");
            }
        }
    else{
        printf("INVALID\n");
    }

}
