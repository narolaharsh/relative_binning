(2, -2, 1): lambda c, s: 2*c*s**3
(2, -2, 2): lambda c, s: s**4

(2, -1, 1): lambda c, s: s**2*(3*c**2-s**2)
(2, -1, 2): lambda c, s: 2*c*s**3

(2, 0, 1): lambda c, s: np.sqrt(6)*(c**3*s-c*s**3)
(2, 0, 2): lambda c, s: np.sqrt(6)*c**2*s**2

(2, 1, 1): lambda c, s: c**2*(c**2-3*s**2)
(2, 1 ,2): lambda c, s: 2*c**3*s

(2, 2, 1): lambda c, s: -2*c**3*s
(2, 2, 2): lambda c, s: c**4


(3, -3, 1): lambda c, s: 0.
(3, -3, 2): lambda c, s: np.sqrt(6)*c*s**5
(3, -3, 3): lambda c, s: s**6

(3, -2, 1): lambda c, s: 0.
(3, -2, 2): lambda c, s: s**4*(5*c**2-s**2)
(3, -2, 3): lambda c, s: np.sqrt(6)*c*s**5

(3, -1, 1): lambda c, s: 0.
(3, -1, 2): lambda c, s: np.sqrt(10)*s**3*(2*c**3-c*s**2)
(3, -1, 3): lambda c, s: np.sqrt(15)*c**2*s**4

(3, 0, 1): lambda c, s: 0.
(3, 0, 2): lambda c, s: np.sqrt(30)*c**2*s**2*(c**2-s**2)
(3, 0, 3): lambda c, s: 2*np.sqrt(5)*c**3*s**3

(3, 1, 1): lambda c, s: 0.
(3, 1, 2): lambda c, s: np.sqrt(10)*c**3*(c**2*s-2*s**3)
(3, 1, 3): lambda c, s: np.sqrt(15)*c**4*s**2

(3, 2, 1): lambda c, s: 0.
(3, 2, 2): lambda c, s: c**4*(c**2-5*s**2)
(3, 2, 3): lambda c, s: np.sqrt(6)*c**6*s

(3, 3, 1): lambda c, s: 0.
(3, 3, 2): lambda c, s:	-np.sqrt(6)*c**5*s
(3, 3, 3): lambda c, s: c**6


(4, -4, 1): lambda c, s: 0.
(4, -4, 2): lambda c, s: 0.
(4, -4, 3): lambda c, s: 0.
(4, -4, 4): lambda c, s: s**8

(4, -3, 1): lambda c, s: 0.
(4, -3, 2): lambda c, s: 0.
(4, -3, 3): lambda c, s: 0.
(4, -3, 4): lambda c, s: 2*np.sqrt(2)*c*s**7

(4, -2, 1): lambda c, s: 0.
(4, -2, 2): lambda c, s: 0.
(4, -2, 3): lambda c, s: 0.
(4, -2, 4): lambda c, s: 2*np.sqrt(7)*c**2*s**6

(4, -1, 1): lambda c, s: 0.
(4, -1, 2): lambda c, s: 0.
(4, -1, 3): lambda c, s: 0.
(4, -1, 4): lambda c, s: 2*np.sqrt(14)*c**3*s**5

(4, 0, 1): lambda c, s: 0.
(4, 0, 2): lambda c, s: 0.
(4, 0, 3): lambda c, s: 0.
(4, 0, 4): lambda c, s: np.sqrt(70)*c**4*s**4

(4, 1, 1): lambda c, s: 0.
(4, 1, 2): lambda c, s: 0.
(4, 1, 3): lambda c, s: 0.
(4, 1, 4): lambda c, s: 2*np.sqrt(14)*c**5*s**3

(4, 2, 1): lambda c, s: 0.
(4, 2, 2): lambda c, s: 0.
(4, 2, 3): lambda c, s: 0.
(4, 2, 4): lambda c, s: 2*np.sqrt(7)*c**6*s**2

(4, 3, 1): lambda c, s: 0.
(4, 3, 2): lambda c, s: 0.
(4, 3, 3): lambda c, s: 0.
(4, 3, 4): lambda c, s: 2*np.sqrt(2)*c**7*s

(4, 4, 1): lambda c, s: 0.
(4, 4, 2): lambda c, s: 0.
(4, 4, 3): lambda c, s: 0.
(4, 4, 4): lambda c, s: c**8
