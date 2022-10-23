
## What Is A List Comprehension
List comprehensions are a really cool way to add data to a list in python, from within the list itself. For example, say we wanted to populate a list with numbers from 0-5, we could use a for loop to accomplish this as follows:

```python
nums = []

for i in range(6):
    nums.append(i)

print(nums)
```
Which would result in the following

```bash
[0, 1, 2, 3, 4, 5]
```

Doing this would give us an array that contains numbers from 0 - 5 , just like we wanted however there's a much cooler way to achieve this, and moreso its a "one-liner". Let's  see how:

```python
nums = [x for x in range(6)]

print(nums)
```

This took us from roughly 5 lines of code to one!. So let me explain what just happened. To create a list comprehension, you create a list first and then add logic for the data inside the square brackets. Usually it follows this template:

```bash
array = [x(placeholder variable) (for statement)]
```

- `x`: is the placeholder variable and represents every item in the list. It's exactly like the for loop variable in the first example `i`. It is always the first part of the list comprehension

- `for statement`: this is the for-loop that populates the list with actual values for x, and can take any form you want, you could even have conditional blocks in it.

Let's see an example of list comprehension that uses conditional statements in it. If we wanted to populate a list with letters or characters from a word except vowels in it we could use a list comprehension to accomplish that as follows:

```python
vowels = 'aeiou'

letters = [x for x in "apple" if x not in vowels]

print(letters)
```

This would result in the following:

```bash
['p', 'p', 'l']
```

We could also include an `else` statement however we need to put the `if` and `else` block before the `for` loop.

```python
vowels = 'aeiou'

letters = [x if x not in vowels else 0 for x in "apple"]

print(letters)
```

This would result in the following:

```bash
[0, 'p', 'p', 'l', 0]
```

This is obviously a much easier way to populate your lists in python and can come in handy when you don't have the luxury of writing a full loop. Have fun coding!.
