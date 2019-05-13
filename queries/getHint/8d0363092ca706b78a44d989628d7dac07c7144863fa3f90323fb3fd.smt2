(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun guess () String)
(declare-fun secret () String)

(assert (and (not (not (= (ite (= (str.at guess 0) (str.at secret 0)) 1 0) 0))) (not (not (= (ite (<= (str.len secret) 0) 1 0) 0)))))

(check-sat)

(get-value (guess))
(get-value (secret))