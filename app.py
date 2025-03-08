from flask import Flask, render_template, jsonify
from qiskit import QuantumCircuit, transpile
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler
import os

app = Flask(__name__)

# Initialize Qiskit Runtime Service with token from environment variable
IBM_TOKEN = os.getenv("IBM_QUANTUM_TOKEN")
if not IBM_TOKEN:
    raise ValueError("IBM_QUANTUM_TOKEN environment variable not set")
service = QiskitRuntimeService(channel="ibm_quantum", token=IBM_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flip', methods=['POST'])
def flip_coin():
    print("Flipping a quantum coin on real IBM hardware...")
    
    # Create a minimal 1-qubit circuit
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    
    # Select the least busy real quantum backend
    backend = service.least_busy(operational=True, simulator=False, min_num_qubits=1)
    print(f"Using backend: {backend.name}")
    
    # Transpile with optimization
    transpiled_circuit = transpile(circuit, backend=backend, optimization_level=2)  # Increased optimization
    
    # Run with Sampler and a reduced timeout (e.g., 25 seconds to fit Render free tier)
    sampler = Sampler(mode=backend)
    job = sampler.run([transpiled_circuit], shots=1)
    try:
        result = job.result(timeout=25)  # Reduced from 60 to 25 seconds
        counts = result[0].data.c.get_counts()
        outcome = list(counts.keys())[0]  # '0' or '1'
        coin_result = "Tails" if outcome == '0' else "Heads"
    except Exception as e:
        print(f"Job timed out or failed: {str(e)}")
        return jsonify({"result": "Timeout: Quantum hardware is busy", "backend": backend.name}), 503
    
    return jsonify({"result": coin_result, "backend": backend.name})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)