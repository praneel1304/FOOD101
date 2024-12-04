def slope_of_cubic(coefft,x):
 int(x)
 if len(coefft) != 4: 
      print("give tuple containing exactly 4 elements for coefficients")
      return
 sum = 3*(int(coefft[0]))*x*x +2*x*(int(coefft[1]))+(int(coefft[2]))
 return sum
