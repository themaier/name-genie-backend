# Integration Guide for Your Existing Frontend

## Backend API Base URL

```javascript
const API_URL = "http://localhost:8000/api";
```

## 1. Generate Keywords (Main Feature)

### JavaScript Example

```javascript
async function generateKeywords(topic, creativity = "high", useSearch = true) {
  try {
    const response = await fetch(`${API_URL}/generate-keywords`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        topic_description: topic,
        use_search: useSearch,
        creativity_level: creativity,
      }),
    });

    const data = await response.json();

    if (data.success) {
      console.log("AI Keywords:", data.keywords);
      console.log("Creative Suggestions:", data.creative_suggestions);
      return data;
    } else {
      console.error("Error:", data.error);
      return null;
    }
  } catch (error) {
    console.error("Network error:", error);
    return null;
  }
}

// Usage
const result = await generateKeywords(
  "A modern AI productivity app for remote teams",
  "high",
  true
);
```

### React Example

```jsx
import { useState } from "react";

function KeywordGenerator() {
  const [topic, setTopic] = useState("");
  const [keywords, setKeywords] = useState(null);
  const [loading, setLoading] = useState(false);
  const [creativity, setCreativity] = useState("high");
  const [useSearch, setUseSearch] = useState(true);

  const generateKeywords = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://localhost:8000/api/generate-keywords",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            topic_description: topic,
            use_search: useSearch,
            creativity_level: creativity,
          }),
        }
      );

      const data = await response.json();

      if (data.success) {
        setKeywords(data);
      }
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <textarea
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Describe your topic..."
      />

      <select
        value={creativity}
        onChange={(e) => setCreativity(e.target.value)}
      >
        <option value="low">Low Creativity</option>
        <option value="medium">Medium Creativity</option>
        <option value="high">High Creativity</option>
      </select>

      <label>
        <input
          type="checkbox"
          checked={useSearch}
          onChange={(e) => setUseSearch(e.target.checked)}
        />
        Enable Web Search
      </label>

      <button onClick={generateKeywords} disabled={loading}>
        {loading ? "Generating..." : "Generate Keywords"}
      </button>

      {keywords && (
        <div>
          <h3>AI Keywords:</h3>
          <p>{keywords.keywords}</p>

          <h3>Creative Suggestions:</h3>
          {keywords.creative_suggestions && (
            <div>
              <h4>Variations:</h4>
              <ul>
                {keywords.creative_suggestions.variations?.map((word, i) => (
                  <li key={i}>{word}</li>
                ))}
              </ul>

              <h4>Combinations:</h4>
              <ul>
                {keywords.creative_suggestions.combinations?.map((word, i) => (
                  <li key={i}>{word}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
```

### Vue.js Example

```vue
<template>
  <div>
    <textarea v-model="topic" placeholder="Describe your topic..." />

    <select v-model="creativity">
      <option value="low">Low Creativity</option>
      <option value="medium">Medium Creativity</option>
      <option value="high">High Creativity</option>
    </select>

    <label>
      <input type="checkbox" v-model="useSearch" />
      Enable Web Search
    </label>

    <button @click="generateKeywords" :disabled="loading">
      {{ loading ? "Generating..." : "Generate Keywords" }}
    </button>

    <div v-if="keywords">
      <h3>AI Keywords:</h3>
      <p>{{ keywords.keywords }}</p>

      <h3>Creative Suggestions:</h3>
      <div v-if="keywords.creative_suggestions">
        <h4>Variations:</h4>
        <ul>
          <li
            v-for="(word, i) in keywords.creative_suggestions.variations"
            :key="i"
          >
            {{ word }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      topic: "",
      keywords: null,
      loading: false,
      creativity: "high",
      useSearch: true,
    };
  },
  methods: {
    async generateKeywords() {
      this.loading = true;

      try {
        const response = await fetch(
          "http://localhost:8000/api/generate-keywords",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              topic_description: this.topic,
              use_search: this.useSearch,
              creativity_level: this.creativity,
            }),
          }
        );

        const data = await response.json();

        if (data.success) {
          this.keywords = data;
        }
      } catch (error) {
        console.error("Error:", error);
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
```

## 2. Quick Creative Suggestions (No AI, Instant)

```javascript
async function getQuickSuggestions(topic) {
  try {
    const response = await fetch(`${API_URL}/creative-suggestions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        topic: topic,
        count: 20,
      }),
    });

    const data = await response.json();

    if (data.success) {
      return data.suggestions;
    }
  } catch (error) {
    console.error("Error:", error);
    return null;
  }
}

// Usage
const suggestions = await getQuickSuggestions("cloud storage");
console.log(suggestions.variations); // ["CloudStorage", "StorageHub", ...]
console.log(suggestions.combinations); // ["CloudStore", "DataCloud", ...]
console.log(suggestions.blends); // ["Clourage", "Stocloud", ...]
```

## 3. Using with Prompt Window + Buttons

If you have buttons that select/unselect parts of the prompt:

```javascript
// Your button state
const [selectedOptions, setSelectedOptions] = useState({
  creative: false,
  formal: false,
  detailed: false,
});

