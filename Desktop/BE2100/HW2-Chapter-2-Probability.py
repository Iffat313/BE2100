print("Problem:  An injection-molded part is equally likely to be obtained from any one of the eight cavities on a mold.\n")
print("a. What is the sample space?:")
print("In a problem like this, the sample space is the number of events. Because each outcome is equally likly with each event, we count a event as one. Because there are 8 cavities that means there are 8 events. ")
print("In short, the sample space is 8, thus being 8 potiental outcomes.")
print("S = {1,1,1,1,1,1,1,1} = 8 or S = {1st even, 2nd event...}")

print("\n")
print("b. What is the probability that a part is from cavity 1 or 2?: ")
print("The probability of 'A' outcome is = 1/S where S = to the sample space, 8")
print("However, the probability of obtaining ONE outcome from  A SET of 'k' outcomes is:")
print("P(Asub1) + P(Asub2) +...+ P(Asubk)")
print("P(1,2) = 1/8 + 1/8 = 2/8 = 1/4")

print("\n")
print("c. What is the probability that a part is from neither cavity 3 nor 4?")
print("There are two ways to go about it: \n")
print("Logical way: ")
print("Because you do not want cavity 3 or 4, the desried outcome increases. You see, this means you're okay with getting an injection mold from cavity 1,2,4,5,6,7 and 8. In fact, you could also interperet it as P(1,2,5,6,7,8) \n")
print("Formula way:")
print("The formula is  P(3',4') = P(S) - P(3,4)")
print("The probability of S is always 1. Based on what we learned earlier, the probability of 3,4 is 1/8 + 1/8 = 1/4. 1 - 1/4 = 4-1/4 = 3/4 ")



