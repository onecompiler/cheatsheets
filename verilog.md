---
title: Verilog HDL
description: Guides through the basics of Verilog for writing digital cicuits on SpartanXL Kit.
created: 2022-10-20
---


#### Identifier:

- An identifier must begin with an alphabetic character or an underscore. Basically anything in the range (a-z A-Z_).
- An identifier may contain alphabetic or numeric characters, the underscore or the dollar sign. Basically anything in the range (a-z A-Z 0-9 _$)

Examples:
```
comparator_input
Compout$p
_datax64
```

#### Keywords:
Keywords are special words used to describe the language construct. As you can see in our above example, module, assign are keywords

Examples:

```
wire
reg
break
module
```

#### Modules:

- The module definition starts with the keyword module followed by the module name which is an identifier to identify the name of the module.
- The module contains a list of the input and output port and enclosed by round bracket parenthesis and followed by ";". 

```
module comparator( 
   x,
   y,
   z)
    );
	input x,
    input y,
    output z
assign z = (~x & ~y) |(x & y);
endmodule
```
Rules for connecting ports

- Input Ports Internally the input ports must always be of type net.
- Externally the inputs can connect to a variable of type reg or net.
- Outputs Internally output port can be net or reg.
- Externally the outputs must connect to a variable of type net.
- Inouts The Inout port must always be of type net internally or externally .

#### Modelling Styles

##### Gate-level Modelling:
-Constructing logical circuits using builtin gates.

```
module fulladd(sum, c-out, a, b, c-in) ; 
// I/O port declarations 
output sum, c-out; 
input a, b, c-in; 
// Internal nets 
wire sl, cl, c2;
xor (sl, a, b); 
and (cl, a, b); 
xor (sum, sl, c-in) ; 
and (c2, sl, c-in); 
or (c-out, c2, cl); 
endmodule
```

##### Behavioural Modelling:

Using basic operators, we can construct digital circuits.

```
module fulladd4 (sum, c-out, a, b, c-in) ; 
// I/O port declarations 
output [3:0] sum; 
output c-out; 
input [3: 01 a, b; 
input c-in; 
// Specify the function of a full adder 
 {c-out, sum) = a + b + c-in; 
endmodul e
```
##### Dataflow Modelling

Using assign statements,we can construct digital circuits:

```
module fulladd4 (sum, c-out, a, b, c-in) ; 
// I/O port declarations 
output [3:0] sum; 
output c-out; 
input [3: 01 a, b; 
input c-in; 
// Specify the function of a full adder 
 {c-out, sum) = a + b + c-in; 
endmodul e
```

#### Operators:

Bitwise Operators:

```
~	bit-wise NOT
&	bit-wise AND
~&	bit-wise NAND
|	bit-wise OR
~|	bit-wise NOR
^	bit-wise XOR
~^	bit-wise XNOR
```

Logical Operators:

```
&&	logical AND
||	logical OR
!	logical NOT
```

Arithmetic Operators:

```
+	addition
-	subtraction
*	multiplication
/	division
%	modulus
**	Exponential operator
```

#### Branching Statements:

if-else-if statements 


```
//Type 1 conditional statement. No else statement. 
//Statement executes or does not execute. 
if (<expression>) true-statement ; 
//Type 2 conditional statement. One else statement 
//Either true-statement or false-statement is evaluated 
if (<expression>) true-sta tement ; else false-statement ; 
//Type 3 conditional statement. Nested if-else-if. 
//Choice of multiple statements. Only one is executed. 
if (<expressionl>) true-statement1 ; 
else if (<expression2>) true-statement2 ; 
else if (cexpression3>) true-statement3 ; 
else defaul t-statement ;

```

Case Statement

```
case ( expression) 
alternativel: statementl; 
alternative2: statement2; 
alternative3: statement3; 
... 
... default: defaul t-statement; 
endcase

```


#### Control Statements:

For Loop:

```
integer count;  
initial 
for ( count=O; count < 128; count = count + 1) 
$display("Count = %do, count); 
```

Repeat Loop

```
initial 
begin 
count = 0; 
repeat (128) 
begin 
$display("Count = %d", count); 
count = count + 1; 
end 
end
```
