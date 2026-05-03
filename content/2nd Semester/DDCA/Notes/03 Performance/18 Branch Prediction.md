
Need to predict
1. whether fetched instruction is a branch (BTB)
2. branch direction
3. branch target address (BTB)

BTB = Branch Target Buffer, "remembers" target address from last time that branch was executed

The hard part is 2. branch direction prediction. f.ex. if or while loops, always taken means it always runs them, always not taken means skip this in prediction

1. static at compile time:  use heuristics based on program analysis to determine predicted direction. programmer can indicate future branch direction. imagine pragmas example if condition as `if(likely(x)){}`.
2. dynamic at run time:

Types
- Last time predictor: predict the same as last result. Add hysteresis with strongly taken, weakly taken, strongly not taken, weakly not taken. That way needs to change 2 times in a row for prediction to change
- Global branch correlation: look at other branches' outcomes. simple example: `if(x<1){}; if(x>1){}`, if the first is taken, 2nd one is not taken. add Global History Register to keep track of T/NT (not taken) history of all branches
- Local branch correlation: look at result from last time of same branch. suppose we keep repeating same pattern such as TTT(NT) 
- Hybrid predictor: combine one of the above and select best prediction

![[Bildschirmfoto 2026-04-17 um 15.38.34.png]]
