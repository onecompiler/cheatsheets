---
title: R 
description: R Cheat Sheet gives you a quick reference of basic R markdown language. 
First appeared:	August 1993
Stable release:	4.2.1 / 23 June 2022
---
  
## What is R?
Introduction to R.<br>
R is a language and environment for statistical computing and graphics. It is a GNU project which is similar to the S language and environment which was developed at Bell Laboratories (formerly AT&T, now Lucent Technologies) by John Chambers and colleagues. R can be considered as a different implementation of S. There are some important differences, but much code written for S runs unaltered under R.

R provides a wide variety of statistical (linear and nonlinear modelling, classical statistical tests, time-series analysis, classification, clustering, …) and graphical techniques, and is highly extensible. The S language is often the vehicle of choice for research in statistical methodology, and R provides an Open Source route to participation in that activity.

One of R’s strengths is the ease with which well-designed publication-quality plots can be produced, including mathematical symbols and formulae where needed. Great care has been taken over the defaults for the minor design choices in graphics, but the user retains full control.

R is available as Free Software under the terms of the Free Software Foundation’s GNU General Public License in source code form. It compiles and runs on a wide variety of UNIX platforms and similar systems (including FreeBSD and Linux), Windows and MacOS.
  
  
## The R environment
R is an integrated suite of software facilities for data manipulation, calculation and graphical display. It includes

an effective data handling and storage facility,
a suite of operators for calculations on arrays, in particular matrices,
a large, coherent, integrated collection of intermediate tools for data analysis,
graphical facilities for data analysis and display either on-screen or on hardcopy, and
a well-developed, simple and effective programming language which includes conditionals, loops, user-defined recursive functions and input and output facilities.
The term “environment” is intended to characterize it as a fully planned and coherent system, rather than an incremental accretion of very specific and inflexible tools, as is frequently the case with other data analysis software.

R, like S, is designed around a true computer language, and it allows users to add additional functionality by defining new functions. Much of the system is itself written in the R dialect of S, which makes it easy for users to follow the algorithmic choices made. For computationally-intensive tasks, C, C++ and Fortran code can be linked and called at run time. Advanced users can write C code to manipulate R objects directly.

Many users think of R as a statistics system. We prefer to think of it as an environment within which statistical techniques are implemented. R can be extended (easily) via packages. There are about eight packages supplied with the R distribution and many more are available through the CRAN family of Internet sites covering a very wide range of modern statistics.

R has its own LaTeX-like documentation format, which is used to supply comprehensive documentation, both on-line in a number of formats and in hardcopy.
 
  
## Sample program Hello World Program in R

```R
> # We can use the print() function
> print("Hello World!")
[1] "Hello World!"
> # Quotes can be suppressed in the output
> print("Hello World!", quote = FALSE)
[1] Hello World!
> # If there are more than 1 item, we can concatenate using paste()
> print(paste("How","are","you?"))
[1] "How are you?"
```  

## There are three important sections of an R Markdown document. 

* **Header:** The first one is the header at the top, bounded by the three dashes. This is where the user specifies the details like the title, name, the date, and what kind of document you want to output. If the user has filled in the blanks in the window earlier, these should be already filled out.
<br><br>
* **Text:** Also on this page, one can see text sections, for example, one section starts with “## R Markdown” this section will render as text when the PDF of this file is produced and all of the formattings that the user will learn generally applies to this section.
<br><br>
* **Code:** Chunk: And finally, the user will see code chunks. These are bounded by the triple backticks. These are pieces of R code chunks that can run right from within the document and the output of this code will be included in the PDF when created. The easiest way to see how each of these sections behave is to produce the PDF.
