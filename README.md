## 1.Background
`SynDT` is an algorithm to learn winning strategy of `Impartial Combinatorial Games`. 

## 2.Install
- the version of Z3-solver is 4.8.13.0
- the version of Antlr4 is 4.9
- the version of  python's operating environment is 3.6.13


## 3.Usage

### Compile PDDL:
Open the terminal and switch to the current folder.

If the antlr-4.9-complete.jar is downloaded to path D:\Javalib, load the parsing tool into the subfile folder under the current folder:

Parsing G4 files：
```
java -jar D:\Javalib\antlr-4.9-complete.jar -Dlanguage=Python3 PDDLGrammar.g4 -o subfile
```

Generate traverser:：
```
java -jar D:\Javalib\antlr-4.9-complete.jar -Dlanguage=Python3 -no-listener -visitor PDDLGrammar.g4 -o subfile
```

We have loaded the parsing tool into the subfile folder. You can skip Compile PDDL.

### Run the code with the following command:

```
python <approach> <gameProblem> <resultFile> <gameType>
```
```approach```: it is one of the Enum, SynDT, SynDT+S;
```gameProblem```: it is the path of game problem(.pddl file);
```resultFile```: it is the path of resulet file(.xml file);
```gameType```: it is normal rule or misere rule.

For example,  the game problem：Two-piled-nim.pddl
```
python SynDT.py ".\domain\2.Nim\2.1 Nim\Two-piled-nim.pddl" ".\result.xls" normal
```

Running process:

