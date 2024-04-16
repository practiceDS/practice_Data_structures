#String Manipulation :- "Input: This_Is_A_Good_Morning
#                 Output:tHIS.iS.a.gOOD.mORNING"


input_string = "This_Is_A_Good_Morning"
swapped_string = input_string.swapcase()
output_string = swapped_string.replace('_','.')
print(output_string)



