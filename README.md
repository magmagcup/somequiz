## 1. First application feature
>>>>>>>>

Creating a program that store data for all student. 

* last 4 digit number of student id 
* First name
* grade

~~~
Welcome to program((A)dd/(Q)uit): A
Last 4 digit: 6054
First name: Sirawich
Grade: 3.16
Welcome to program((A)dd/(Q)uit):
~~~

## 2. Print all of the information.
~~~
Welcome to program((A)dd/(Q)uit/(P)rint): P
~~~
ID: 6054

Name: Sirawich

Grade: 3.16
~~~
Welcome to program((A)dd/(Q)uit/(P)rint): A
Last 4 digit: 5555
First name: Payaya
Grade: 3.00
Welcome to program((A)dd/(Q)uit/(P)rint): P 
~~~
ID: 6054

Name: Sirawich

Grade: 3.16

ID: 5555

Name: Payaya

Grade: 3.00

## 3. Check input
#### Condition:
*   Input for an ID isn't 4 digit int (9999 >= x >= 0000),
    get new input, Repeat until user put a correct information.
*   Input for a grade isn't 2 decimal float (4.00 >= x >= 0.00),
    get new input, Repeat until user put a correct information.
~~~
Welcome to program((A)dd/(Q)uit/(P)rint): A
Last 4 digit: abcs
Last 4 digit must be an integer: ok
Last 4 digit must be an integer: 1234
First name: mag
Grade: 9000
Grade must be a float with 2 decimal: 1.23
Welcome to program((A)dd/(Q)uit/(P)rint):
~~~

## 4. Print individual student
Creating second page menu inside choice "P" which have the following function.
: Printing individual student from id number
: Printing all student inside
~~~
Welcome to program((A)dd/(Q)uit/(P)rint): P
(I)d / (A)ll: I
ID number: 1
~~~
ID: 5555

Name: Payaya

Grade: 3.00
~~~
Welcome to program((A)dd/(Q)uit/(P)rint): P
(I)d / (A)ll: A
~~~
ID: 6054

Name: Sirawich

Grade: 3.16

ID: 5555

Name: Payaya

Grade: 3.00

ID: 1234

Name: mag

Grade: 1.23
