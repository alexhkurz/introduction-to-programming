# include <stdio.h>

int n = 1 ;

void f(){
    n = 2 ; 
    printf("%d\n",n) ;
}

int main() {
    printf("%d\n",n) ;
    f() ;
    printf("%d\n",n) ;
}