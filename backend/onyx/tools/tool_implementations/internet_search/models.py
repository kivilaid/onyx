from pydantic import BaseModel


class InternetSearchResult(BaseModel):
    title: str
    url: str
    published_date: str
    author: str | None
    score: float | None
    full_content: str
    summary: str


class InternetSearchResponse(BaseModel):
    revised_query: str
    internet_results: list[InternetSearchResult]
