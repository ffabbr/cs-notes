---
draft: "true"
---

1. We need a new input for the toggle of the switch. 
2. We use an always block to set a direction `reg`based on the switch position (if `reset`, set to `1'b0`, else set the `reg`to the switch position)
3. Extend the `assign` statement for `IOReadData` to also contain the information of the direction register. Depending on the `IOAddr` value we assign `IOReadData` either to the speed or the direction switch.
4. All the other changes are not made in `top.v` 