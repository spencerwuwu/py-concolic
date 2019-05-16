(set-logic ALL_SUPPORTED)
(set-option :strings-exp true)
(set-option :produce-models true)
(set-option :rewrite-divk true)

(declare-fun digits () String)

(assert (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (and (not (not (= (ite (= (str.at (str.substr (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1)) 1 (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1)) 0) "5") 1 0) 0))) (not (= (ite (= (str.len (str.substr (str.substr (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1)) 1 (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1)) 1 (- (str.len (str.substr (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1)) 1 (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1))) 1))) 0) 1 0) 0))) (not (not (= (ite (= (str.len (str.substr (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1)) 1 (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1))) 0) 1 0) 0)))) (not (not (= (ite (= (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 0) 1 0) 0)))) (not (not (= (ite (= (str.len (str.substr digits 1 (- (str.len digits) 1))) 0) 1 0) 0)))) (not (not (= (ite (= (str.len digits) 0) 1 0) 0)))) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1)) 1 (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr (str.substr digits 1 (- (str.len digits) 1)) 1 (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)) (>= 1 0)) (>= (- (str.len (str.substr digits 1 (- (str.len digits) 1))) 1) 0)) (>= 1 0)) (>= (- (str.len digits) 1) 0)))

(check-sat)

(get-value (digits))