// When generating keywords
async function generateWithOptions() {
  // Determine creativity level based on selected options
  let creativity = "medium";
  if (selectedOptions.creative) creativity = "high";
  if (selectedOptions.formal) creativity = "low";

  const result = await fetch("http://localhost:8000/api/generate-keywords", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      topic_description: topic,
      use_search: selectedOptions.detailed, // Use search for detailed results
      creativity_level: creativity,
    }),
  });

  const data = await result.json();
  return data;
}
```

## 4. Full Integration Example (HTML/JS)

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Keyword Generator</title>
  </head>
  <body>
    <div id="app">
      <!-- Topic Input -->
      <textarea id="topic" placeholder="Describe your topic..."></textarea>

      <!-- Option Buttons -->
      <div class="options">
        <button class="option-btn" data-option="creative">Creative</button>
        <button class="option-btn" data-option="formal">Formal</button>
        <button class="option-btn" data-option="detailed">Detailed</button>
      </div>

      <!-- Generate Button -->
      <button id="generate">Generate Keywords</button>

      <!-- Results -->
      <div id="results"></div>
    </div>

    <script>
      const API_URL = "http://localhost:8000/api";
      const selectedOptions = new Set();

      // Handle option buttons
      document.querySelectorAll(".option-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
          const option = btn.dataset.option;
          if (selectedOptions.has(option)) {
            selectedOptions.delete(option);
            btn.classList.remove("active");
          } else {
            selectedOptions.add(option);
            btn.classList.add("active");
          }
        });
      });

      // Generate keywords
      document
        .getElementById("generate")
        .addEventListener("click", async () => {
          const topic = document.getElementById("topic").value;

          // Determine creativity based on selected options
          let creativity = "medium";
          if (selectedOptions.has("creative")) creativity = "high";
          if (selectedOptions.has("formal")) creativity = "low";

          try {
            const response = await fetch(`${API_URL}/generate-keywords`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                topic_description: topic,
                use_search: selectedOptions.has("detailed"),
                creativity_level: creativity,
              }),
            });

            const data = await response.json();

            if (data.success) {
              displayResults(data);
            }
          } catch (error) {
            console.error("Error:", error);
          }
        });

      function displayResults(data) {
        const resultsDiv = document.getElementById("results");

        let html = `
        <h3>AI Keywords:</h3>
        <p>${data.keywords}</p>
      `;

        if (data.creative_suggestions) {
          html += "<h3>Creative Suggestions:</h3>";

          for (const [category, words] of Object.entries(
            data.creative_suggestions
          )) {
            html += `<h4>${category}:</h4>`;
            html += "<ul>";
            words.forEach((word) => {
              html += `<li>${word}</li>`;
            });
            html += "</ul>";
          }
        }

        resultsDiv.innerHTML = html;
      }
    </script>
  </body>
</html>
```

## 5. CORS Configuration

The backend is already configured to accept requests from localhost:3000 and localhost:3001.

If your frontend runs on a different port, update `main.py`:

```python
# In main.py, add your frontend URL
allow_origins=[
    "http://localhost:3000",   # Default
    "http://localhost:3001",
    "http://localhost:5173",   # Add your port here
    # ... or your production URL
]
```

## 6. Response Structure

### Generate Keywords Response

```typescript
interface KeywordResponse {
  success: boolean;
  keywords: string; // AI-generated keywords
  creative_suggestions: {
    variations: string[]; // Word variations
    combinations: string[]; // Word combinations
    styled: string[]; // Styled words
    acronyms: string[]; // Generated acronyms
    blends: string[]; // Blended words
  };
  topic: string;
  creativity_level: string;
  search_enabled: boolean;
}
```

### Creative Suggestions Response

```typescript
interface CreativityResponse {
  success: boolean;
  suggestions: {
    variations: string[];
    combinations: string[];
    styled: string[];
    acronyms: string[];
    blends: string[];
  };
}
```

## 7. Error Handling

```javascript
try {
  const response = await fetch(`${API_URL}/generate-keywords`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(requestData),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.detail || "Server error");
  }

  if (!data.success) {
    throw new Error(data.error || "Generation failed");
  }

  // Success!
  handleResults(data);
} catch (error) {
  if (error.message.includes("fetch")) {
    alert("Cannot connect to server. Is it running?");
  } else {
    alert(`Error: ${error.message}`);
  }
}
```

## 8. TypeScript Types

```typescript
// Request types
interface KeywordRequest {
  topic_description: string;
  use_search?: boolean;
  creativity_level?: "low" | "medium" | "high";
}

interface CreativityRequest {
  topic: string;
  count?: number;
}

// Response types
interface KeywordResponse {
  success: boolean;
  keywords?: string;
  creative_suggestions?: {
    variations: string[];
    combinations: string[];
    styled: string[];
    acronyms: string[];
    blends: string[];
  };
  topic?: string;
  creativity_level?: string;
  search_enabled?: boolean;
  error?: string;
}

interface CreativityResponse {
  success: boolean;
  suggestions?: {
    variations: string[];
    combinations: string[];
    styled: string[];
    acronyms: string[];
    blends: string[];
  };
  error?: string;
}
```

## Ready to Integrate! 🚀

The backend API is ready to work with any frontend framework. Just make sure:

1. Backend is running: `python main.py`
2. API is accessible at `http://localhost:8000`
3. CORS allows your frontend URL
