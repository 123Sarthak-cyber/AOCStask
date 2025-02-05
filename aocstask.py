import numpy as np
import control as crtl1
import matplotlib.pyplot as pt


# Define the transfer function G(s) = 1 / (s^3 + 3s^2 + 5s + 1)
numerator = [1]
denominator = [1, 3, 5, 1]
G = crtl1.TransferFunction(numerator, denominator)
print(G) #Defining the transfer function using numerator/denominator
# PID Controller Parameters 
Kp = 8 
Ki = 3  
Kd = 4  
#Kp denotes the proportional gain,Ki denotes the integral gain,kd denotes the derivative gain.We have design the PID controller of our choice.
# Define the PID controller: C(s) = Kp + Ki/s + Kd*s
PIDctr = crtl1.TransferFunction([Kd, Kp, Ki], [1, 0])

# Closed-loop system: H(s) = (PID * G) / (1 + PID * G)
closed_loop_system = crtl1.feedback(PIDctr * G)


t = np.linspace(0, 10, 100) #Library function that creates an array of evenly spaced valuesover a specified interval

# Step response
T, resp = crtl1.step_response(closed_loop_system, t)
print(resp)

# Adding noise to simulate sensor inaccuracies
noise = np.random.normal(0, 0.01, len(resp))  
resp_noisy = resp + noise
print(resp_noisy)
# Plot the response
pt.figure(figsize=(10, 5))
pt.plot(T, resp, label="Ideal Response", linestyle='--')
pt.plot(T, resp_noisy, label="Noisy Response")
pt.xlabel("Time (s)")
pt.ylabel("System Output")
pt.title("PID Controller Response with Noise")
pt.legend()
pt.grid()
pt.show()
