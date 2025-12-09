(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cadar x) (car (cdr (car x))))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 13
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 13
  (define (enumerate_helper index s)
    (if (null? s)
      '()
      (cons (list index (car s)) (enumerate_helper (+ index 1) (cdr s)))
      )
    )
  (enumerate_helper 0 s)
  ; END PROBLEM 13
  )


;; Problem 14

;; Return the value for a key in a dictionary list
(define (get dict key)
  ; BEGIN PROBLEM 14
  (if (null? dict)
    #f
    (if (eq? (caar dict) key)
      (cadar dict)
      (get (cdr dict) key)
      )
    )
  ; END PROBLEM 14
  )

;; Return a dictionary list with a (key value) pair
(define (set dict key val)
  ; BEGIN PROBLEM 14
  (if (null? dict)
    (cons (list key val) nil)
    (if (eq? (caar dict) key)
      (cons (list key val) (cdr dict))
      (cons (car dict) (set (cdr dict) key val))
      )
    )
  ; END PROBLEM 14
  )

;; Problem 15
(define (solution-code problem solution)
(map (lambda (item)
       (if (and (list? item) (not (null? item)))
           (solution-code item solution)   ; recurse into sublist
           (if (eq? item '_____)
               solution
               item)))
     problem))
