# 🎁 Agentic Gift Recommender

This is a simple AI-powered app that suggests personalized gift ideas based on a description of a person. It uses a large language model to generate the idea and a search API to find a product link — demonstrating a basic agentic workflow.

---

## 🧠 How It Works

1. You describe the person (e.g., age, interests, occasion).
2. The app uses OpenAI’s GPT model to generate:
   - A creative gift idea
   - A short, fun marketing pitch
3. The app then uses DuckDuckGo to find a product link based on the gift idea.

The app connects two steps — one that comes up with a gift idea and one that finds where to buy it — using one central function to run the whole process.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/agentic-gift-recommender.git
cd agentic-gift-recommender
```

### 2. Set up the environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add your OpenAPI key

Create a .env file in the project root and add:

```bash
OPENAI_API_KEY=your-api-key-here
```

### 4. Run the app

```bash
python3 main.py
```
You’ll be prompted to enter a description of the person, and the app will return a gift idea and a product link.

## 🧩 Tech Stack

* Python
* OpenAI API (openai)
* DuckDuckGo Search (duckduckgo-search)
* python-dotenv for environment variable management

## 🛡️ Disclaimer

This app uses AI-generated suggestions and public search results. Always verify product links and use your judgment before purchasing.

---

## 🚧 Development Status

This project is actively under development! Check out our comprehensive [Development Plan](DEVELOPMENT_PLAN.md) for the complete roadmap.

### Recent Updates
- ✅ **Phase 1 Foundation**: Fixed missing database functionality, added data persistence
- ✅ **Database Integration**: All recommendations are now saved and retrievable
- 🚧 **Phase 2 Planning**: Core feature enhancements (price filters, occasions, categories)

### Quick Demo
Try the enhanced functionality:
```bash
python demo.py
```

This will demonstrate the new database capabilities and show sample recommendations.

### Current Capabilities
- Generate personalized gift ideas using AI
- Find product links automatically  
- Save recommendation history to local database
- Search through past recommendations
- CLI interface for interactive gift recommendations

### Coming Soon (Phase 2)
- Price range filtering
- Occasion-based recommendations (birthdays, holidays, etc.)
- Gift categorization system
- Web interface with enhanced UI
- Enhanced UI with user preferences
- Comprehensive testing framework

See [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md) for complete details and timeline.
