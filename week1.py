from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 1-qubit circuit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Run on simulator with 1024 shots
simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()

# Get counts and plot histogram
counts = result.get_counts(qc)
print("Measurement results:", counts)

plot_histogram(counts)
plt.show()
