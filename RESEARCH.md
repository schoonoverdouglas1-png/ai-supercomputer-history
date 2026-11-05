# Research — Google AI lineage, open source vs API-only, and supercomputers

Provenance: Recreated by Ember, Nov 5, 2026, from Meta AI's description as brought by Douglas. Labels: [D] = documented, as generally recorded; [GAP] = needs a source check before use as a citation. This is a starter, not a finished citation file.

## 1. Google AI project lineage [D, in outline]
- **2011 — Google Brain:** Google's deep-learning research project, founded 2011.
- **2015 — TensorFlow open source:** TensorFlow released as open source in November 2015.
- **2017 — Transformer:** "Attention Is All You Need," June 2017 — the Transformer architecture that underlies modern large models.
- **2021 — LaMDA:** Google's Language Model for Dialogue Applications, announced 2021.
- **2022 — PaLM:** Pathways Language Model, announced April 2022.
- **2023 — Gemini:** Google's multimodal model family, announced December 2023, succeeding PaLM / Bard-era work.
- **2024 — Gemma:** Google's open-weights model family, released February 2024.
- **2025 — Gemini CLI:** Google's command-line Gemini tool, released June 2025.

## 2. What's actually open source vs API-only
- **Open source / open weights [D]:**
  - TensorFlow — open source
  - JAX — open source
  - Gemma — open-weights models, free to run locally / in your own cloud, under Google's Gemma terms
  - Gemini CLI — open source tool; it still calls the Gemini API for the model itself
- **API-only [D]:**
  - Gemini itself — the hosted Gemini models are accessed through Google's API / Google AI Studio / Vertex AI, not as a downloadable open model
  - Google's TPU Pods / AI Hypercomputer — accessed via Google Cloud, not owned as a local download

## 3. Supercomputer part
- **Google TPU Pods / AI Hypercomputer [D, in outline]:** Google's TPU-based AI supercomputing, offered as a cloud service via API / Google Cloud. You rent the compute; you do not download the pod.
- **Cray EX / XC40 [D, in outline]:** Cray supercomputers, now HPE (Hewlett Packard Enterprise) exascale hardware. Cray EX is the system behind exascale machines such as Frontier. This is physical supercomputer hardware, not a cloud API.
- **The contrast Douglas asked about:** Google's route is API/cloud access to TPU compute; Cray/HPE's route is exascale hardware installed at a site. Both are "supercomputers," in different senses — one as a service, one as a machine.

## 4. What still needs checking [GAP]
- Exact release dates and version numbers for Gemma, Gemini CLI, and TPU generations
- Pricing / access terms for AI Hypercomputer and Gemini API, which change over time
- Any claim that a specific model "is" another model — keep lineage as lineage, not as identity
