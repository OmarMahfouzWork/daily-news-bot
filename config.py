INTEREST_KEYWORDS = [
    # System Architecture & Leadership
    "system design",
    "architecture",
    "microservices",
    "high availability",
    "scalability",
    "distributed systems",
    "engineering management",
    "tech leadership",
    # Project Management
    "project management",
    "agile",
    "scrum",
    "product management",
    "tech debt",
    "roadmap",
    # AI & Agentic Systems
    "agentic",
    "ai agent",
    "rag",
    "nlp",
    "langchain",
    "llamaindex",
    "automation",
    # LLM & New Models
    "llm",
    "large language model",
    "transformer",
    "fine-tuning",
    "open weights",
    "embeddings",
    # VR & Game Dev
    "vr",
    "virtual reality",
    "spatial computing",
    "unity",
    "unreal engine",
    "game dev",
    "hand tracking",
    "openxr",
]

CATEGORIES = {
    "System Architecture & Leadership": [
        "architecture",
        "system design",
        "microservices",
        "distributed",
        "scalability",
        "infrastructure",
        "high availability",
        "engineering management",
        "tech leadership",
    ],
    "Project Management": [
        "project management",
        "agile",
        "scrum",
        "product management",
        "roadmap",
        "tech debt",
        "sprint",
        "kanban",
    ],
    "AI & Agentic Systems": [
        "agentic",
        "ai agent",
        "autonomous agent",
        "rag",
        "langchain",
        "llamaindex",
        "workflow",
        "nlp",
        "ocr",
        "vector database",
    ],
    "LLM & Models": [
        "llm",
        "large language model",
        "transformer",
        "fine-tuning",
        "gpt",
        "claude",
        "gemini",
        "llama",
        "open weights",
        "model release",
        "embeddings",
    ],
    "VR & Game Dev": [
        "vr",
        "virtual reality",
        "ar",
        "augmented reality",
        "spatial computing",
        "unity",
        "unreal engine",
        "game dev",
        "hand tracking",
        "openxr",
        "quest",
        "3d graphics",
    ],
    "General Tech": [],  # fallback
}

# Note: Removed "gaming" from blacklist so VR and Game Dev feeds don't get filtered out.
BLACKLIST_KEYWORDS = [
    "celebrity",
    "sports",
    "entertainment",
    "politics",
    "election",
    "movie",
    "tv show",
    "crypto",
    "nft",
]

RSS_SOURCES = {
    # System Architecture & Leadership
    "ByteByteGo": "https://blog.bytebytego.com/feed",
    "Pragmatic Engineer": "https://newsletter.pragmaticengineer.com/feed",
    # Project Management
    "Mind the Product": "https://www.mindtheproduct.com/feed/",
    # AI & Agentic Systems
    "LangChain Blog": "https://blog.langchain.dev/rss/",
    "LlamaIndex Blog": "https://www.llamaindex.ai/blog/rss.xml",
    # LLM & New Models
    "Hugging Face Blog": "https://huggingface.co/blog/feed.xml",
    "OpenAI News": "https://openai.com/news/rss.xml",
    # VR & Game Dev
    "UploadVR": "https://uploadvr.com/feed/",
    "Road to VR": "https://www.roadtovr.com/feed/",
    "Unity Blog": "https://blog.unity.com/feed",
}

HN_KEYWORDS = [
    "architecture",
    "system design",
    "LLM",
    "agent",
    "RAG",
    "VR",
    "Unity",
    "spatial computing",
    "game dev",
]

SIMILARITY_THRESHOLD = 0.75

MAX_ARTICLES_PER_RUN = 15
