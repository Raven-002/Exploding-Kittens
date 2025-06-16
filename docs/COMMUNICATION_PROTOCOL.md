# Communication Protocol

This document defines the binary communication protocol used between the C `GameServer` and the Python `GameClient`.

## General Message Structure

All messages will follow a common header structure, followed by a message-specific payload.

| Field        | Size (Bytes) | Description                                     |
| :----------- | :----------- | :---------------------------------------------- |
| `Message Type` | 1            | Identifies the type of message (e.g., `JOIN_GAME`). |
| `Payload Length` | 2            | Length of the `Payload` in bytes (max 65535). |
| `Payload`    | Variable     | Message-specific data.                          |

## Message Types

### 1. `JOIN_GAME` (Type: `0x01`)

*   **Description**: Sent by the client to request joining a game.
*   **Payload**:
    | Field    | Size (Bytes) | Description                               |
    | :------- | :----------- | :---------------------------------------- |
    | `Player Name Length` | 1            | Length of the player name string.         |
    | `Player Name` | Variable     | UTF-8 encoded string of the player's name. |

### 2. `DRAW_CARD_REQUEST` (Type: `0x02`)

*   **Description**: Sent by the client to request drawing a card.
*   **Payload**: Empty

### 3. `PLAY_CARD_REQUEST` (Type: `0x03`)

*   **Description**: Sent by the client to request playing a card.
*   **Payload**:
    | Field    | Size (Bytes) | Description                               |
    | :------- | :----------- | :---------------------------------------- |
    | `Card ID` | 1            | Identifier for the card being played.     |
    | `Target Player ID` | 1            | Optional: ID of the target player for certain cards (e.g., Attack, Nope). `0` if no target. |

### 4. `GAME_STATE_UPDATE` (Type: `0x10`)

*   **Description**: Sent by the server to update clients on the current game state.
*   **Payload**:
    | Field    | Size (Bytes) | Description                               |
    | :------- | :----------- | :---------------------------------------- |
    | `Current Player ID` | 1            | ID of the player whose turn it is.        |
    | `Deck Size` | 2            | Number of cards remaining in the deck.    |
    | `Discard Pile Size` | 2            | Number of cards in the discard pile.      |
    | `Player Count` | 1            | Number of active players.                 |
    | `Player Info` | Variable     | Array of `Player` structures. Each `Player` structure: `Player ID` (1 byte), `Cards in Hand` (1 byte). |

### 5. `PLAYER_HAND_UPDATE` (Type: `0x11`)

*   **Description**: Sent by the server to a specific client to update their hand.
*   **Payload**:
    | Field    | Size (Bytes) | Description                               |
    | :------- | :----------- | :---------------------------------------- |
    | `Card Count` | 1            | Number of cards in the player's hand.     |
    | `Card IDs` | Variable     | Array of `Card ID` (1 byte each).         |

## Error Codes

*   `0x00`: Success
*   `0xF0`: Invalid Message Type
*   `0xF1`: Invalid Payload Length
*   `0xF2`: Invalid Game State (e.g., action not allowed now)
*   `0xF3`: Player Not Found
*   `0xF4`: Card Not Found / Not in Hand
