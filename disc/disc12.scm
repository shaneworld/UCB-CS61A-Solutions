(define-macro (mystery-macro expr old new)
    (mystery-helper expr old new))

(define (mystery-helper e o n)
  (if (and (list? e) (not (null? e)))
      (cons (mystery-helper (car e) o n) (mystery-helper (cdr e) o n))
      (if (eq? e o) n e)))



(define-macro (assign sym1 sym2 expr1 expr2)
  `(let ((temp1 ,expr1)
         (temp2 ,expr2))
     (begin
       (define ,sym1 temp1)
       (define ,sym2 temp2))))


(define-macro (switch expr cases)
  `(begin
     (define val ,expr)
     ,(cons
       'cond
       (map (lambda (case)
              (cons
               `(equal? val ,(car case))
               (cdr case)))
            cases))))
