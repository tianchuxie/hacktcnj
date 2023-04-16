import numpy as np
# import qutip
from qutip import *

# Create a qubit in the state |0>
qubit = qutip.basis(2, 0)

# Define a rotation matrix
theta = np.pi / 4
phi = np.pi / 4
R = qutip.qeye(2) * np.cos(theta / 2) - 1j * qutip.sigmaz() * np.sin(theta / 2) * np.exp(1j * phi)

# Generate the Bloch sphere animation
b = Bloch()
b.add_states(qubit)
b.add_states(R * qubit)
b.make_video()