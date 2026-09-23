import os
import time
from google import genai

from config import CATEGORIES

_client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY", ""))


def _detect_category(title: str, description: str) -> str:
    text = (title + " " + description).lower()
    for category, keywords in CATEGORIES.items():
        if any(kw.lower() in text for kw in keywords):
            return category
    return "General Tech"


def _call_gemini(prompt: str) -> str:
    response = _client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    # Rate limiting buffer for free tier
    time.sleep(5)
    text = response.text.strip()
    print(f"Gemini raw response: {text}", flush=True)
    return text


def summarize(article: dict) -> tuple:
    errors = []
    title = article.get("title", "")
    description = article.get("description", "")

    prompt = (
        "You are an executive technical editor summarizing news for engineering leads, system architects, and tech managers.\n"
        "Given the article below, provide a crisp 3-4 sentence summary covering: "
        "(1) What was announced/released, (2) How it works technically or structurally, and (3) Why it matters for engineering/product strategy.\n\n"
        "Respond in EXACTLY this format with no extra text or markdown headers:\n"
        "SUMMARY: <3-4 sentence technical summary>\n"
        "TAGS: <3-5 comma-separated tags>\n\n"
        f"Title: {title}\n"
        f"Content: {description[:1200]}"
    )

    summary = "Summary unavailable"
    tags = []

    try:
        text = _call_gemini(prompt)
        summary, tags = _parse_response(text)
    except Exception as e1:
        print(f"Gemini error (attempt 1): {str(e1)}", flush=True)
        try:
            time.sleep(15)
            text = _call_gemini(prompt)
            summary, tags = _parse_response(text)
        except Exception as e2:
            print(f"Gemini error (attempt 2): {str(e2)}", flush=True)
            errors.append(f"Summarization failed for '{title}': {str(e2)}")

    article["summary"] = summary
    article["tags"] = tags
    article["field"] = _detect_category(title, description)

    return article, errors


def _parse_response(text: str) -> tuple:
    summary = "Summary unavailable"
    tags = []

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        elif line.startswith("TAGS:"):
            raw_tags = line.replace("TAGS:", "").strip()
            tags = [t.strip() for t in raw_tags.split(",") if t.strip()]

    return summary, tags
