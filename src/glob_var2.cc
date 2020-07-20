# include <stdio.h>


int main() {

    void f(){
        n = 2 ; 
        printf("%d\n",n) ;
    }

    int n = 1 ;
    printf("%d\n",n) ;
    f() ;
    printf("%d\n",n) ;
}