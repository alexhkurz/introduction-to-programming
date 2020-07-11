# include <stdio.h>

int fib(int n) {
    if (n <= 1)
        return 1 ;
    else
        return fib(n-1) + fib(n-2) ;
}

int main() {
    printf("Fibonacci of %d is %d\n",10,fib(10)) ;
}