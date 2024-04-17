import time
start_time = time.time()

def num2text_in(n):
    if n < 0:
        print("Please, Don't put Negetive numbers") 
    else:
        raw_n = int(n)
        n =str(raw_n).zfill(9)

        n1 = int(n[8])
        n2 = int(n[7])
        n3 = int(n[6])
        n4 = int(n[5])
        n5 = int(n[4])
        n6 = int(n[3])
        n7 = int(n[2])
        n8 = int(n[1])
        n9 = int(n[0])
        n = int(n)  

        ones = { 0: "", 1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 
            6: "Six ", 7: "Seven ", 8: "Eight ", 9: "Nine "}  
        tens = { 0 : "", 2 : "Twenty ", 3: "Thirty ", 4: "Forty ", 5: "Fifty ", 6: "Sixty ", 7: "Seventy ",
                8: "Eighty ", 9: "Ninety ",} 
        orders = { 3:"Hundred ", 5:"Thousand ", 7:"Lakh ", 9:"Crore "}

        def elv_enable(p,q):
            elevens = { 10: "Ten ", 11: "Eleven ", 12: "Twelve ", 13: "Thirteen ", 14: "Fourteen ", 
                    15: "Fifteen ", 16: "Sixteen ", 17: "Seventeen ", 18: "Eighteen ", 19: "Nineteen "}       
            if p == 1:
                elv = int(str(p)+str(q))
                elv1 = elevens[elv]
                p = 0 
                q = 0
            else:
                elv1 =""
            return elv1 , p , q
        
        if n == 0:
            print("Zero")    
        if n < 1000000000:
            if n3 == 0:
                orders[3] = ""
            if n5+n4 == 0:
                orders[5] = ""
            if n7+n6 == 0:
                orders[7] = ""
            if n9+n8 == 0:
                orders[9] = ""

            elv , n2 , n1 = elv_enable(n2,n1)
            elvt , n5 , n4= elv_enable(n5,n4)
            elvl , n7 , n6= elv_enable(n7,n6)
            elvc , n9 , n8= elv_enable(n9,n8)

            text = f"{elvc}{tens[n9]}{ones[n8]}{orders[9]}{elvl}{tens[n7]}{ones[n6]}{orders[7]}{elvt}{tens[n5]}{ones[n4]}{orders[5]}{ones[n3]}{orders[3]}{elv}{tens[n2]}{ones[n1]}"
        else: 
            text = "Sorry! it's only limited to 99 Crore. if you're that rich. pay me more"
        return text

while True:
  n = int(input("Total money (in Number): "))

  txt = num2text_in(n)

  print(f"Total Money (in words): {txt} ")

  choice = input("Do you want to continue? (y/n): ")
  if choice.lower() != "y":
    break
# i = -530
# while i < 1000000000:
#     n = i
#     print(f"Total money (in Number): {n}")
#     txt = num2text_in(n)
#     print(f"Total money (in words): {txt} ")
#     i = i + 794256111


print("Thank you for using the program!")
end_time = time.time()

execution_time = end_time - start_time

print(f"Execution time: {execution_time:.4f} seconds")