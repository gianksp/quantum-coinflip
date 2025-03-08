# Quantum Coinflip

Welcome to **Quantum Coinflip**! This web app lets you flip a virtual coin using a real IBM Quantum Computer, demonstrating quantum randomness with an interactive 3D environment. Unlike traditional coin flips or pseudo-random number generators, this app leverages quantum superposition and measurement for true randomness, visualized with a stunning 3D coin animation.

## Overview
Quantum Coinflip uses a single-qubit quantum circuit executed on IBM's quantum hardware to generate a random outcome (Heads or Tails). The result is displayed with a 3D coin that spins and lands, created using Three.js. This project combines cutting-edge quantum computing with modern web technologies, making quantum mechanics accessible and engaging.

## How It Works
1. **Quantum Circuit**:
   - A single qubit is initialized and subjected to a Hadamard gate, placing it in a superposition state (50% chance of 0 or 1).
   - The qubit is then measured, collapsing its state to either 0 (Tails) or 1 (Heads).

2. **IBM Quantum Hardware**:
   - The circuit is sent to a real IBM Quantum Computer (e.g., `ibm_brisbane`) via the Qiskit SDK.
   - The hardware processes the quantum state and returns the measurement result.

3. **3D Visualization**:
   - Three.js renders a 3D coin with extruded shapes (Shiba Inu for Heads, paw print for Tails).
   - The coin spins for 2 seconds during the quantum computation, then lands on the result.

## Quantum Concepts Explained
### Superposition
- In quantum mechanics, a qubit can exist in a superposition of states (0 and 1 simultaneously) until measured. The Hadamard gate creates this 50/50 superposition, making each flip truly random.

### Measurement
- Measuring a qubit collapses its superposition to a definite state (0 or 1). This process is inherently probabilistic, unlike classical systems, ensuring genuine randomness.

### Quantum Randomness vs. Pseudo-Randomness
- **Pseudo-Random Number Generators (PRNGs)**: Used in traditional computing, PRNGs rely on algorithms and seeds, making them deterministic and predictable with enough data.
- **Quantum Randomness**: Based on the physical behavior of qubits, it’s unpredictable and unbiased, ideal for cryptography, simulations, and scientific experiments.
- **Advantage**: Quantum randomness provides a higher level of security and authenticity, as it’s not reproducible without re-measuring the quantum state.

## How IBM Handles Quantum Computing
- **Quantum Hardware**: IBM operates a fleet of quantum computers with superconducting qubits, accessible via the cloud. These are noisy intermediate-scale quantum (NISQ) devices, suitable for simple tasks like this coin flip.
- **Qiskit SDK**: The app uses Qiskit, IBM’s open-source quantum development kit, to construct and submit the circuit. The `Sampler` primitive runs the job on real hardware, with results returned after queue processing.
- **Access**: Free-tier users share backends, leading to potential delays (seconds to hours), mitigated by a 60-second timeout.
- **Noise and Errors**: Real quantum hardware introduces noise (e.g., gate errors), slightly affecting the ideal 50/50 outcome, adding to the authentic quantum experience.

## What to Expect
- **User Experience**: Click "Flip Coin" to start the 3D animation. The coin spins for 2 seconds while the quantum job processes, then lands on Heads or Tails with the backend name (e.g., "Result: Heads (via ibm_brisbane)").
- **Delays**: Due to IBM’s queue, results may take up to 60 seconds. A "Timeout" message appears if it exceeds this.
- **Visuals**: A large 3D coin (radius 3, height 0.3) with extruded Shiba Inu (Heads) and paw print (Tails) shapes, starting face-on and landing clearly.
- **Errors**: If Three.js fails to load or the quantum job fails, a text message will update you (e.g., "Error: 3D library failed to load").

## Setup and Development

### Prerequisites
- Python 3.8+
- Git
- An IBM Quantum account (free at [quantum-computing.ibm.com](https://quantum-computing.ibm.com/))
- A Render account (free tier available at [render.com](https://render.com/))

### Local Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/quantum-coinflip.git
   cd quantum-coinflip