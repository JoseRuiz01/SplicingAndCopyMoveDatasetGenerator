# 🎧 Splicing and Copy-Move Audio Forgery Dataset Generator

This project contains **two audio forgery dataset generators** based on the [**TIMIT**](https://catalog.ldc.upenn.edu/LDC93S1) speech corpus. It simulates **splicing** and **copy-move forgeries** for use in training and evaluating audio forensic systems.

---

## 🛠️ Overview

The dataset generation process involves applying transformations to authentic audio files from TIMIT using two distinct methods:

### 🔀 1. <span style="color:#3498db">RandomPosition Method</span>

Simulates **forgeries** by:
- Selecting a **random segment** from the original audio.
- Inserting that segment at a **random new position**.
- Reconstructing the audio so that the inserted segment appears naturally within the waveform.

<details>
<summary>📌 Example (simplified)</summary>

Original: `---[Original Segment A]---[Original Segment B]---`  
Forgery: `---[Original Segment A]---[Copied Segment from B]---[Remaining B]---`
</details>

---

### 🔁 2. <span style="color:#e67e22">Concatenation Method</span>

Based on the paper:  
**_"Autoencoder for Audio Forgery Detection using Spliced and Copy-Move Audio"_**,  
📄 *Shaikh et al., 2021*  
[Read the paper here](https://arxiv.org/abs/2109.06665)

This method simulates **forgeries** by:
- Extracts **2-second and 1-second segments** from each audio file.
- **Concatenates** them in different combinations to simulate forged samples.
- Produces:
  - **3-second spliced audio**
  - **2-second spliced audio**

<details>
<summary>📌 Forgery Sample Generation</summary>

- Take `2s + 1s = 3s` → Spliced audio sample  
- Take `1s + 1s = 2s` → Another spliced sample
</details>

---

## 📂 Output

For each original audio file, this tool will generate:
- Authentic audio
- Copy-move forgeries (via RandomPosition)
- Splicing forgeries (via Concatenation)

---

## 📌 Use Cases

- Training deep learning models for **audio forgery detection**
- Evaluating **robustness** of audio forensic systems
- Dataset creation for **research in speech integrity**
