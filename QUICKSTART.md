# 🚀 Quick Start Guide - Keyword Generator AI

## Step 1: Install Python Packages

```bash
pip install -r requirements.txt
```

This will install:

- fastapi
- uvicorn
- crewai
- crewai-tools
- langchain-openai
- pydantic
- python-dotenv

## Step 2: Set Up API Keys

1. **Copy the environment template:**

   ```bash
   copy .env.example .env
   ```

2. **Get your OpenAI API key:**

   - Go to https://platform.openai.com/api-keys
   - Create a new API key
   - Copy it

3. **Get your Serper API key (optional but recommended):**

   - Go to https://serper.dev/
   - Sign up for free
   - Get your API key

4. **Edit `.env` file and add your keys:**
   ```env
   OPENAI_API_KEY=sk-your-actual-key-here
   SERPER_API_KEY=your-serper-key-here
   ```

## Step 3: Test Your Setup

```bash
python test_setup.py
```

This will verify:

- ✅ All packages are installed
- ✅ API keys are configured
- ✅ Tools are working

## Step 4: Start the Server

```bash
python main.py
```

You should see:

```
Starting server at http://localhost:8000
API documentation available at http://localhost:8000/docs
```

## Step 5: Use the App

### Option A: Use the Web Interface

1. Open `index.html` in your browser
2. Enter your topic description
3. Adjust creativity level
4. Click "Generate Keywords"

### Option B: Use the API

Visit: http://localhost:8000/docs

Try the `/api/generate-keywords` endpoint with:

```json
{
  "topic_description": "A modern AI-powered productivity app",
  "use_search": true,
  "creativity_level": "high"
}
```

## Example Usage

**Input:**

```
A modern AI-powered productivity app for remote teams
```

**Settings:**

- Creativity: High
- Web Search: Enabled

**Output:**

- Core keywords
- Creative variations
- Word combinations
- Acronyms
- Blended words
- Trending keywords (from web search)

## Troubleshooting

### "Module not found" errors

```bash
pip install -r requirements.txt
```

### "Invalid API key" errors

- Check your `.env` file
- Make sure OPENAI_API_KEY is set correctly
- No spaces around the `=` sign

### Server won't start

- Make sure port 8000 is not in use
- Check if another Python process is running
- Try: `python main.py`

### Web search not working

- SERPER_API_KEY might not be set
- This is optional - keywords will still generate
- Get a free key at https://serper.dev/

## Next Steps

1. **Customize creativity levels** in `crew/crew_manager.py`
2. **Add more word patterns** in `tools/creativity_tool.py`
3. **Modify the frontend** in `index.html`
4. **Integrate with your existing app** using the API

## Support

- Check `README.md` for detailed documentation
- Visit http://localhost:8000/docs for API reference
- Run `python test_setup.py` to diagnose issues

---

**Ready to generate keywords!** 🎯
