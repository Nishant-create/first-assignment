#include <stdio.h>

int main() {
    int age = 15;

    if (age>10) {
        printf("Inside if condition\n");
        printf("Your age is greater than 10\n");
    } 
    if (age%5==0) {
        printf("You are insdie another if condition\n");
        printf("Your age is multiple of 5\n");
    }
    return 0;
}