int fibonacci (n) {
    int fib_one,fib_two,fib ;
    fib_one = 0 ;
    fib_two = 1 ;
    int i = 0 ;
    while (i < n+1) {
        if ( i == 0 ) {
            fib = fib_one ;
        }   
        else {
            if ( i == 1 ) {
                fib = fib_two ;
            }
            else {
                fib = fib_one + fib_two ;
                fib_one = fib_two ;
                fib_two = fib ;
            }
        }
    i = i+1 ;     
    }
    return fib ;
}

fibonacci(100) ;
