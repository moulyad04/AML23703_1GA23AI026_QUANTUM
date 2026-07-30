import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
    plot_bloch_multivector,
    plot_state_qsphere
)
theta = np.random.uniform(-0.2, 0.2)

qc4 = QuantumCircuit(1)

qc4.h(0)

# Phase error
qc4.p(theta, 0)

print("Random phase =", theta)

state = Statevector.from_instruction(qc4)

print(state)

plot_bloch_multivector(state)
plt.show()
