import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
    plot_bloch_multivector,
    plot_state_qsphere
)
qc3 = QuantumCircuit(2)

qc3.h(0)
qc3.h(1)

print(qc3)

state = Statevector.from_instruction(qc3)

print("\nStatevector:")
print(state)

print("\nProbabilities:")
print(state.probabilities())

print("Sum of probabilities =", np.sum(state.probabilities()))

plot_state_qsphere(state)
plt.show()