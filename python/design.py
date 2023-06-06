import os

from qdrant_client import QdrantClient
from qdrant_client.http import models


QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
QDRANT_HOST = os.getenv("QDRANT_HOST")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

client = QdrantClient(
    url="https://bceadf6b-a95a-42cc-9053-32a6bce439fa.us-east-1-0.aws.cloud.qdrant.io:6333",
    api_key="yd09n92c2R6c3HuhoVFxHm17wyRX3V_Wje2sfm-iF1FpHNS8AgvGxw")

#
#
#
client.recreate_collection(
    collection_name="{iching}",
    vectors_config=models.VectorParams(size=100, distance=models.Distance.COSINE),
)
#
#
#
from qdrant_client import QdrantClient
from qdrant_client.http import models

#client = QdrantClient("localhost", port=6333)

#
#
#
client.upsert(
    collection_name="{iching}",
    points=models.Batch(
        ids=[1, 2, 3],
        payloads=[
            {"color": "red"},
            {"color": "green"},
            {"color": "blue"},
        ],
        vectors=[
            [0.9, 0.1, 0.1],
            [0.1, 0.9, 0.1],
            [0.1, 0.1, 0.9],
        ]
    ),
)