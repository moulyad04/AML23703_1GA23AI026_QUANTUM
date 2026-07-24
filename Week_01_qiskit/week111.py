import numpy as np
import random
import collections

# --- 1. Quantum Random Number Generator (Simulated) ---
def qrng_bit():
    # Initial state |0⟩
    state = np.array([1.0, 0.0])
    
    # Hadamard Gate Matrix
    H = (1 / np.sqrt(2)) * np.array([[1, 1],
                                     [1, -1]])
    
    # Apply Hadamard gate to create superposition
    superposition_state = np.dot(H, state)
    
    # Calculate probabilities from amplitudes (Amplitude squared)
    probabilities = np.abs(superposition_state) ** 2
    
    # Measure: collides the state into |0⟩ or |1⟩
    measured_bit = np.random.choice([0, 1], p=probabilities)
    return measured_bit

# --- 2. Generate and Compare ---
samples = 10000

# Generate quantum bits (simulated)
quantum_data = [qrng_bit() for _ in range(samples)]

# Generate classical pseudo-random bits
classic_data = [random.randint(0, 1) for _ in range(samples)]

# --- 3. Statistical Analysis ---
def analyze(data, name):
    counts = collections.Counter(data)
    mean = np.mean(data)
    variance = np.var(data)
    
    print(f"--- {name} ---")
    print(f"  Zeros: {counts[0]} | Ones: {counts[1]}")
    print(f"  Mean: {mean:.4f} (Ideal: 0.5000)")
    print(f"  Variance: {variance:.4f} (Ideal: 0.2500)\n")

analyze(quantum_data, "Quantum RNG (Simulated Superposition)")
analyze(classic_data, "Python PRNG (Mersenne Twister)")

# Check sequence reproducibility (The Determinism Test)
random.seed(42)
prng_seq1 = [random.randint(0, 1) for _ in range(5)]
random.seed(42)
prng_seq2 = [random.randint(0, 1) for _ in range(5)]

print("Determinism Test:")
print(f"  PRNG Run 1: {prng_seq1}")
print(f"  PRNG Run 2: {prng_seq2} (Identical seeds yield identical sequences)")
