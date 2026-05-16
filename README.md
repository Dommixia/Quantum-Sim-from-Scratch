# Quantum Simulator from Scratch

A quantum circuit simulator built entirely from NumPy and linear algebra — no Qiskit, no abstractions. Implements single and multi-qubit gates, tensor products, entanglement, and measurement.

## What it does

Simulates quantum circuits by representing qubit states as complex vectors and quantum gates as matrices. Apply gates via matrix multiplication, create entanglement with CNOT, and measure qubits probabilistically.

## Core Components

**Qubit states** — represented as 2-element complex vectors. Single |0⟩ and |1⟩, or combined multi-qubit states via tensor product.

**Quantum gates** — X, Y, Z, H gates as 2x2 matrices. Apply to single qubits or expand to multi-qubit systems via tensor product with identity.

**CNOT gate** — 4x4 matrix that creates entanglement between two qubits. Flips target qubit only if control qubit is |1⟩.

**Measurement** — collapses qubit state probabilistically based on amplitudes. Outcome determined by |α|² and |β|².

## Math Behind It

Every quantum operation is matrix multiplication:
new_state = gate_matrix @ state_vector

Multi-qubit gates are built via tensor products:    
gate_on_qubit_0 = gate ⊗ I
gate_on_qubit_1 = I ⊗ gate

Entanglement is created by applying CNOT to a superposition state:
H on q0 → 1/√2(|00⟩ + |10⟩)
CNOT    → 1/√2(|00⟩ + |11⟩)

Normalization is enforced after every operation:
norm = √(Σ|αᵢ|²)    state = state / norm

General gate application to qubit q in an n-qubit system:
full_gate = I ⊗ ... ⊗ gate ⊗ ... ⊗ I  (gate at position q)

Measurement collapses state to subspace consistent with outcome:
1. Sample outcome using Born rule probabilities |αᵢ|²
2. Zero all amplitudes where qubit q ≠ measured bit
3. Renormalize collapsed state

## Key Features

- Pure NumPy — no quantum computing frameworks
- Single and multi-qubit support
- All basic gates (X, Y, Z, H)
- CNOT for entanglement
- Probabilistic measurement
- Bell state creation and verification
- Normalization enforced after every gate operation
- General n-qubit gate application via tensor product expansion
- State collapse after measurement with post-measurement state returned

## Tech Stack

- Python
- NumPy (linear algebra only)

## Setup

```bash
pip -r requirements.txt
python main.py
```

## Results

Bell state measurement across 100 trials shows entanglement:
- Always measures |00⟩ or |11⟩
- Never measures |01⟩ or |10⟩
- Proves qubits are correlated despite being separate

## Key Learnings

- Quantum states are vectors, gates are matrices
- Tensor products combine multi-qubit systems
- Matrix multiplication applies quantum operations
- Entanglement emerges from CNOT + superposition
- Measurement collapses superposition probabilistically
- Measurement extracts one qubit's value via bit manipulation on outcome index