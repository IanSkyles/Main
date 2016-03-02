parent(a,b).     % a is the parent of b

parent(a,d).
parent(a,k).
parent(k,l).
parent(k,m).
parent(b,e).
parent(b,f).
parent(f,g).
parent(f,h).
parent(f,i).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(Z,Y), ancestor(X,Z).

