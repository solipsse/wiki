# Python
!!! note
    Interpreter read from top to bottom

## Data type in python
- int: 2, -12
- float: 2.0, -1.23
- string: "hello"
- boolean: True, False

## Variable
!!! note
    Python use type inference, and therefore can assign without declare
!!! note "convention"
    - **Snake case**: hello_world
    - **Camel case**: helloWorld

# Cheatsheet
## Common usage
Usage| Command
-|-
User input| `input('x: ')`
Assignment| `x = <data>`
Multiple Values| `x,y,z = '1','2','3'`
Console log| `print(variables, goes, here)`
List|`x=[int, str, bool, any]`
Length of iteratable object|`len()`
Range Function|`in range(start, stop, step)`
Slice operator|`list[start:stop:step] or list[:stop] or list[start:]`
Set|`s = set(elements)` or `s = {1,2,3}` only if not empty

## Operator
Arithmetic Operator|command
-|-
Addition|`+`
Subtraction|`-`
Multiplication|`*`
Division|`/`
Exponential| `**`
Floor Division| `//`
Mod| `%`

!!! note "Order of operation"
    use pemdas, bedmas, or whatever

???+ info "What if one of the operand is a float?"
    Output will remain the same number of precision of the most precise float.

Type conversion|command
-|-
to int|`int(number)`
to string| `str(any not list)`
to float| `float(number)`
what's the type?| `type(var)`
to list| `list(any)`

!!! note
    Maximum accurate decimal point is 13

String method|command
-|-
to uppercase|`str.upper()`
to lowercase| `str.lower()`
Capitalise| `str.capitalize()`
Count Occurence| `str.count(str)`
Repeat String| `str * int` times
Concatenate| `str + str`
ASCII value, ord| `ord(char)`

??? info "what exactly are string data type?"
    It is a class instance, so it has access to parent class method like `.upper()` and `.lower()`

List method|command
-|-
Append|`list.append(str)`
Extend|`list.extend(list)`
Pop|`list.pop(index)`
Element Assignment|`list[index]=...`
Duplicate|`list2 = list[:]`


!!! info
    Tuple is an immutable list -> no append, pop, etc... (x,y,z)

Conditional Operator|command
-|-
Equality|`==`
Inequality|`!=`
Comparison|`>, >=, <, <=`
And|`and`
Or|`or`
Not|`not`
conditional statement|`if ...: elif ...: else:`

!!! info
    Characters can be compared which represent through their ASCII value `'a' > 'b'` is false

Set method|command
-|-
Add|`set.add(any)`
Delete|`set.remove(element)`
Existent check|`element in set`
union, intersection, difference|`set.union(another set)` replace the union method with what's necessary

### Dictionary

`dict = {any data key: any value}`

- it is possible to find the `key in dict` <br>
- assignment works like on list
- to get a list of value from a dict `dict.values

### Iteration
#### For loops
```python
for index in range(start, stop, step):
    ...
for element in [list]:
    ...
for index, element in enumerate(list):
    ...
```
#### While Loops
```python
index/count = 0
while condition: #usually, the condition is base on max count, or other boolean, run only if TRUE
    ...
    index/count += 1
while True:
    ...
    i+= 1
    if exit-condition:
        break #only break the current loop or the child loop
```

## Playground
```python exec='1' source='tabbed-right'
arr = [1,2,3,'a']
print("helloworld"[::-1])
```

*[Floor Division]: divide by ... return the quotient
*[Mod]: divide by ... return the remainder
*[operand]: An object that operator acts on
*[Capitalise]: Capitalise first character and lowered case for all others
*[ord]: Ordinal values, something about being order
*[List]: Ordered, mutable, elements can be any data types, elements not need to be unique
*[Extend]: Concatenate list together
*[Pop]: removes element by index from list, removed item can be refer through `list.pop(index)`, default is the end index
*[Element Assignment]: This works because python's list is mutable
*[Duplicate]: Without `:` in the bracket, the `list2` will be refering to `list`
*[Range Function]: (start, stop, step), default start = 0 and step = 1
*[Slice operator]: start and stop are default on the outer element and the step is default as 1 `list[::-1]` will start at the right, end left because the step is in reverse direction. works on str, list and tuple
[Python in 90 mins]: https://www.youtube.com/watch?v=VchuKL44s6E
