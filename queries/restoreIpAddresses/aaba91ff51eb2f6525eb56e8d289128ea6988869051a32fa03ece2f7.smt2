(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun s () String)

(assert (and (and (and (and (not (not (not (= (ite (> (- (- (- (str.len s) 1) 1) 3) 0) 1 0) 0)))) (not (not (= (ite (> (- (- (- (str.len s) 1) 1) 2) 0) 1 0) 0)))) (not (not (= (ite (> (- (- (- (str.len s) 1) 1) 1) 0) 1 0) 0)))) (not (not (= (ite (> (str.len s) 12) 1 0) 0)))) (not (not (= (ite (= (str.len s) 0) 1 0) 0)))))

(check-sat)

(get-value (s))