a = [2200, 2350, 2600, 2130, 2190]
# Expansive months such as January = 2200, February = 2350, March = 2600, April = 2130 and May = 2190
# Now to compare to spend January and Februarya
b = a[1]-a[0]
print(b)   # 150

# Now Find out toital expansive in First three months in a years

c = a[0] + a[1] + a[2] + a[3]
print(c) # 9280

# Now Find out if You sepend Exectly 2000 dollors in any months

if a == 200:
    print("Yes")
else:
    print("No")

# Now June months just finish and yours expansive is 1980 dollor. Add this iten in Months

a.append(1980)
print(a)

# You returned an item that you bought in a month of April and
#got a refund of 200$. Make a correction to your monthly expense list

a[3] = a[3] - 200
print(a)