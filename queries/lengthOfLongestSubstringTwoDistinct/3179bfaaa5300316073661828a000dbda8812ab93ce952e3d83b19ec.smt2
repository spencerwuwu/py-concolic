(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun s () String)

(assert (and (and (and (and (and (not (not (= (ite (not (= (str.at s 1) (str.at s 3))) 1 0) 0))) (not (not (= (ite (= (str.at s 3) (str.at s 2)) 1 0) 0)))) (not (= (ite (not (= (str.at s 0) (str.at s 2))) 1 0) 0))) (not (not (= (ite (= (str.at s 2) (str.at s 1)) 1 0) 0)))) (not (not (= (ite (= (str.at s 1) (str.at s 0)) 1 0) 0)))) (not (not (= (ite (<= (str.len s) 1) 1 0) 0)))))

(check-sat)

(get-value (s))