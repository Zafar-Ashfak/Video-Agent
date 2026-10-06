<h1>Summify AI – AI-powered video and meeting summarizer</h1>
<br />

<p> <strong>Summify AI</strong> is an AI-powered video and meeting summarization application that takes a <strong>YouTube or meeting video link</strong> as input and transforms the video into structured and actionable information. The application extracts the audio, converts speech into text using <strong>Whisper</strong> or <strong>Sarvam AI</strong>, and uses <strong>Llama 3.2</strong> with LangChain to generate a concise summary, meeting title, action items, key decisions, and open questions. It also provides a <strong>RAG-powered chat</strong> that allows users to ask questions directly about the video content and receive answers based on the generated transcript. The application supports both <strong>English and Hinglish</strong> conversations through a clean and interactive Streamlit interface. </p>

<br />

<h2>Features</h2>

<ul>
<li>YouTube video and Meeting video support</li>
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
                                    │  YouTube / Meeting   │
                                    │        Video         │
                                    └──────────┬───────────┘
                                               │
                                               ▼
                                    ┌──────────────────────┐
                                    │   Audio Processing   │
                                    │    yt-dlp + Pydub    │
                                    │  16kHz Mono + Chunks │
                                    └──────────┬───────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    ▼                     ▼
                             ┌──────────────┐      ┌──────────────┐
                             │    English   │      │   Hinglish   │
                             │    Whisper   │      │   Sarvam AI  │
                             └──────┬───────┘      └──────┬───────┘
                                    └──────────┬──────────┘
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
                                    │      Vector Store +  │
                                    │      Retriever + LLM │
                                    └──────────┬───────────┘
                                               │
                                               ▼
                                    ┌──────────────────────┐
                                    │  Chat with Meeting   │
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