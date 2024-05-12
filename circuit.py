import cirq
qbits = cirq.LineQubit(n)
circuit = cirq.circuit(
     cirq.QuantmFouierTransform(qbits),
     cirq.phaseEstimation(qbits,exponent = 2),
     cirq.QuantmFouierTransform(qbits)
)
simulator = cirq.simulator()
result = simulator.run(circuit)
factors = result.measurements['phase_estimation'].values
print(factors)