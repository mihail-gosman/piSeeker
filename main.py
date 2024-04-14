import pyseeker.leibniz
import pyseeker.leibniz_pi

iterations = 10**9

#estimation1, time = pyseeker.leibniz.leibniz(iterations)
estimation2, time2 = pyseeker.leibniz_pi.leibniz_pi(iterations)

#print(f"Vanilla estimation pi={estimation1} in {time} seconds")
print(f"Numpy method pi={estimation2} in {time2}")