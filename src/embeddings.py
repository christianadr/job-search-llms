from typing import List

import requests
from openai import OpenAI

client = OpenAI()


def get_embeddings(text: str, model: str = "text-embedding-ada-002") -> List[float]:
    """Creates vector embeddings of given text

    Parameters
    ----------
    text : str
        Text to convert into embeddings
    model : str, optional
        Model available from OpenAI to use for embedding,
        by default "text-embedding-ada-002"

    Returns
    -------
    List[float]
        List of floats representing the embedding vector
    """

    text = text.replace("\n", " ")

    return (
        client.embeddings.create(
            input=[text],
            model=model,
        )
        .data[0]
        .embedding
    )
