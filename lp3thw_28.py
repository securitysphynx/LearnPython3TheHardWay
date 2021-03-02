# 11, 14, 16, and 19 have errors.  To be fixed. 

print("""
\t\tGood Tips: 
\t- Find an equality test and replace it with it's truth. 
\t- Solve any and/or inside parentheses first. 
\t- Invert each not. 
\t- Solve remaining and/or 
""")

line_break = "\n<================================>"

print(line_break)
print("1. True and True: ")
print("""\n\tSince this is in a truth table, we have reduced it to it's simplest form.
\tTRUE and TRUE equal TRUE
\tThis is: """, True and True)

print(line_break)
print("2. False and True: ")
print("""\n\tSince this is in a truth table, we have reduced it to it's simplest form.
\t FALSE and TRUE equal FALSE. 
\tThis is: """, False and True)

print(line_break)
print("3. 1 == 1 and 2 == 1: ")
print("""\t1 == 1 is TRUE.
\t2 == 1 is FALSE. 
\tTRUE and FALSE equals FALSE. 
\t. This is: """, 1 == 1 and 2 == 1)

print(line_break)
print('4. "test" == "test": ')
print('''\tThis is an equality test (==) in it\'s simplest form.
\ttest does not equal test. 
\tThis is: ''', ("test" == "test"))

print(line_break)
print("5. 1 == 1 or 2 != 1: ")
print("""\n\tThis is two equality tests on either side of an OR. 
\t1 == 1 evaluates to TRUE
\t2 != 1 evaluates to TRUE
\tso the truth table form is: 
\tTRUE or TRUE, which evaluates to TRUE.
\tThis is: """, (1 == 1 or 2 != 1))

print(line_break)
print("6. True and 1 == 1: ")
print("""\tThe equality test of 1 == 1 evaluates to TRUE
\tThe equation is reduced to the truth table base of TRUE and TRUE, which is TRUE
\tThis is: """, True and 1 == 1)

print(line_break)
print("7. False and 0 != 1: ")
print("""\tThe equality test of 0 != 1 evaluates to TRUE
\tThe equation is reduced to FALSE and TRUE, which is FALSE. 
\tThis is: """, False and 0 != 1)

print(line_break)
print("8. True or 1 == 1): ")
print("""\t1 == 1 is an equality test that is TRUE.
\tTRUE or TRUE is TRUE.
\tThis is: """, True or 1 == 1)

print(line_break)
print('9. test" == "testing": ', "test" == "testing")
print("""\t'test' == 'testing' is an equality test that is FALSE.
\tThis is: """, ("test" == "testing"))

print(line_break)
print("10. 1 != 0 and 2 == 1: ")
print("""\t1 != 0 is TRUE. 
\t2 == 1 is FALSE. 
\tTRUE and FALSE is FALSE. 
\tThis is: """,  (1 != 0 and 2 == 1))

print(line_break)
print("""11. test != testing""")
print("""\t1 != 0 is TRUE.
\t2 == 1 is FALSE.
\tTRUE and FALSE is FALSE.
\tThis is: """, ('test' != 'testing'))

print(line_break)
print('12. "test" == 1: ')
print("""\ttest == 1 is FALSE.
\tThis is: """, ("test" == 1 ))

print(line_break)
print("13. not (True and False): ")
print("""\tTRUE and FALSE is FALSE. 
\tnot FALSE is TRUE. 
\tThis is: """, (not (True and False)))

print(line_break)
print("14. not (1 == 1 and 0 != 1): ")
print("""\t1 == 1 is TRUE. 
\t 0 != 1 is FALSE. 
\tTRUE and FALSE is FALSE. 
\tnot FALSE is TRUE.
\tThis is :""", not (1 == 1 and 0 != 1))

print(line_break)
print("15. not (10 == 1 or 1000 == 1000): ")
print("""\t10 == 1 is FALSE. 
\t1000 == 1000 is TRUE.
\tFALSE or TRUE equals TRUE.
\t not TRUE is FALSE.
\t This is: """, not (10 == 1 or 1000 == 1000))

print(line_break)
print("16. not (1 != 10 or 3 == 4): ")
print("""\t1 != 0 is TRUE.
\t3 == 4 is FALSE. 
\tTRUE or FALSE is TRUE.
\tThis is: """, (not (1 != 10 or 3 == 4)))

print(line_break)
print('17. not ("testing" == "testing" and "Zed" ==  "Cool Guy"): ')
print("""\ttesting == testing is TRUE.
\tZed == Cool Guy is FALSE. 
\tTRUE and FALSE are FALSE.
\tThis is: """, ( not ("testing" == "testing" and "Zed" ==  "Cool Guy")))

print(line_break)
print('18. 1 == 1 and (not ("testing" == 1 or 1 == 0)): ')
print("""\ttesting == 1 is FALSE. 
\t1 == 0 is FALSE.
\tFALSE or FALSE is FALSE. 
\tnot FALSE is TRUE. 
\t1 == 1 is TRUE.
\tTRUE and TRUE is TRUE.
\tThis is: """, (1 == 1 and (not ("testing" == 1 or 1 == 0))))

print(line_break)
print('19. "chunky" == "bacon" and (not (3 == 4 or 3 == 3)): ', "chunky" == "bacon" and (not (3 == 4 or 3 == 3)))
print("""\t3 == 4 is FALSE.
\t3 == 3 is TRUE.
\tFALSE or TRUE is TRUE.
\tnot TRUE is FALSE.
\tchunky == bacon is FALSE.
\tFALSE and FALSE is TRUE.
\tThis is: """, ("chunky" == "bacon" and (not (3 == 4 or 3 == 3))))

print(line_break)
print('20. 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")): ')
print("""\ttesting == testing is TRUE. 
\t Python == Fun is FALSE. 
\tTRUE or FALSE equals TRUE. 
\tnot TRUE equals FALSE. 
\t3 ==3 is TRUE. 
\tTRUE and FALSE equals FALSE.  
\tThis is: """, (3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))))