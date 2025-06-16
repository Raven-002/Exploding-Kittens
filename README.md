# Exploding Kittens

## About The Game
Exploding Kittens is a card game that combines strategy, luck, and a bit of humor. The goal is to avoid drawing an Exploding Kitten card, which eliminates you from the game. Players take turns drawing cards from a deck, using various action cards to manipulate the game state. The game ends when only one player remains, who is declared the winner.

## Components

### GameServer
A server, written in C, that manages the game state, handles player connections and actions, and ensures the game rules are followed. It uses structs to represent players, cards, the game state, and actions taken by players.

### GameClient
A client, written in Python, that allows players to connect to the GameServer, view their hand of cards, and perform actions such as drawing cards or playing action cards. It communicates with the server using a simple binary protocol.

The GameClient will consists of a python backend providing web frontend with a simple UI to interact with the game. The UI will allow players to see their cards, take actions, and view the game state.
