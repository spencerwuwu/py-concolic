(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun word () String)
(declare-fun abbr () String)

(assert (and (and (and (and (and (and (and (and (not (not (not (= (ite (not (= (str.at word 3) (str.at abbr 3))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 3) 1 0) 0)))) (not (not (= (ite (not (= (str.at word 2) (str.at abbr 2))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 2) 1 0) 0)))) (not (not (= (ite (not (= (str.at word 1) (str.at abbr 1))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 1) 1 0) 0)))) (not (not (= (ite (not (= (str.at word 0) (str.at abbr 0))) 1 0) 0)))) (not (not (= (ite (<= (str.len word) 0) 1 0) 0)))) (not (not (= (ite (<= (str.len abbr) 0) 1 0) 0)))))

(check-sat)

(get-value (word))
(get-value (abbr))