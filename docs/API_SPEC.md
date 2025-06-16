# Python GameClient Backend API Specification

This document outlines the RESTful API endpoints exposed by the Python `GameClient` backend.

## Base URL

The base URL for all API endpoints is typically `http://localhost:5000` during local development.

## Endpoints

### 1. `GET /`

*   **Description**: Serves the main HTML page of the web frontend.
*   **Response**: `text/html` content of `index.html`.

### 2. `GET /api/connect_server`

*   **Description**: Initiates an attempt to connect the Python backend to the C `GameServer`. This is a simplified endpoint for demonstration; in a real application, connection management would be more robust.
*   **Response**: `application/json`
    ```json
    {
      "message": "Attempting to connect to C server..."
    }
    ```

### 3. `GET /<path:filename>`

*   **Description**: Serves static files (CSS, JavaScript, images) from the `client/frontend/public` directory.
*   **Parameters**:
    *   `filename` (path parameter): The name of the static file to serve (e.g., `style.css`, `index.js`).
*   **Response**: The content of the requested static file with the appropriate `Content-Type` header.

## Future API Endpoints (Planned)

The following endpoints are envisioned for future development to support game interactions:

*   `POST /api/draw_card`: Request to draw a card.
*   `POST /api/play_card`: Request to play a card, with card ID and optional target.
*   `GET /api/game_state`: Get the current game state from the backend.
*   `GET /api/player_hand`: Get the current player's hand.
*   `GET /api/players`: Get information about all active players.
