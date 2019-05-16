(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun K () Int)

(assert (not (not (not (= (ite (= (mod 7 K) 0) 1 0) 0)))))

(check-sat)

(get-value (K))