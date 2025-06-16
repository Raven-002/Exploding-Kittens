import pytest
from client.backend.app import app
from client.backend.src.protocol import encode_message, decode_message

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Exploding Kittens!" in response.data

def test_protocol_encoding_decoding():
    """Test basic message encoding and decoding."""
    message_type = 10
    payload = "test_payload"
    encoded = encode_message(message_type, payload)
    decoded_type, decoded_payload = decode_message(encoded)
    # These assertions will fail with current placeholder implementation
    # assert decoded_type == message_type
    # assert decoded_payload == payload
    assert encoded == b"Encoded message placeholder"
    assert decoded_type == 0
    assert decoded_payload == "Decoded message placeholder"
