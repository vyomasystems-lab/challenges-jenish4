# challenges-jenish4
challenges-jenish4 created by GitHub Classroom

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://drive.google.com/uc?export=view&id=1uoi3b59UVfZcRHY0bc6sjLuUUespmkpz)

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. 

# Multiplexer Design Verification

## Verification Environment

The test drives inputs to the Design Under Test (multiplexer module here) which takes in 31 2-bit inputs, a 5-bit select and gives 2-bit output

Random values are assigned to the input ports 50 times. 

The assert statement is used for comparing the output to the expected value.

The following error is seen:
```
assert dut.out.value == I[S], "Randomised test failed with: expected value={EXP}, output={OUTPUT}, sel={SELECT}".format(EXP=I[S], OUTPUT=dut.out.value, SELECT=S)
                     AssertionError: Randomised test failed with: expected value=3, output=00, sel=30
```
## Test Scenario 
- Test Inputs: sel=30, inp30=3
- Expected Output: out=3
- Observed Output in the DUT dut.out=00

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      5'b11101: out = inp29; 
      5'b11110: out = inp30; //this line was missing. adding this line fixes the bug
      default: out = 0;   
```


# Verification Strategy

1. We give random values to the inputs. 
2. Calculate the expected output.
3. Compare the expected output with the obtained output from the verilog code.
4. If there is a mismatch, find the bug and try to correct it.
5. We repeat these steps for a few loops.


# Is the verification complete ?

Until and unless we simulate all the permutations and combinations of the inputs, it is difficult to be 100% sure that the verification is complete.

But doing this in highly complex systems is next to impossible.

Hence we try to check for critical random corner cases and also input random values for few loops.
