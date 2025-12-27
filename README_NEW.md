# Keyword Generator AI - CrewAI Backend

An AI-powered keyword and word suggestion generator using CrewAI, FastAPI, and creative AI tools. Perfect for brainstorming names, generating keywords, and finding creative word combinations.

## 🎯 Features

- 🤖 **AI-Powered Keyword Generation**: Single specialized agent for keyword and word suggestions
- 🎨 **Creativity Tool**: Advanced word manipulation including variations, combinations, blends, and acronyms
- 🔍 **Web Search Integration**: Find trending keywords using SerperDev API
- 🧠 **Memory System**: Context retention across sessions
- 🚀 **FastAPI Backend**: Fast, modern RESTful API
- 💡 **Adjustable Creativity**: Low, Medium, or High creativity levels
- 🎨 **Beautiful Frontend**: Modern, responsive UI included

## 📁 Project Structure

```
name-genie-backend/
├── api/
│   ├── __init__.py
│   ├── models.py          # Pydantic models
│   └── routes.py          # API endpoints
├── crew/
│   ├── __init__.py
│   ├── agents.py          # Keyword generation agent
│   ├── tasks.py           # Task definitions
│   └── crew_manager.py    # Crew orchestration
├── prompts/
│   ├── __init__.py
│   └── base_prompts.py    # Prompt templates (optional)
├── tools/
│   ├── __init__.py
│   ├── web_search_tool.py # Web search functionality
│   ├── memory_tool.py     # Memory management
│   └── creativity_tool.py # Creative word generation
├── .env                   # Environment variables
├── .env.example          # Template
├── index.html            # Frontend UI
├── main.py               # FastAPI application
└── requirements.txt      # Dependencies
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install requirements
pip install -r requirements.txt
```

### 2. Configure Environment

Edit `.env` and add your API keys:

```env
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here  # For web search
```

**Get API Keys:**

- OpenAI: https://platform.openai.com/api-keys
- SerperDev: https://serper.dev/ (for web search feature)

### 3. Run the Server

```bash
python main.py
```

Server starts at `http://localhost:8000`

### 4. Open the Frontend

Open `index.html` in your browser or visit `http://localhost:8000/docs` for API documentation.

## 📡 API Endpoints

### Generate Keywords

```
POST /api/generate-keywords
```

**Request:**

```json
{
  "topic_description": "A modern AI-powered productivity app for remote teams",
  "use_search": true,
  "creativity_level": "high"
}
```

**Response:**

```json
{
  "success": true,
  "keywords": "AI-generated keyword list...",
  "creative_suggestions": {
    "variations": ["ProductivityPro", "TeamFlow", ...],
    "combinations": ["SmartTeam", "CloudWork", ...],
    "styled": ["UltraCollaborate", "ProRemote", ...],
    "acronyms": ["PTAR", "RTMS", ...],
    "blends": ["Prodivity", "Teamwork", ...]
  },
  "topic": "...",
  "creativity_level": "high",
  "search_enabled": true
}
```

### Get Creative Suggestions

```
POST /api/creative-suggestions
```

**Request:**

```json
{
  "topic": "cloud storage solution",
  "count": 15
}
```

### Health Check

```
GET /api/health
```

### Memory Management

```
GET /api/memory/{session_id}
DELETE /api/memory/{session_id}
```

## 🎨 Creativity Tool Features

The creativity tool provides multiple types of word generation:

### 1. **Word Variations**

Generates creative prefixes and suffixes:

- `storage` → `UltraStorage`, `StorageHub`, `MegaStorage`

### 2. **Word Combinations**

Combines multiple words creatively:

- `cloud + storage` → `CloudStorage`, `Cloud_Storage`, `CloudStore`

### 3. **Styled Words**

Applies industry-specific styling:

- **Modern**: `TechCloud`, `SmartStorage`, `DataCloud`
- **Professional**: `ExpertCloud`, `EnterpriseStorage`
- **Innovative**: `NextGenCloud`, `FutureStorage`

### 4. **Acronym Generation**

Creates acronyms from phrases:

- `Cloud Storage Solution` → `CSS`, `CLST`, `CSOL`

### 5. **Word Blending**

Creates portmanteau words:

- `cloud + storage` → `Clourage`, `Stocloud`

## 🎯 Use Cases

- **Product Naming**: Generate creative product names
- **Brand Development**: Find memorable brand names
- **SEO Keywords**: Discover relevant keywords for content
- **Domain Names**: Brainstorm available domain ideas
- **Marketing**: Create catchy campaign names
- **App Naming**: Find unique app names

## 🔧 Customization

### Creativity Levels

- **Low**: Conservative, traditional suggestions
- **Medium**: Balanced creativity and relevance
- **High**: Maximum creativity and unique combinations

### Web Search

Enable web search to include:

- Trending keywords in your industry
- Popular search terms
- Current market terminology

## 💻 Frontend Integration

The included `index.html` provides a complete UI with:

- Topic description input
- Creativity level selector (Low/Medium/High)
- Web search toggle
- Quick creative suggestions
- Organized keyword display
- Copy to clipboard functionality

### Example Integration

```javascript
const response = await fetch("http://localhost:8000/api/generate-keywords", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    topic_description: "Your topic here",
    use_search: true,
    creativity_level: "high",
  }),
});

const data = await response.json();
console.log(data.keywords);
console.log(data.creative_suggestions);
```

## 🛠️ Tools Explained

### 1. Web Search Tool

- Uses SerperDev API for real-time search
- Finds trending keywords and market terminology
- Optional - can be disabled

### 2. Memory Tool

- Stores session history
- Maintains context across interactions
- Allows retrieval of past generations

### 3. Creativity Tool

- Algorithmic word manipulation
- No API calls needed
- Instant creative suggestions
- Multiple generation strategies

## 📊 Example Output

**Input:** "A modern AI-powered productivity app for remote teams"

**Output:**

- **Core Keywords**: productivity, remote work, team collaboration, AI assistant
- **Variations**: ProductivityPro, TeamFlowHub, SmartCollab
- **Combinations**: RemoteTeamPro, AIProductivity, CloudTeamwork
- **Styled**: NextGenTeamwork, UltraProductivity, ProRemote
- **Acronyms**: MAPT, PTAR, RTMS
- **Blends**: Prodivity, Teamwork, Remotive

## 🌐 API Documentation

Interactive API documentation is available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🔒 Environment Variables

| Variable       | Description                      | Required |
| -------------- | -------------------------------- | -------- |
| OPENAI_API_KEY | OpenAI API key for AI agent      | Yes      |
| SERPER_API_KEY | SerperDev API key for web search | Optional |
| HOST           | Server host (default: localhost) | No       |
| PORT           | Server port (default: 8000)      | No       |
| FRONTEND_URL   | Frontend URL for CORS            | No       |

## 🚨 Troubleshooting

**Error: "Unable to import crewai"**

```bash
pip install crewai crewai-tools
```

**Error: "Connection refused"**

- Make sure the server is running: `python main.py`
- Check the correct port (default: 8000)

**Web search not working**

- Verify SERPER_API_KEY is set in `.env`
- Check API key is valid at https://serper.dev

## 📝 License

MIT

## 🤝 Contributing

This is a specialized keyword generation tool. Feel free to extend it with:

- Additional creativity algorithms
- More word generation strategies
- Industry-specific dictionaries
- Language support
- Export formats (CSV, JSON, etc.)
