% learn prolog now 10.2

max(X,Y,Y):- X =< Y.
max(X,Y,X):- X > Y. 

% max with green cut.
maxGC(X,Y,Y):- X =< Y, !.
maxGC(X,Y,X):- X > Y. 

% max with red cut.
maxRC(X,Y,Z) :- X =< Y, !, Y = Z.
maxRC(X,Y,X).


% Learn prolog now Exercise 10.1 
%Suppose we have the following database:

p(1).
p(2) :- !.
p(3).

% ?-  p(X).
% X = 1 ;
% X = 2.

%p(X),p(Y).
%X = Y, Y = 1 ;
%X = 1,
%Y = 2 ;
%X = 2,
%Y = 1 ;
%X = Y, Y = 2.

%p(X),!,p(Y).
%X = Y, Y = 1 ;
%X = 1,
%Y = 2.


% Learn prolog now Exercise 10.4
% Recall that in Exercise 3.3 we gave you the following knowledge base:

directTrain(saarbruecken, dudweiler).
directTrain(forbach, saarbruecken).
directTrain(freyming, forbach).
directTrain(stAvold, freyming).
directTrain(fahlquemont, stAvold).
directTrain(metz, fahlquemont).
directTrain(nancy, metz).

% We asked you to write a recursive predicate travelFromTo/2 that told us when
% we could travel by train between two towns.

% Now, it’s plausible to assume that whenever it is possible to take a direct
% train from A to B, it is also possible to take a direct train from B to
% A. Add this information to the database. Then write a predicate route/3 which
% gives you a list of towns that are visited by taking the train from one town
% to another. For instance:

% ?- route(forbach,metz,Route).
% Route = [forbach,freyming,stAvold,fahlquemont,metz].

%if track from a to b
%then track from b to a
tracks(A, B) :-
    directTrain(A, B).

tracks(A, B) :-
    directTrain(B, A).

% base case
route(A, B, [A,B], _) :-
    tracks(A,B),
    %only find one direct route
    !.

% recursive case
route(A, B, [A|Route], Visited) :-
	%is there any railroad track?
    tracks(A, C),
    %is the town not already in the route?
    %true if C has not been visited
    not(member(C, Visited)),
    route(C, B, Route, [A | Visited]).

% start case
route(A, B, Route) :-
    route(A,B, Route, [A]).