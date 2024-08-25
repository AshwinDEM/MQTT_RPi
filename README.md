# MQTT Protocol Implementation on Raspberry Pi 4

## Description
This project demonstrates the implementation of the MQTT protocol on a Raspberry Pi 4. The protocol is used in publisher/subscriber models and incorporates basic blockchain functionality, encryption using Elgamal, and is developed with Python 3.12.

## Features
- Publisher/Subscriber model using MQTT
- Basic blockchain functionality
- Elgamal encryption for secure communication
- Developed with Python 3.12

## Requirements
### Hardware
- Raspberry Pi 4

### Software
- Python 3.12

## Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/mqtt-raspberry-pi.git
    cd mqtt-raspberry-pi
    ```

2. **Install the required Python libraries**:
    ```sh
    pip install paho-mqtt pycryptodome
    ```

## Usage
1. **Run the publisher**:
    ```sh
    python publisher.py
    ```

2. **Run the subscriber**:
    ```sh
    python subscriber.py
    ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.