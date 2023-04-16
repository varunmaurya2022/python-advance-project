''' The assert Satatement is useful to ensure that a given condition is True. If it is not true, it raises
Assertion Error.
Syntax:-assert condition, error_message
1. If the condition ids False then the exception by the name AssertionError is raised along with the message.
2. if message is not given and the condition is False then also AssertionError is raised without 
message.'''
a=10
assert a<=10,"Invalid Number"
print(a)