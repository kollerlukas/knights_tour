# Knight's Tour Revisited Revisited

This is a Isabelle/HOL formalization of (Cull and De Curtins, 1978). In (Cull and De Curtins, 1978) the existence of a Knight's path is proved for arbitrary `n×m`-boards with `min n m ≥ 5`. If `even n*m`, then there exists a Knight's circuit.

A [Knight's path](https://en.wikipedia.org/wiki/Knight%27s_tour) is a sequence of squares on a chessboard s.t. every step in sequence is a valid move for a Knight that the Knight visits every square on the boards exactly once. A Knight is a chess figure that is only able to move two squares vertically and one square horizontally or two squares horizontally and one square vertically. Finding a Knight's path is an instance of the Hamiltonian Path Problem. A Knight's circuit is a Knight's path, where additionally the Knight can move from the last square to the first square of the path, forming a loop.

The main idea for the proof of the existence of a Knight's path is to inductivly construct paths from a few pre-computed paths for small boards, e.g. `5×5`, `5×6`, ..., `8×9`. The paths for small boards are transformed (i.e. transpose, mirror, translate) and combined to create paths for larger boards.

## Incorrect Boards & Corrections

While formalizing the proofs I discovered two mistakes in the original proof by Cull and De Curtins: (i) the pre-computed path for the `6×6` board that ends in the upper-left (in Figure 2) and (ii) the pre-computed path for the `8×8` board that ends in the upper-left (in Figure 5) are incorrect. I.e. on the `6×6` board the Knight cannot step from square 26 to square 27; in the `8×8` board the Knight cannot step from square 27 to square 28.

I have computed correct paths for the `6×6` and `8×8`-boards that start in the lower left and end in the upper-left.

To compute the correct paths I used the python script `compute_paths.py`. In `compute_paths.py` I have implemented a simple backtracking algorithm to compute paths on arbitrary `n×m` boards for arbitrary start and end squares. The algorithm uses the heuristic to first try to explore the least accessible neighbors, as described in (Conrad, 1999).

| 8  | 25 | 10 | 21 | 6  | 23 |
|----|----|----|----|----|----|
| 11 | 36 | 7  | 24 | 33 | 20 |
| 26 | 9  | 34 | 3  | 22 | 5  |
| 35 | 12 | 15 | 30 | 19 | 32 |
| 14 | 27 | 2  | 17 | 4  | 29 |
| 1  | 16 | 13 | 28 | 31 | 18 |

| 38 | 41 | 36 | 27 | 32 | 43 | 20 | 25 |
|----|----|----|----|----|----|----|----|
| 35 | 64 | 39 | 42 | 21 | 26 | 29 | 44 |
| 40 | 37 | 6  | 33 | 28 | 31 | 24 | 19 |
| 5  | 34 | 63 | 14 | 7  | 22 | 45 | 30 |
| 62 | 13 | 4  | 9  | 58 | 49 | 18 | 23 |
| 3  | 10 | 61 | 52 | 15 | 8  | 57 | 46 |
| 12 | 53 | 2  | 59 | 48 | 55 | 50 | 17 |
| 1  | 60 | 11 | 54 | 51 | 16 | 47 | 56

## Future Work

An interesting way to extend this work would be to implement a backtracking algorithm in Isabelle/HOL (as in the python script `compute_paths.py`) and formally prove the algorithm correct. I imagine the proof being quite involved and of similar complexity as the proof presented here.

## References

- Cull, P. and De Curtins, J. (1978). "Knight’s Tour Revisited." In: *Fibonacci Quarterly*. Vol. 16, pp. 276--285. June, 1978.
- Conrad, A. (1999). "Das Springerproblem." accessed 29.12.2021. [http://www.axel-conrad.de/springer/springer.html](http://www.axel-conrad.de/springer/springer.html). Dec, 1999
