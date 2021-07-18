weight = 4.8
#ground shipping
if weight <= 2:
  cost_ground = 1.50 * weight + 20.00
elif weight <= 6:
  cost_ground = 3.00 * weight + 20.00
elif weight <= 10:
  cost_ground = 4.00 * weight + 20.00
else:
  cost_ground = 4.75 * weight + 20.00

print('standard ground cost:', cost_ground)

#premium ground shipping
cost_ground_premium = 125.00

print('premium ground cost:', cost_ground_premium)

#drone shipping
if weight <= 2:
  cost_drone_shipping = 4.50 * weight
elif weight <= 6:
  cost_drone_shipping = 9.00 * weight
elif weight <= 10: 
  cost_drone_shiping = 12.00 * weight
else:
  cost_drone_shipping = 14.25 * weight

print('drone shipping cost:',cost_drone_shipping)
