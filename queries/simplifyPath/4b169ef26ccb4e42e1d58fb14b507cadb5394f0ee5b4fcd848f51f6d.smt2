
(declare-fun path () String)

(assert (and (and (not (not (= (ite (not (= (str.len path) 0)) 1 0) 0))) (not (not (= (ite (str.contains path "/") 1 0) 0)))) (not (not (= (ite (= (str.len path) 0) 1 0) 0)))))

(check-sat)

(get-value (path))



