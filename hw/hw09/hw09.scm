(define (curry-cook formals body)
(if (null? formals)
    body
    (let ((first (car formals))
          (rest  (cdr formals)))
      `(lambda (,first)
         ,(curry-cook rest body)))))

(define (curry-consume f args)
  (if (null? args)
      f
      (curry-consume ((if (procedure? f) f (eval f)) (car args))
                     (cdr args))))

(define-macro (switch expr options) (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map
         (lambda (option) 
           (cons (list 'equal? (car (cdr switch-expr)) (car option))
                 (cdr option)))
         (car (cdr (cdr switch-expr))))))
