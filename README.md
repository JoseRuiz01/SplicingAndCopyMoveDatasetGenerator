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
<summary>📌 Forgery Sample Generation</summary>

Original A: `---[Original Audio A]`
Original B: `---[Original Audio B]---`  
Forgery: `---[Segment from A]---[Segment from B]---[Remaining A]---`
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

- Forgery: `2s [Segment from A] + 1s [Segment from B] → 3s [Forgered Audio]` 
- Forgery: `1s [Segment from A] + 1s [Segment from B] → 2s [Forgered Audio]` 
- Forgery: `1s [Segment from A] + 1s [Segment from B] + 1s [Segment from A] → 3s [Forgered Audio]` 
- Forgery: `0.5s [Segment from A] + 1s [Segment from B] + 0.5s [Segment from A] → 2s [Forgered Audio]` 

</details>

---

## 📂 Output

For each original audio file, this tool will generate:
- Original audio dataset
- Copy-move forgeries dataset 
- Splicing forgeries dataset 

---

## 📌 Use Cases

- Training deep learning models for **audio forgery detection**
- Evaluating **robustness** of audio forensic systems
- Dataset creation for **research in speech integrity**
