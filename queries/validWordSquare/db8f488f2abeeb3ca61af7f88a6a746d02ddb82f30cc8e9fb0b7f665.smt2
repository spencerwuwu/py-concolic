
(declare-fun in1 () String)
(declare-fun in0 () String)

(assert (and (and (and (and (and (not (not (not (= (ite (not (= (str.at in1 1) (str.at in1 1))) 1 0) 0)))) (not (not (= (ite (<= (str.len in1) 1) 1 0) 0)))) (not (not (= (ite (<= (str.len in1) 1) 1 0) 0)))) (not (not (= (ite (not (= (str.at in0 1) (str.at in1 0))) 1 0) 0)))) (not (not (= (ite (<= (str.len in1) 0) 1 0) 0)))) (not (not (= (ite (<= (str.len in0) 1) 1 0) 0)))))

(check-sat)

(get-value (in1))
(get-value (in0))



