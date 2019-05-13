(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun in0 () String)
(declare-fun in1 () String)

(assert (and (and (and (and (and (and (and (and (and (and (not (not (not (= (ite (not (= (str.at in0 4) (str.at in1 4))) 1 0) 0)))) (not (= (ite (> (str.len in0) 4) 1 0) 0))) (not (not (= (ite (not (= (str.at in0 3) (str.at in1 3))) 1 0) 0)))) (not (= (ite (> (str.len in0) 3) 1 0) 0))) (not (not (= (ite (not (= (str.at in0 2) (str.at in1 2))) 1 0) 0)))) (not (= (ite (> (str.len in0) 2) 1 0) 0))) (not (not (= (ite (not (= (str.at in0 1) (str.at in1 1))) 1 0) 0)))) (not (= (ite (> (str.len in0) 1) 1 0) 0))) (not (not (= (ite (not (= (str.at in0 0) (str.at in1 0))) 1 0) 0)))) (not (= (ite (> (str.len in0) 0) 1 0) 0))) (not (not (= (ite (< (str.len in1) (str.len in0)) 1 0) 0)))))

(check-sat)

(get-value (in0))
(get-value (in1))