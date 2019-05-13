(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun str () String)

(assert (and (not (not (not (= (ite (str.contains str " ") 1 0) 0)))) (not (not (= (ite (= (str.len str) 0) 1 0) 0)))))

(check-sat)

(get-value (str))