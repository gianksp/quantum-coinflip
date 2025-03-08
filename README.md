# Quantum Coinflip

![Quantum Coinflip Screenshot](https://i.ibb.co/BXp3Dh8/coinflip.png)

Welcome to **Quantum Coinflip**! This web app lets you flip a virtual coin using a real IBM Quantum Computer, demonstrating quantum randomness with an interactive 3D environment. Unlike traditional coin flips or pseudo-random number generators, this app leverages quantum superposition and measurement for true randomness, visualized with a stunning 3D coin animation.

**Try it now!** Play with the live version on Render: [https://quantum-coinflip.onrender.com](https://quantum-coinflip.onrender.com)

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

Experience the quantum coin flip in action: [https://quantum-coinflip.onrender.com](https://quantum-coinflip.onrender.com)

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
- **Access**: Free-tier users share backends, leading to potential delays (seconds to hours), mitigated by a 25-second timeout. Additionally, free-tier IBM Quantum accounts have a monthly limit on quantum resources, which may be reached, causing job failures.
- **Noise and Errors**: Real quantum hardware introduces noise (e.g., gate errors), slightly affecting the ideal 50/50 outcome, adding to the authentic quantum experience.

## What to Expect
- **User Experience**: Click "Flip Coin" to start the 3D animation. The coin spins for 2 seconds while the quantum job processes, then lands on Heads or Tails with the backend name (e.g., "Result: Heads (via ibm_brisbane)").
- **Delays**: Due to IBM’s queue, results may take up to 25 seconds. A "Timeout" message appears if it exceeds this.
- **Visuals**: A 3D coin with extruded Shiba Inu (Heads) and paw print (Tails) shapes, starting face-on and landing clearly.
- **Errors**: If Three.js fails to load, the quantum job fails (e.g., due to monthly limits or timeouts), or the Render free tier runs out of resources, a text message will update you (e.g., "Error: 3D library failed to load" or "Timeout: Quantum hardware is busy"). Note that the free tier on Render and IBM Quantum may lead to occasional failures or resource exhaustion.
- **Resource Limits**: As this app uses the free tiers of Render and IBM Quantum, you may encounter service interruptions if the monthly quantum resource limit is reached or if Render’s memory/timeout constraints are exceeded.

Want to see it in action? Visit the live demo: [https://quantum-coinflip.onrender.com](https://quantum-coinflip.onrender.com)

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
   ```

2. **Set Up a Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Obtain IBM Quantum Token**:
    Sign into [quantum-computing.ibm.com](https://quantum-computing.ibm.com/).
    Generate a token under "My Account" and copy it.

5. **Set Environment Variable**:
    ```bash
    set IBM_QUANTUM_TOKEN=your-ibm-token-here
    ```
- Or use a .env file.

6. **Run Locally**:
    ```bash
    python app.py
    ```

### Deploying to Render

1. **Push to GitHub**
- Ensure your codeis in a GitHub repository:
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```
- The repository should be public for free-tier Render deployment, or private if on a paid plan.

2. **Sign Up for Render**
- Create an account at [render.com](https://render.com/).
- Link your GitHub account to allow Render to access your repository.

3. **Create a Web Service**
- From the Render Dashboard, click New > Web Service.
- Select Build and deploy from a Git repository.
- Choose your quantum-coinflip repository and click Connect.

4. **Configure the Service**
- Name: quantum-coinflip
- Environment: Python 3
- Branch: main
- Build Command: pip install -r requirements.txt
- Start Command: gunicorn app:app
- Instance Type: Free (for testing; upgrade for production to avoid timeouts or resource limits)
- Environment Variables:
-   Key: IBM_QUANTUM_TOKEN
-   Value: Your IBM Quantum token
- Click Create Web Service.

5. **Monitor Deployment**
- Render will build and deploy your app.
- Check the Events tab for logs.
- Once deployed, access your app at the provided URL: https://quantum-coinflip.onrender.com.

### Contributing
- Fork the repository and submit pull requests.
- Suggestions for improving the 3D model, quantum circuit, or UI are welcome!
- Report issues on the GitHub Issues page.

### License
- MIT License (or specify your preferred license).

### Acknowledgements
- Powered by IBM Quantum and Qiskit.
- 3D visualization with Three.js.
- Deployed on Render.