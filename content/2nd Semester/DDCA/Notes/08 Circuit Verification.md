
How can we test for **functionality** and **timing**? 

→ ==Simulation==

---

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=93]]
![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=94]]

---

## Functional Checks

- check logical correctness of the design
- physical circuit timing ignored

**Testbench**: 
- a simulation of the circuit
- a module created specifically to test a design
- Tested design is called the "device under test (DUT)"

### Example

```verilog
module testbench2(); // No inputs, outputs
  reg  a, b, c;      // Manually assigned
  wire y;            // Manually checked

  // instantiate device under test
  sillyfunction dut(.a(a), .b(b), .c(c), .y(y));

  // apply hardcoded inputs one at a time
  initial begin
    a = 0; b = 0; c = 0; #10; // apply input, wait 10ns
    if (y !== 1) $display("000 failed."); // check result
    
    c = 1; #10;               
    if (y !== 0) $display("001 failed.");

  end
endmodule
```

Problem: ==not scalable==

