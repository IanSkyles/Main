/**Exercise  4.3 Write a predicate second(X,List) which checks whether X is the second element of List . */



second(X,List) :-
	List = [_,B | _], X=B.
	

/**Exercise  4.4 Write a predicate swap12(List1,List2) which checks whether List1 is identical to List2 , except that the first two elements are exchanged. */
swap12Real([LOneOne, LOneTwo | LOneRestOf],[LTwoOne, LTwoTwo | LTwoRestOf]) :-
	LOneOne = LTwoTwo,
	LOneTwo = LTwoOne,
	LTwoOne = LOneTwo,
	LTwoTwo = LOneOne,
	LOneRestOf = LTwoRestOf.

swap12(List1,List2) :-
	List1 = [A, B | X],
	List2 = [B, A | X]. 

/** Exercise  4.5 Suppose we are given a knowledge base with the following facts:  */

   tran(eins,one). 
   tran(zwei,two). 
   tran(drei,three). 
   tran(vier,four). 
   tran(fuenf,five). 
   tran(sechs,six). 
   tran(sieben,seven). 
   tran(acht,eight). 
   tran(neun,nine).
 
  /**listtran([],X).*/
  listtran([],E) :- E =[].
  listtran(G,[]) :- G =[].

  listtran([First|Tail], [Meaning|E]) :-
  	tran(First,Meaning),
  	listtran(Tail,E).
/** listtran([eins,neun,zwei],X). */
/** listtran(X,[one,seven,six,two]). */