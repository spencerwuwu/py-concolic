
(declare-fun s () String)

(assert (and (and (and (and (and (and (not (not (= (ite (= (str.len (str.substr s 0 (- 1 0))) 1) 1 0) 0))) (not (= (ite (<= (- (- (- (str.len s) 1) 1) 1) 3) 1 0) 0))) (not (= (ite (> (- (- (- (str.len s) 1) 1) 1) 0) 1 0) 0))) (not (not (= (ite (> (str.len s) 12) 1 0) 0)))) (not (not (= (ite (= (str.len s) 0) 1 0) 0)))) (>= 0 0)) (>= (- 1 0) 0)))

(check-sat)

(get-value (s))



