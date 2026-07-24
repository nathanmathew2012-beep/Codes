# 1) Store the given values:
#    `mean1` (wrong mean), `wrong_number`, `correct_number`, and `total_number`.

# 2) Calculate the total sum using the wrong mean:
#    - Multiply `mean1` by `total_number`
#    - Store it in `sum`
#    - Print the sum.

# 3) Fix the sum to get the correct total:
#    - Remove the wrong number (subtract `wrong_number`)
#    - Add the correct number (add `correct_number`)
#    - Store the corrected total in `num2`
#    - Print the corrected sum.

# 4) Find the correct mean:
#    - Divide `num2` by `total_number`
#    - Store it in `mean2`
#    - Print `mean2`.
mean1 = 38
wrong_number=36
correct_number=56
total_number=40
#sum of 40 numbers
sum = mean1*total_number
print("the sum of 40 number: ",sum)

#correct sum of these numbers
num2=sum-((wrong_number)-(correct_number))
print("sum-((wrong_number)-(correct_number)): ",num2)

#the correct mean
mean2=num2/total_number
print(mean2)