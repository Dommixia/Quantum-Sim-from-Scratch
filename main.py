import numpy as np

# Qubits
zero = np.array([1,0], dtype = complex)
one = np.array([0,1], dtype = complex)
#Multi Qubits
q00 = np.kron(zero, zero)
q01 = np.kron(zero, one)
q10 = np.kron(one, zero)
q11 = np.kron(one, one)
#identity Matrix
I = np.eye(2, dtype = complex)
#Gates
H_gate = np.array([[1,1], [1,-1]], dtype = complex)/np.sqrt(2)
X = np.array([[0,1], [1,0]], dtype = complex)
Y = np.array([[0,-1j], [1j, 0]], dtype = complex)
Z = np.array([[1,0], [0, -1]], dtype = complex)
CNOT = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 0, 1],
                  [0, 0, 1, 0]], dtype=complex)
def normalize(state):
    norm = np.linalg.norm(state)
    return state / norm
def isNormalized(state):
    return np.isclose(np.sum(np.abs(state) ** 2), 1.0)

class Quantum(object):
    def applyGate(gate, state):
        return normalize(gate @ state)

    def measure(state, qubit_index, n_qubits):
        prob = np.abs(state) ** 2
        outcome = np.random.choice(len(state), p=prob)
        bit = (outcome >> (n_qubits - 1 - qubit_index)) & 1
        new_state = np.zeros(len(state), dtype=complex)
        for i in range(len(state)):
            if ((i >> (n_qubits - 1 - qubit_index)) & 1) == bit:
                new_state[i] = state[i]
        new_state = normalize(new_state)
        return bit, new_state
    # Multi Qubit Gates via Tensor Products
    def applyGateToQubit(gate, qubit_index, n_qubits, state):
        full_gate = np.array([[1]], dtype=complex)
        for i in range(n_qubits):
            if i == qubit_index:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, I)
        newState = normalize(full_gate @ state)
        assert isNormalized(newState), "State not normalized"
        return newState

    def applyCNOT(state):
        return normalize(CNOT @ state)

state = Quantum.applyGateToQubit(H_gate, 0, 2, q00)
bell_state = Quantum.applyCNOT(state)
bit, collapsed_state = Quantum.measure(bell_state, 0, 2 )
print(bell_state)
print(np.sum(np.abs(bell_state)**2))
print(f"Measured qubit 0: {bit}")
print(f"Collapsed state: {collapsed_state}")
print(f"Normalized: {isNormalized(collapsed_state)}")