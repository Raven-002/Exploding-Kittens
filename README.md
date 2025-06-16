# Exploding Kittens Project

This project implements a simplified version of the Exploding Kittens card game. It consists of a C-based game server and a Python-based game client with a vanilla web frontend.

## Architecture Overview

*   **GameServer (C)**: Manages game state, logic, and network communication.
*   **GameClient (Python Backend)**: Connects to the C GameServer, manages client-side game state, and serves the web frontend.
*   **GameClient (Web Frontend)**: Provides a simple, interactive user interface for players using vanilla HTML, CSS, and JavaScript.

## Setup Instructions

### Prerequisites

*   **C Development Tools**: `gcc` or `clang`, `cmake`, `make`
*   **Python**: Python 3.8+
*   **Git**: For version control

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Exploding-Kittens.git
cd Exploding-Kittens
```

### 2. GameServer Setup (C)

```bash
cd server
mkdir build
cd build
cmake ..
make
# To run tests (after implementing them)
# make test
cd ../..
```

### 3. GameClient Setup (Python)

#### Backend

```bash
cd client
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd ..
```

#### Frontend

The frontend is vanilla HTML/CSS/JavaScript and does not require a separate build step or package manager.

### 4. Running the Application

1.  **Start the GameServer:**
    ```bash
    cd server/build
    ./GameServerExecutable # Replace with actual executable name
    cd ../..
    ```
2.  **Start the GameClient Backend:**
    ```bash
    cd client
    source venv/bin/activate
    python backend/app.py
    cd ..
    ```
3.  **Access the Web Frontend:**
    Open your web browser and navigate to the address where the Python backend is serving the frontend (e.g., `http://localhost:5000`).

## Testing

*   **C GameServer Tests**: Run using `make test` in the `server/build` directory.
*   **Python GameClient Backend Tests**: Run using `pytest` in the `client` directory (after activating the virtual environment).
*   **Web Frontend Tests**: Currently, manual testing in the browser.

## Contributing

(Add contribution guidelines here)

## License

This project is licensed under the [LICENSE_TYPE] License - see the [LICENSE](LICENSE) file for details.
