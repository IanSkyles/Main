% movie(M,Y) <- movie M came out in year Y
movie(the_usual_suspects, 1995).
movie(american_beauty, 1999).
movie(down_from_the_mountain, 2000).
movie(girl_with_a_pearl_earring, 2003).
movie(barton_fink, 1991).
movie(crimewave, 1985).
movie(lick_the_star, 1998).
movie(the_horse_whisperer, 1998).
movie(blade_runner, 1997).

% director(M,D) <- movie M was directed by director D
director(american_beauty, sam_mendes).
director(girl_with_a_pearl_earring, peter_webber).
director(barton_fink, joel_coen).
director(crimewave, sam_raimi).
director(lick_the_star, sofia_coppola).
director(blade_runner, joseph_d_kucan).

% actor(M,A,R) <- actor A played role R in movie M
actor(american_beauty, kevin_spacey, lester_burnham).
actor(american_beauty, wes_bentley, ricky_fitts).
actor(american_beauty, chris_cooper, col_frank_fitts_usmc).
actor(the_usual_suspects, kevin_spacey, roger_verbal_kint).
actor(crimewave, joel_coen, reporter_at_execution).
actor(the_horse_whisperer, chris_cooper, frank_booker).
actor(blade_runner, joseph_d_kucan, crazylegs_larry).

% actress(M,A,R) <- actress A played role R in movie M
actress(american_beauty, annette_bening, carolyn_burnham).
actress(american_beauty, thora_birch, jane_burnham).
actress(american_beauty, mena_suvari, angela_hayes).
actress(girl_with_a_pearl_earring, scarlett_johansson, griet).
actress(anna, sofia_coppola, noodle).

released_after(M, Y) :-
	movie(M, X),
	X > Y.

releaed_before(M,Y) :-
	movie(M,X),
	X < Y.

same_year(M1, M2) :-
	movie(M1,X),
	movie(M2,Y),
	X == Y.

co_star(A1, A2) :-
	actor(Y,A1, _),
	actor(X,A2, _),
	X == Y;
	actor(Y,A1, _),
	actress(X,A2, _),
	X == Y;
	actress(Y,A1, _),
	actor(X,A2, _),
	X == Y;
	actress(Y,A1, _),
	actress(X,A2, _),
	X == Y.

released_after_two :-
	write('Movies after what year'),
	read(Y),
	movie(M, X),
	X > Y,
	write(M).

findMovieYear :-
	write('what movie?'),
	read(Name),
	movie(Name, X),
	write('The movie'), write(Name), write('was procduced in'), write(X), nl.