---
title: Verilog
description: Verilog cheatsheet contains useful code syntax with examples which is handy while coding.
created: 2022-10-05
updated: 2022-10-05
---  
- Verilog is a Hardware Description Language (HDL).
- It is a language used for describing a digital system such as a network switch, a microprocessor, a memory, or a flip-flop.
- We can describe any digital hardware by using HDL at any level.
- It is great and specific language for programming spartlet kit extensively used by Design engineers from AMD ,Qualcomm and other industries.  

#### I) Literals
```
<size >'<base><number>
```
Some examples include:

```
2'b10
4'b1011
8'hAF
{4'hA,4'b1111}
{4'hA,{4{1'b1}}}  
```

#### II) Module declaration

//Rule: Use separate file for each module (Filename should be saved with syntax .v)

```
module module_name (A, B, C);
input A; // Inputs to the module
input [2:0] B; //Convention: one per line
output C; // Output of the module
...
endmodule  
```

#### III) Nets and Variables  

Declaring a 4 bit wire with index starting at 0
```
wire [3:0] w;
```
Bit extract example:
```
r[5:2];
```
returns the 4 bits between bit positions 2 to 5 inclusive  

### III) Module instantiation

//In file outer_module.v

```
module outer_module (in1, in2, out);
input in1;
input [2:0] in2;
output out;
module_name md (.A(in1), .B(in2), .C(out));
...
endmodule
```   

### IV) Assignment

Assignment to wires uses the assign primitive outside  
an always block, vis:
```
assign mywire = a & b;
```
This is called continuous assignment because mywire
is continually updated as a and b change (i.e. it is all
combinational logic).  
Registers are assigned to inside an always block which
specifies where the clock comes from, vis:
```
always @(posedge clock)
r<=r+1;
```
The <= assignment operator is none blocking and is
performed on every positive edge of clock. Note that
if you have whole load of none blocking assignments
then they are all updated in parallel.  


### V) For Practice 

[Use this link](https://hdlbits.01xz.net/wiki/Main_Page)




