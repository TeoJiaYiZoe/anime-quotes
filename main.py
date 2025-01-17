from fastapi import FastAPI, Query, status, HTTPException
import random
from typing import List, Optional
from mangum import Mangum
from quotes import quotes  # Import the quotes
import re

app = FastAPI()


def normalize_string(value: str) -> str:
    """Normalize a string by converting to lowercase and removing non-alphanumeric characters."""
    return re.sub(r"[^a-zA-Z0-9\s]", "", value).lower().strip()


@app.get("/random-quote")
def get_random_quote():
    """Return a random quote."""
    return random.choice(quotes)


@app.get("/quotes-by-anime/{anime}", status_code=status.HTTP_200_OK)
def get_quotes_by_anime(anime: str):
    """Return all quotes from a specific anime."""
    anime_normalized = normalize_string(anime)
    results = [
        quote
        for quote in quotes
        if anime_normalized == normalize_string(quote.get("anime", ""))
    ]
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No quotes found for anime '{anime}'"
        )
    return results


@app.get("/available-anime", status_code=status.HTTP_200_OK)
def get_available_animes():
    """Return a list of all animes."""
    animes = set(quote.get("anime", "") for quote in quotes)
    return {"animes": sorted(animes)}


@app.get("/quotes-by-tag/{tag}", status_code=status.HTTP_200_OK)
def get_quotes_by_tag(tag: str):
    """Return all quotes with a specific tag."""
    tag_normalized = normalize_string(tag)
    results = [
        quote
        for quote in quotes
        if any(tag_normalized == normalize_string(t) for t in quote.get("tags", []))
    ]
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No quotes found for tag '{tag}'"
        )
    return results


@app.get("/available-tags", status_code=status.HTTP_200_OK)
def get_available_tags():
    """Return a list of all tags."""
    tags = set(tag for quote in quotes for tag in quote.get("tags", []))
    return {"tags": sorted(tags)}


@app.get("/search-quotes/{anime}/{tag}", status_code=status.HTTP_200_OK)
def search_quotes(
    anime: Optional[str] = None,
    tag: Optional[str] = None,
):
    """
    Search quotes by multiple parameters: anime and tag.
    At least one parameter is required.
    """
    if not (anime or tag):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one search parameter (anime, tag) is required."
        )

    results = quotes
    if tag:
        tag_normalized = normalize_string(tag)
        results = [
            quote
            for quote in results
            if any(tag_normalized == normalize_string(t) for t in quote.get("tags", []))
        ]
    if anime:
        anime_normalized = normalize_string(anime)
        results = [
            quote
            for quote in results
            if anime_normalized == normalize_string(quote.get("anime", ""))
        ]

    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No quotes found matching the criteria."
        )
    return results


# Wrap the app with Mangum for AWS Lambda
handler = Mangum(app)