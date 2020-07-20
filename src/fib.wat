(func $fib (export "fib") (param $n i32) (result i32)
 (local.get $n)
 (i32.const 1)
 i32.le_s
 (if
  (result i32)
  (then (i32.const 1) return)
  (else
   (local.get $n)
   (i32.const 1)
   i32.sub
   (call $fib)
   (local.get $n)
   (i32.const 2)
   i32.sub
   (call $fib)
   i32.add
   return
  )
 )
)