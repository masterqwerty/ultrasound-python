import UltraSound

us = UltraSound.UltraSound(1, 5, 1, 1)

I_1 = us.reflect(100, 200)
I_2 = us.propagate(0.9, 3)

print(I_1, I_2)

