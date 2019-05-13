(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun s () String)
(declare-fun t () String)

(assert (and (and (and (and (and (not (not (= (ite (= (str.len s) 1) 1 0) 0))) (not (not (= (ite (> (str.len s) 1) 1 0) 0)))) (not (= (ite (= (str.at s 0) (str.at t 0)) 1 0) 0))) (not (= (ite (> (str.len s) 0) 1 0) 0))) (not (not (= (ite (> (- (str.len t) (str.len s)) 1) 1 0) 0)))) (not (not (= (ite (> (str.len s) (str.len t)) 1 0) 0)))))

(check-sat)

(get-value (s))
(get-value (t))