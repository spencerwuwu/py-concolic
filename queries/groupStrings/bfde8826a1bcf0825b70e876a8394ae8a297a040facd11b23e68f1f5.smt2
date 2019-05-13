(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun in0 () String)

(assert (and (not (not (not (= (ite (= (str.len in0) 1) 1 0) 0)))) (not (not (= (ite (= (str.len in0) 0) 1 0) 0)))))

(check-sat)

(get-value (in0))