import json
from braket.circuits import Circuit
from braket.aws import AwsDevice

def lambda_handler(event, context):
    coinflip_circuit = Circuit().h(0)  # Hadamard gate for superposition
    device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
    task = device.run(coinflip_circuit, shots=1)
    result = task.result()
    measurement = result.measurements[0][0]
    coin_result = "Tails" if measurement == 0 else "Heads"
    return {
        "statusCode": 200,
        "body": json.dumps({"result": coin_result}),
        "headers": {"Content-Type": "application/json"}
    }