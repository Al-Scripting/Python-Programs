
#Variables Used
name = str(input("Enter employee's name: "))
numHoursWorked = float(input("Enter number of hours worked in a week: "))
hourlyPayRate = float(input("Enter hourly payrate: "))
federalTax = float(input("Enter federal tax withholding rate: "))
stateTax = float(input("Enter state tax withholding rate: "))



print("#######################################################")

#name
print("Employee Name: ",name)

#hours worked
print("Hours Worked: ",numHoursWorked)

#payrate
print("Pay Rate: $",hourlyPayRate)

#gross pay
grossPay = numHoursWorked*hourlyPayRate
print("Gross Pay: $",float(grossPay))

print("Deductions: ")

#Federal Witholding
fedWithhold = grossPay * federalTax
print("\tFederal Withholding (%", federalTax*100,") : $", fedWithhold)

#State Tax Withholding
stateWithhold = grossPay * stateTax
print("\tState Withholding (%", stateTax*100,") : $", round(stateWithhold, 2))

#Total Dedections
totalDedections = fedWithhold+stateWithhold
print("\tTotal Dedections : $", totalDedections)

#Net Pay
netPay = grossPay-totalDedections
print("Net Pay: $", netPay)




