import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import (
    plot_bloch_multivector,
    plot_state_qsphere
)

qc2 = QuantumCircuit(1)

qc2.h(0)
qc2.s(0)

print(qc2)

state = Statevector.from_instruction(qc2)

print("\nStatevector:")
print(state)

plot_bloch_multivector(state)
plt.show()
