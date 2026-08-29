
Programs often have branches such as `if, else` statements. We try to predict which branch will be taken. 

> [!Note]- not so deep intro
> Need to predict
> 1. whether fetched instruction is a branch (BTB)
> 2. branch direction
> 3. branch target address (BTB)
> 
> BTB = Branch Target Buffer, "remembers" target address from last time that branch was executed

*CPI=cycles per instruction*
`CPI = (1 + (C*T)*P) = (1 + G*P)`

C: percentage of control flow instructions
T: percentage of ==taken== control flow instructions 
G: percentage of correctly guessed branches
P: penalty for misprediction

---

The hard part is branch direction prediction. f.ex. if or while loops, always taken means it always runs them, always not taken means skip this in prediction

**static at compile time**, f.ex.: 
- always taken, always not taken
- use heuristics based on program analysis to determine predicted direction. programmer can indicate future branch direction. imagine pragmas example if condition as `if(likely(x)){}`.

**dynamic at run time**:
- ==Last time predictor==: predict the same as last result. this changes prediction from T to N too quickly, so add hysteresis with strongly taken, weakly taken, strongly not taken, weakly not taken (2-bit). That way needs to change 2 times in a row for prediction to change
- ==Global branch correlation==: look at other branches' outcomes. simple example: `if(x<1){}; if(x>1){}`, if the first is taken, 2nd one is not taken. add Global History Register to keep T/NT (not taken) history of all branches, then pattern match the current global history to past global histories to see. The GHR (global history register) is the current history, PHT (pattern history table) is like a table with the GHR state in one col and what to predict (2-bit last time predictor for this case) next.
  ![[Bildschirmfoto 2026-05-07 um 14.06.32.png]]
  
- ==Local branch correlation==: look at result from last time of same branch. suppose we keep repeating same pattern such as TTT(NT) 
- ==Hybrid predictor==: combine one of the above and select best prediction

![[Bildschirmfoto 2026-04-17 um 15.38.34.png]]
