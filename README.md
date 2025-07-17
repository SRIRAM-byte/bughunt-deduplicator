# 🧹 dedupicator – Duplicate Line Cleaner for Recon

**dedupicator** is a simple Python 3 script to remove duplicate lines from input `.txt` files — ideal for cleaning reconnaissance output (subdomains, URLs, IPs) during bug bounty hunting and OSINT workflows.

---

### ✅ Features

- Removes **duplicate lines** from large text files
- Preserves original line order
- Prints total lines read and duplicates removed
- Saves cleaned results to `final_unique_sites.txt`
- Lightweight, fast, and dependency-free

---

### 🔧 Usage

```bash
python3 deduplicator.py sample_input.txt
