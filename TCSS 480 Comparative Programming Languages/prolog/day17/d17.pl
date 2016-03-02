% Exercise  3.2 from 
% http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse11


directlyIn(katarina,olga).
directlyIn(olga,natasha).
directlyIn(natasha,irina).

in(X,Y) :- 
	directlyIn(X,Y).

in(X,Y) :- 
	directlyIn(X,Z),
	in(Z,Y).




% Example 3.3 from
% http://www.learnprolognow.org/lpnpage.php?pagetype=html&pageid=lpn-htmlse11
directTrain(saarbruecken,dudweiler). 
directTrain(forbach,saarbruecken). 
directTrain(freyming,forbach). 
directTrain(stAvold,freyming). 
directTrain(fahlquemont,stAvold). 
directTrain(metz,fahlquemont). 
directTrain(nancy,metz).

%2 way rail road



travelFromTo(X,Y) :- directTrain(X,Y).
travelFromTo(X,Y) :- 
	directTrain(X,Z),
	travelFromTo(Z,Y).

%travelFromTo(X,Y) :- directTrain(X,Y).
%travelFromTo(X,Y) :- directTrain(Y,X).
%travelFromTo(X,Y) :- directTrain(Y,Z), travelFromTo(Z,X).
%travelFromTo(X,Y) :- directTrain(X,Z), travelFromTo(Z,Y).


%travelFromTo(X,Y) :- directTrain(Y,Z), travelFromTo(X,Z).
%travelFromTo(X,Y) :- directTrain(X,Z), travelFromTo(Y,Z).


%travelFromTo(X,Y) :- directTrain(Z,Y), travelFromTo(X,Z).