```
#################################################################
######################### Formalization #########################
#################################################################

GameName:
         Two-piled-nim
Terminal Condition:
         And(v1 == 0, v2 == 0)
Constraint:
         And(v1 >= 0, v2 >= 0)
Action Name:     take1
Action parameters:       [k]
Precondition:    And(v1 >= k, k > 0)
EffectList:      [[True, v1, v1 - k]]
Transition Formula:
         And(And(v1 >= k, k > 0), v1' == v1 + -1*k, v2' == v2)
Action Name:     take2
Action parameters:       [k]
Precondition:    And(v2 >= k, k > 0)
EffectList:      [[True, v2, v2 - k]]
Transition Formula:
         And(And(v2 >= k, k > 0), v2' == v2 + -1*k, v1' == v1)
Var List: [v1, v2]
Var next list [v1_next, v2_next]
Appeal constant []
Global transition formula:
         Or(Exists([k],And(And(v1 >= k, k > 0),
    v1_next == v1 + -1*k,
    v2_next == v2)),Exists([k],And(And(v2 >= k, k > 0),
    v2_next == v2 + -1*k,
    v1_next == v1)))
All terminate position:
         [[0, 0]]


####################################################################
################# Learning winning formula #########################
####################################################################


Labels set:      {False: [], True: []}

-------------------------- Learn decision tree -------------------------
         v1 == v1

----------------------------- Verification  ----------------------------

Repeat expression
InitializeStates 3 example generate:     [[0, 1], [1, 0], [0, 2]]
Labels set:      {False: [], True: [[0, 1], [1, 0], [0, 2]]}
the set of atoms: [v1 == v2, v1 == 0, v1 == 1, v2 == 1, v1 >= 0, v2 > 1]
Number of data points:   3

-------------------------- Learn decision tree -------------------------
         True

----------------------------- Verification  ----------------------------

The constraint of winning formula is not valid and add countexamples, go to the next round of the learning process.
Generate 3 countexamples:        [[0, 0], [1, 1], [2, 0]]
Labels set:      {False: [[0, 0], [1, 1]], True: [[0, 1], [1, 0], [0, 2], [2, 0]]}
the set of atoms: [v1 == v2, v1 == 0, v1 == 1, v2 == 1, v1 >= 0, v2 > 1, v2 == 0, v1 >= v2, v1 >= 1, v2 >= v1, v2 
>= 1, v1 > v2, v1 > 1, v2 > v1]
Number of data points:   6

-------------------------- Learn decision tree -------------------------
         If(v1 == v2, False, True)

----------------------------- Verification  ----------------------------

The constraints of wwinning formula is valid

---------------------------- Winning formula  --------------------------

Losing formula： v1 == v2
Winning Fromula： Not(v1 == v2)
The total running time： 0.45
The size:  3


#####################################################################
################# Learning winning strategy #########################
#####################################################################


All T-label paths:
         ['Not(v1 == v2)']

******************** One of T-label path formula: Not(v1 == v2) **********************

Generate ground action for datapoint [0, 1]
Find a ground action:take2(1)
Generate ground action for datapoint [1, 0]
Find a ground action:take1(1)
Generate ground action for datapoint [0, 2]
Find a ground action:take2(2)
Generate ground action for datapoint [2, 0]
Find a ground action:take1(2)
The set of data points: [[0, 1], [1, 0], [0, 2], [2, 0]]
Ensure each data point have label cover:
[0, 1] no label cover:
Find action:take2(1)
[1, 0] no label cover:
Find action:take1(1)
[0, 2] no label cover:
Find action:take2(v2)
[2, 0] no label cover:
Find action:take1(v1)
The set of label:
        take2(1)  take1(1)  take2(v2)  take1(v1)

The set of atoms
         [v1 > v2, v1 < v2, v1 == v2, v1 == 0, v1 == 1, v1 == 2, v2 == 0, v2 == 1, v2 == 2, v1 >= 0, v1%2 == 0, v2%2 == 0]
The set of data poins
         [[0, 1], [1, 0], [0, 2], [2, 0]]
The label of data points:
         take2(1) : [[0, 1]]
         take1(1) : [[1, 0]]
         take2(v2) : [[0, 2], [0, 1]]
         take1(v1) : [[2, 0], [1, 0]]

---------------------------- Learn decision tree --------------------------
        If(v1 > v2,take1(v1),take2(v2))
------------------------------- Verification  -----------------------------

Path: Not(v1 == v2) , all canditate strategy: [[v1 > v2, (0, v1)], [Not(v1 > v2), (1, v2)]]
Verify this path: And(Not(v1 == v2), v1 > v2) execute action: take1(v1)
The constraint of winning strategy is not valid and add countexamples, go to the next round of the learning process.
=========== generate countexample =========
Generate 3 countexamples: [[2, 1], [0, 3], [1, 2]]
Generate ground action for datapoint [2, 1]
Find a ground action:take1(1)
Generate ground action for datapoint [0, 3]
Find a ground action:take2(3)
Generate ground action for datapoint [1, 2]
Find a ground action:take2(1)
==============================================

The set of data points: [[0, 1], [1, 0], [0, 2], [2, 0], [2, 1], [0, 3], [1, 2]]
Ensure each data point have label cover:
The set of label:
        take2(1)  take1(1)  take2(v2)  take1(v1)  take1(v2)  take2(v2 - v1)

The set of atoms
         [v1 < v2, v1 == v2, v1 == 0, v1 == 1, v1 == 2, v2 == 0, v2 == 1, v2 == 2, v1 >= 0, v1%2 == 0, v2%2 == 0, 
v1 >= v2, v1 >= 1, v2 >= v1, v2 >= 1, v2 >= 2, v2 > 2, v2%2 == 1]
The set of data poins
         [[0, 1], [1, 0], [0, 2], [2, 0], [2, 1], [0, 3], [1, 2]]
The label of data points:
         take2(1) : [[0, 1], [1, 2]]
         take1(1) : [[1, 0], [2, 1]]
         take2(v2) : [[0, 2], [0, 1], [0, 3]]
         take1(v1) : [[2, 0], [1, 0]]
         take1(v2) : [[2, 1]]
         take2(v2 - v1) : [[0, 1], [0, 2], [0, 3], [1, 2]]

---------------------------- Learn decision tree --------------------------
        If(v1 >= v2,If(v2 == 0,take1(v1),take1(1)),take2(v2 - v1))

------------------------------- Verification  -----------------------------

Path: Not(v1 == v2) , all canditate strategy: [[And(v1 >= v2, v2 == 0), (0, v1)], [And(v1 >= v2, Not(v2 == 0)), (0, 1)], [Not(v1 >= v2), (1, v2 - v1)]]
Verify this path: And(Not(v1 == v2), And(v1 >= v2, v2 == 0)) execute action: take1(v1)
         [And(v1 >= v2, v2 == 0), (0, v1)] have a winning rule
Verify this path: And(Not(v1 == v2), And(v1 >= v2, Not(v2 == 0))) execute action: take1(1)
The constraint of winning strategy is not valid and add countexamples, go to the next round of the learning process.
=========== generate countexample =========
Generate 3 countexamples: [[3, 1], [3, 0], [0, 4]]
Generate ground action for datapoint [3, 1]
Find a ground action:take1(2)
Generate ground action for datapoint [3, 0]
Find a ground action:take1(3)
Generate ground action for datapoint [0, 4]
Find a ground action:take2(4)
==============================================

The set of data points: [[0, 1], [1, 0], [0, 2], [2, 0], [2, 1], [0, 3], [1, 2], [3, 1], [3, 0], [0, 4]]
Ensure each data point have label cover:
[3, 1] no label cover:
Find action:take1(2)
The set of label:
        take2(1)  take1(1)  take2(v2)  take1(v1)  take1(v2)  take2(v2 - v1)  take1(2)

The set of atoms
         [v1 < v2, v1 == v2, v1 == 0, v1 == 1, v1 == 2, v2 == 1, v2 == 2, v1 >= 0, v1%2 == 0, v2%2 == 0, v1 >= 1, 
v2 >= v1, v2 >= 1, v2 >= 2, v2 > 2, v2%2 == 1, v2 == 0, v1 >= v2, v1 >= 2, v1 > 2, v1%2 == 1]
The set of data poins
         [[0, 1], [1, 0], [0, 2], [2, 0], [2, 1], [0, 3], [1, 2], [3, 1], [3, 0], [0, 4]]
The label of data points:
         take2(1) : [[0, 1], [1, 2]]
         take1(1) : [[1, 0], [2, 1]]
         take2(v2) : [[0, 2], [0, 1], [0, 3], [0, 4]]
         take1(v1) : [[2, 0], [1, 0], [3, 0]]
         take1(v2) : [[2, 1]]
         take2(v2 - v1) : [[0, 1], [0, 2], [0, 3], [1, 2], [0, 4]]
         take1(2) : [[3, 1], [2, 0]]

---------------------------- Learn decision tree --------------------------
        If(v1 < v2,take2(v2 - v1),If(v2 == 1,If(v1 == 2,take1(1),take1(2)),take1(v1)))

------------------------------- Verification  -----------------------------

Path: Not(v1 == v2) , all canditate strategy: [[v1 < v2, (1, v2 - v1)], [And(Not(v1 < v2), v2 == 1, v1 == 2), (0, 
1)], [And(Not(v1 < v2), v2 == 1, Not(v1 == 2)), (0, 2)], [And(Not(v1 < v2), Not(v2 == 1)), (0, v1)]]
Verify this path: And(Not(v1 == v2), v1 < v2) execute action: take2(v2 - v1)
         [v1 < v2, (1, v2 - v1)] have a winning rule
Verify this path: And(Not(v1 == v2), And(Not(v1 < v2), v2 == 1, v1 == 2)) execute action: take1(1)
         [And(Not(v1 < v2), v2 == 1, v1 == 2), (0, 1)] have a winning rule
Verify this path: And(Not(v1 == v2), And(Not(v1 < v2), v2 == 1, Not(v1 == 2))) execute action: take1(2)
The constraint of winning strategy is not valid and add countexamples, go to the next round of the learning process.
=========== generate countexample =========
Generate 3 countexamples: [[4, 1], [1, 3], [4, 0]]
Generate ground action for datapoint [4, 1]
Find a ground action:take1(3)
Generate ground action for datapoint [1, 3]
Find a ground action:take2(2)
Generate ground action for datapoint [4, 0]
Find a ground action:take1(4)
==============================================

The set of data points: [[0, 1], [1, 0], [0, 2], [2, 0], [2, 1], [0, 3], [1, 2], [3, 1], [3, 0], [0, 4], [4, 1], [1, 3], [4, 0]]
Ensure each data point have label cover:
[4, 1] no label cover:
Find action:take1(v1 - 1)
The set of label:
        take2(1)  take1(1)  take2(v2)  take1(v1)  take1(v2)  take2(v2 - v1)  take1(2)  take1(v1 - 1)  take1(v1 - v2)

The set of atoms
         [v1 == v2, v1 == 0, v1 == 1, v2 == 2, v1 >= 0, v1%2 == 0, v2%2 == 0, v1 >= 1, v2 >= v1, v2 >= 1, v2 >= 2, v2 > 2, v2%2 == 1, v2 == 0, v1 >= v2, v1 >= 2, v1 > 2, v1%2 == 1, v1 == 2, v2 == 1]
The set of data poins
         [[0, 1], [1, 0], [0, 2], [2, 0], [2, 1], [0, 3], [1, 2], [3, 1], [3, 0], [0, 4], [4, 1], [1, 3], [4, 0]] 
The label of data points:
         take2(1) : [[0, 1], [1, 2]]
         take1(1) : [[1, 0], [2, 1]]
         take2(v2) : [[0, 2], [0, 1], [0, 3], [0, 4]]
         take1(v1) : [[2, 0], [1, 0], [3, 0], [4, 0]]
         take1(v2) : [[2, 1]]
         take2(v2 - v1) : [[0, 1], [0, 2], [0, 3], [1, 2], [0, 4], [1, 3]]
         take1(2) : [[3, 1], [2, 0]]
         take1(v1 - 1) : [[4, 1], [2, 1], [3, 1]]
         take1(v1 - v2) : [[1, 0], [2, 0], [2, 1], [3, 1], [3, 0], [4, 1], [4, 0]]

---------------------------- Learn decision tree --------------------------
        If(v2 >= v1,take2(v2 - v1),take1(v1 - v2))

------------------------------- Verification  -----------------------------

Path: Not(v1 == v2) , all canditate strategy: [[v2 >= v1, (1, v2 - v1)], [Not(v2 >= v1), (0, v1 - v2)]]
Verify this path: And(Not(v1 == v2), v2 >= v1) execute action: take2(v2 - v1)
         [v2 >= v1, (1, v2 - v1)] have a winning rule
Verify this path: And(Not(v1 == v2), Not(v2 >= v1)) execute action: take1(v1 - v2)
         [Not(v2 >= v1), (0, v1 - v2)] have a winning rule

The T-label path formula Not(v1 == v2) can find partial winning strategy：
         If(Not(v2 >= v1),take2(v2 - v1),take1(v1 - v2))

---------------------------- Winning strategy  ---------------------------

[And(Not(v1 == v2), v2 >= v1), 'take2(v2 - v1)']
[And(Not(v1 == v2), Not(v2 >= v1)), 'take1(v1 - v2)']
The total running time: 1.67
```
The result will be saved in the filr result.xls, which contains 6 columns : `game name | winning formula |	time of winning formula | size | winning strategy |	time of winning strategy`.

## 4.Domain
We use PDDL to define the game problem, like this:
```
(define (domain Two-piled-nim)
	(:objects ?v1 ?v2)
	(:tercondition (and (= ?v1 0) (= ?v2 0) ))
    (:constraint (and (>= ?v1 0) (>= ?v2 0)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0))
        :effect (assign ?v2 (- ?v2 ?k)))
)
```
All domain are stored in folder `domain`.

## 5.Optimization

1. We also provide a way to synthesize winning formulas and strategies for multiple games in turn. The file main.py can execute a folder that contains multiple PDDL files for different game problems like this:
   
```
python main.py <approach> <PDDLFolder> <resultFile> <Type>
```

For example:
```
python main.py SynDT+S.py ".\domain\1.Sub\1.1 Take-away" ".\result.xls" normal
```

2. We can also increase the number of counterexamples generated per round to reduce the number of iterations by changing the value of ```ptk``` in approach. 
The default value of ```ptk```  is 3.
   ****