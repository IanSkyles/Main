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

/*actor(M,A,R) :-
	female(X),
	parents(X, M, F),
	parents(X, M, F).
*/

% actress(M,A,R) <- actress A played role R in movie M
actress(american_beauty, annette_bening, carolyn_burnham).
actress(american_beauty, thora_birch, jane_burnham).
actress(american_beauty, mena_suvari, angela_hayes).
actress(girl_with_a_pearl_earring, scarlett_johansson, griet).
actress(anna, sofia_coppola, noodle).



/* EXERCISES
Part 1: Write queries to answer the following questions.
    a. In which year was the movie American Beauty released?
    	movie(american_beauty, X).
    	or 
    	movie(american_beauty, 1999).
    b. Find the movies released in the year 2000.
    	movie(X, 2000).
    		press the ; to get any after the first one.
    c. Find the movies released before 2000.
    	movie(X, Y), Y<2000.
    d. Find the movies released after 1990.
    	movie(X,Y), Y > 1990.
    e. Find an actor who has appeared in more than one movie.
	    (2 queries with the same variable for actor, different for movie and role.
	    You must also state that the first movie variable cannot equal the second).
	    actor(M,A,R) <- actor A played role R in movie M

	    actor(M1,A,_), actor(M2, A, _), M1\=M2.

    f. Find a director of a movie in which Scarlett Johansson appeared.
    	director(movie(,D)
    		director(M,D), actress(M, scarlett_johansson, _).
    g. Find an actor who has also directed a movie.
    	 director(_,D), actor(_,D,_).
    h. Find an actor or actress who has also directed a movie.
    	director(_,D), actor(_,D,_); director(_,D), actress(_,D,_).
    i. Find the movie in which John Goodman and Jeff Bridges were co-stars.
Part 2: Add rules to the database to do the following,
    a. released_after(M, Y) <- the movie was released after the given year.
    b. released_before(M, Y) <- the movie was released before the given year.
    c. same_year(M1, M2) <- the movies are released in the same year.
    d. co_star(A1, A2) <- the actor/actress are in the same movie.
*/

released_after(M, Y) :-
	movie(M, X),
	X > Y.

released_before(M, Y) :-
	movie (M, X),
	X < Y.

same_year(M1, M2) :-
	M1 == M2.


