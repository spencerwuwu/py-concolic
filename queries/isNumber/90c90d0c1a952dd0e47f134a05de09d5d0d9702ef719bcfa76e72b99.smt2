(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun s () String)

(assert (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (not (not (not (= (ite (> (str.len s) 6) 1 0) 0)))) (not (= (ite (> (str.len s) 5) 1 0) 0))) (not (= (ite (> (str.len s) 4) 1 0) 0))) (not (= (ite (> (str.len s) 3) 1 0) 0))) (not (= (ite (> (str.len s) 2) 1 0) 0))) (not (= (ite (> (str.len s) 1) 1 0) 0))) (not (= (ite (> (str.len s) 0) 1 0) 0))) (not (not (= (ite (= (str.at s 0) "-") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) "+") 1 0) 0)))) (not (not (= (ite (= (str.len s) 0) 1 0) 0)))) (not (not (= (ite (= (str.at s (- (str.len s) 1)) "\f") 1 0) 0)))) (not (not (= (ite (= (str.at s (- (str.len s) 1)) "\v") 1 0) 0)))) (not (not (= (ite (= (str.at s (- (str.len s) 1)) "\r") 1 0) 0)))) (not (not (= (ite (= (str.at s (- (str.len s) 1)) "\n") 1 0) 0)))) (not (not (= (ite (= (str.at s (- (str.len s) 1)) "\t") 1 0) 0)))) (not (not (= (ite (= (str.at s (- (str.len s) 1)) " ") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) "\f") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) "\v") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) "\r") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) "\n") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) "\t") 1 0) 0)))) (not (not (= (ite (= (str.at s 0) " ") 1 0) 0)))) (not (not (= (ite (= (str.len s) 0) 1 0) 0)))))

(check-sat)

(get-value (s))