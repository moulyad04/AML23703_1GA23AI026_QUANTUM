import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
    plot_bloch_multivector,
    plot_state_qsphere
)

qc1 = QuantumCircuit(1)

# Apply X gate
qc1.x(0)

print("Circuit:")
print(qc1)

state = Statevector.from_instruction(qc1)

print("\nStatevector:")
print(state)

plot_bloch_multivector(state)
plt.show()
