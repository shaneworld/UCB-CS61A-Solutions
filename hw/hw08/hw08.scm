(define (ascending? s) 
  (if (or (null? s) (null? (cdr s)))
    #t
    (if (< (car (cdr s)) (car s))
      #f
      (ascending? (cdr s))
      )
    )
  )


(define (my-filter pred s)
  (if (null? s)
    '()
    (if (pred (car s))
      (cons (car s) (my-filter pred (cdr s)))
      (my-filter pred (cdr s))
      )
    )
  )

(define (interleave lst1 lst2)
  (cond 
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
    )
  )

(define (no-repeats s)
  (if (null? s)
    '()
    (cons 
      (car s)
      (filter
        (lambda (x) (not (eq? x (car s))))
        (no-repeats (cdr s))
        )
      )
    )
  )
