const BACKEND_URL = "http://localhost:8000";

const urlEl = document.getElementById("url");
const loadBtn = document.getElementById("loadBtn");
const questionEl = document.getElementById("question");
const askBtn = document.getElementById("askBtn");
const statusEl = document.getElementById("status");
const answerEl = document.getElementById("answer");

let currentUrl = "";

function setStatus(message) {
  statusEl.textContent = message;
}

function showAnswer(text) {
  answerEl.textContent = text;
  answerEl.hidden = false;
}

async function getCurrentTabUrl() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  return tab ? tab.url : "";
}

async function loadPage() {
  loadBtn.disabled = true;
  setStatus("Loading page into the vector store…");

  try {
    const response = await fetch(`${BACKEND_URL}/ingest`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url: currentUrl }),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || `Request failed (${response.status})`);
    }

    const data = await response.json();
    setStatus(`Loaded ${data.chunks} chunks. Ask a question below.`);
  } catch (error) {
    setStatus(`Error: ${error.message}`);
  } finally {
    loadBtn.disabled = false;
  }
}

async function askQuestion() {
  const question = questionEl.value.trim();

  if (!question) {
    setStatus("Type a question first.");

    return;
  }

  askBtn.disabled = true;
  answerEl.hidden = true;
  setStatus("Thinking…");

  try {
    const response = await fetch(`${BACKEND_URL}/query?q=${encodeURIComponent(question)}`);

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.detail || `Request failed (${response.status})`);
    }

    const data = await response.json();
    setStatus("");
    showAnswer(data.answer);
  } catch (error) {
    setStatus(`Error: ${error.message}`);
  } finally {
    askBtn.disabled = false;
  }
}

async function init() {
  currentUrl = await getCurrentTabUrl();
  urlEl.textContent = currentUrl || "No active tab";
}

loadBtn.addEventListener("click", loadPage);
askBtn.addEventListener("click", askQuestion);
init();
