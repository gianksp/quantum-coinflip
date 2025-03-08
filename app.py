from flask import Flask, render_template, jsonify
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import Sampler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flip', methods=['POST'])
def flip_coin():
    print("Hello World! Flipping a quantum coin...")
    
    # Create a 1-qubit circuit with 1 classical bit
    circuit = QuantumCircuit(1, 1)  # 1 qubit, 1 classical bit
    circuit.h(0)
    circuit.measure(0, 0)
    
    # Use local Aer simulator
    backend = AerSimulator()
    
    # Transpile the circuit for the target backend
    transpiled_circuit = transpile(circuit, backend=backend)
    
    # Run with Sampler
    sampler = Sampler(mode=backend)
    job = sampler.run([transpiled_circuit], shots=1)
    result = job.result()
    
    # Access counts from the measurement register
    print(result[0].data)
    counts = result[0].data.c.get_counts()
    outcome = list(counts.keys())[0]  # '0' or '1'
    
    # Map to coin flip
    coin_result = "Tails" if outcome == '0' else "Heads"
    return jsonify({"result": coin_result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)