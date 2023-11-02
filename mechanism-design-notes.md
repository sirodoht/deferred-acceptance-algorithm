# Mechanism Design Notes

> Notes from Mustafa’s LCPT Mechanism Design Module (https://lu.ma/y2frh5dz)

Mechanisms to allow for group decision making.

Definitions:

* Mechanism: a process for making decisions as a function of agents.
* The Draw: a mechanism (a random selection).
* Pareto Optimality: property of an outcome, in that there is no way to make a
partipant better off without making someone else worse off.
    * [https://en.wikipedia.org/wiki/Pareto_efficiency](https://en.wikipedia.org/wiki/Pareto_efficiency)
* Strategyproofness: you will be definitely be worse if you lie about your
preferences.
    * [https://en.wikipedia.org/wiki/Strategyproofness](https://en.wikipedia.org/wiki/Strategyproofness)
* One-sided Market: room selection, rooms do not care who's in
* Two-sided Market: uni applications, universities care to get the best students
* Centralised Market: universities in Hungary, there is a gov system that says
who goes where
* Decentralised Market: universities in the UK, they choose their own students
* Collusion: people work together
* Competition: people might undermine each other
* Market Failure/Unravelling
* Bipartite Graph Matching: bipartite: men/women, students/universities; both
sides have preferences
* Stable Matching: nobody wants to re-marry; 2-sided pareto optimality
    * [https://en.wikipedia.org/wiki/Stable_marriage_problem](https://en.wikipedia.org/wiki/Stable_marriage_problem)
* Deferred acceptance algorithm, a greedy algorithm, aka Gale–Shapley algorithm.
Is only strategyproof for proposers.
    * [https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm)

## Next time

* Arrow's impossibility theorem: nice voting systems are impossible.
    * [https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem](https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem)

## Post-lecture research

* [https://www.astralcodexten.com/i/138369770/manifoldlove](https://www.astralcodexten.com/i/138369770/manifoldlove)
    * Scott Alexander on dating prediction markets
* [https://en.wikipedia.org/wiki/Condorcet_method](https://en.wikipedia.org/wiki/Condorcet_method)
* [https://daffidwilde.github.io/matching/](https://daffidwilde.github.io/matching/)
    * Python library implementing the Deferred acceptance algorithm (which it
    calls Stable Marriage algorithm).
* [https://en.wikipedia.org/wiki/Stable_roommates_problem](https://en.wikipedia.org/wiki/Stable_roommates_problem)
    * This is distinct from the stable-marriage problem in that the
    stable-roommates problem allows matches between any two elements, not just
    between classes of "men" and "women".
* [https://en.wikipedia.org/wiki/National_Resident_Matching_Program#Matching_algorithm](https://en.wikipedia.org/wiki/National_Resident_Matching_Program#Matching_algorithm)
    * The hospitals/residents problem – also known as the college admissions
    problem – differs from the stable marriage problem in that a hospital can
    take multiple residents, or a college can take an incoming class of more
    than one student.
* [https://en.wikipedia.org/wiki/Stable_marriage_problem#Related_problems](https://en.wikipedia.org/wiki/Stable_marriage_problem#Related_problems)
