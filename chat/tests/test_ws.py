from channels.testing import WebsocketCommunicator

from chat.consumers import ChatConsumer

import pytest
import json


@pytest.mark.asyncio
async def test_websocket_consumer():
    communicator = WebsocketCommunicator(ChatConsumer, "/ws/chat/testws/")
    connected, subprotocol = await communicator.connect()
    assert connected
    # Test sending text
    testData = {'message': 'hello'}
    await communicator.send_to(text_data=json.dumps(testData))
    response = await communicator.receive_from()
    assert json.loads(response) == testData
    # Close
    await communicator.disconnect()
