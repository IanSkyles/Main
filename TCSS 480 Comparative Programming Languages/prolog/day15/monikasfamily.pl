male(jozef).
male(alex).

female(ludwika).
female(monika).
female(joanna).

%child mother father
parents(alex, ludwika, jozef).
parents(monika, ludwika, jozef).
parents(joanna, ludwika, jozef).

sister_of(X, Y) :-
	female(X),
	parents(X, M, F),
	parents(Y, M, F).

