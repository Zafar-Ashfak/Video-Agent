<h1>AI Video Assistant – Meeting Intelligence</h1>
<br />

<p>
AI Video Assistant is an AI-powered meeting intelligence tool designed to transform meeting recordings into useful and actionable information. It supports <strong>YouTube videos</strong> and <strong>local audio/video files</strong>, converts speech into text, generates professional summaries, extracts <strong>action items</strong>, <strong>key decisions</strong>, and <strong>open questions</strong>. It also includes a <strong>RAG-powered chat</strong> that allows users to ask questions directly from the meeting transcript. The application supports both <strong>English and Hinglish</strong> conversations with a clean Streamlit interface and dark/light mode.
</p>

<br />

<h2>Features</h2>

<ul>
<li>YouTube video and local audio/video support</li>
<li>Speech-to-text transcription using Whisper</li>
<li>Hinglish transcription and translation using Sarvam AI</li>
<li>Automatic meeting title generation</li>
<li>AI-powered meeting summarization</li>
<li>Action item extraction with owner and deadline</li>
<li>Key decision extraction</li>
<li>Open question and follow-up extraction</li>
<li>RAG-based question answering from meeting transcripts</li>
<li>Chat with your meeting using an AI assistant</li>
<li>English and Hinglish language support</li>
<li>Dark and Light mode</li>
<li>Modern Streamlit user interface</li>
</ul>

<br />

<h2>Workflow</h2>

                    ┌──────────────────────┐
                    │  YouTube / Local     │
                    │  Audio / Video       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Audio Processing   │
                    │ yt-dlp + Pydub       │
                    │ 16kHz Mono + Chunks  │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌──────────────┐      ┌──────────────┐
             │    English   │      │   Hinglish   │
             │   Whisper    │      │  Sarvam AI   │
             └──────┬───────┘      └──────┬───────┘
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │  Meeting Transcript  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Llama 3.2 +        │
                    │      LangChain       │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        ┌──────────┐     ┌──────────┐     ┌────────────┐
        │ Summary  │     │ Actions  │     │ Decisions  │
        └──────────┘     └──────────┘     └────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      RAG Pipeline    │
                    │ Vector Store +       │
                    │ Retriever + LLM      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Chat with Meeting │
                    └──────────────────────┘

<br />

<h2>How It Works</h2>

<p>
The user provides a YouTube URL or local media file and selects the preferred language. The system downloads or processes the audio, converts it into a 16kHz mono WAV file, and splits it into manageable chunks. The chunks are then transcribed using <strong>Whisper</strong> for English or <strong>Sarvam AI</strong> for Hinglish.
</p>

<p>
The generated transcript is processed by <strong>Llama 3.2</strong> through LangChain to generate a meeting title, summary, action items, key decisions, and open questions. The transcript is also passed through a <strong>RAG pipeline</strong>, allowing users to ask questions and receive answers based only on the meeting content.
</p>

<br />

<h2>Project Screenshot</h2>

<img src="./src/assets/Video_Agent.png" width="100%" />

<br />

<h2>Tech Stack</h2>

<strong>Language:</strong> Python
<br/>
<strong>AI Framework:</strong> LangChain
<br/>
<strong>LLM:</strong> Ollama – Llama 3.2 3B
<br/>
<strong>Speech-to-Text:</strong> OpenAI Whisper
<br/>
<strong>Hinglish Transcription:</strong> Sarvam AI
<br/>
<strong>RAG:</strong> LangChain + Vector Store
<br/>
<strong>Audio Processing:</strong> Pydub
<br/>
<strong>YouTube Processing:</strong> yt-dlp
<br/>
<strong>Frontend:</strong> Streamlit
<br/>
<strong>Environment Management:</strong> python-dotenv
<br/>
<strong>Tools & Platforms:</strong> Git, GitHub, VS Code

<br />