from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

# 1. Initialize a quantum circuit with 3 qubits
num_qubits = 3
circuit = QuantumCircuit(num_qubits)

# 2. Apply Hadamard gates to all qubits to create an equal superposition
for qubit in range(num_qubits):
    circuit.h(qubit)

# 3. Verify using Statevector (Theoretical exact probabilities)
state = Statevector.from_instruction(circuit)
probs = state.probabilities_dict()

print("--- Theoretical Probabilities ---")
for state_str, prob in probs.items():
    print(f"State |{state_str}⟩: Probability = {prob:.3f} (Expected: 0.125)")

# 4. Verify using AerSimulator (Empirical counts from measurement)
circuit.measure_all()
simulator = AerSimulator()
result = simulator.run(circuit, shots=10000).result()
counts = result.get_counts()

print("\n--- Empirical Measurement Probabilities (10,000 shots) ---")
for state_str, count in sorted(counts.items()):
    empirical_prob = count / 10000
    print(f"State |{state_str}⟩: Measured Probability = {empirical_prob:.3f}")
