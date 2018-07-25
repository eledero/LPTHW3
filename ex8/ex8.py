#Declares formatter with four string slots
formatter = "{} {} {} {}"

#Prints based on different versions of formatters
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))


#Print a formatter that is based on formaters in turn
a = formatter.format(1, 2, 3, 4)
b = formatter.format("a", "b", "c", "d")
c = formatter.format("One", "Two", "Thre", "Four")
d = formatter.format("Uno", "Dos", "Tres", "Cuatro")
print(formatter.format(a, b, c, d))
