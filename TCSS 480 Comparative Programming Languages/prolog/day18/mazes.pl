% facts indicate that there is a connection between two entities of length n meters
pway(a, b, 10).
pway(b, c, 15).
pway(d, c, 5).
pway(d, b, 10).

% If the user types solve(a, b, P, N) then 
% P = [a, b]
% N = 10
% If the user types solve(a, d, P, N) then 
% P = [a, b, c, d]
% N = 30;
% P = [a, b, d]
% N = 20

solve(X, Y, P, N) :- solve(X,Y,P,N).
solve(X, Y, P, N) :- 
	pway(X,Z,M),
	N is N + N.
	
	travelFromTo(Z,Y).