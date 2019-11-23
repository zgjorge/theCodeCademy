train_mass = 22680
train_acceleration = 10
train_distance = 100
f100_in_celsius = 100

bomb_mass = 1

# Convert from Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = (f_temp -32) * 5/9
  return c_temp


the_value = f_to_c(f100_in_celsius)
print(the_value)

# Convert from Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Train Force 
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Train Energy
def get_energy(mass, c = 3*10**8):
  return mass * c*c

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# Get work
def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over "+ str(train_distance) + " meters.")

