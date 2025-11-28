(define (square n) (* n n))

(define (pow base exp)
  (cond
    ((= exp 0) 1)  ; Base case: x^0 = 1
    ((even? exp)   (square (pow base (/ exp 2))))  ; Even exponent: (x^y)^2
    (else          (* base (square (pow base (/ (- exp 1) 2)))))))  ; Odd exponent: x * (x^y)^2

(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (repeatedly-cube (- n 1) (expt x 3))))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))
