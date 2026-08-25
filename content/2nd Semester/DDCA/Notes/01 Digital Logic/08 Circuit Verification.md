
We test for **functionality** and **timing** through verification and testing.

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

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=103|06 Slides]]

## Self-Checking Testbench Example

still **not scalable**

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

## Testvectors

- separate clock just for testing
- apply input on rising edge, check outputs on falling edge

Code Example starting at [[2nd Semester/DDCA/Slides/06 Slides.pdf#page=111|Slide 111]]

## Golden Models

- represent ideal behaviour on the highest abstraction
- compare your behaviour with the Golden Model
- automated testing, scalable, can also compare timing, separation of roles

![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=118|06 Slides]]

→ Code Example for automated testing: 
![[2nd Semester/DDCA/Slides/06 Slides.pdf#page=120|Slide 120]]

