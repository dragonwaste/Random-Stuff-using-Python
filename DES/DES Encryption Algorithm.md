# DES Encryption Algorithm (Python)

## 📌 Project Overview

This project is a **from-scratch implementation of the Data Encryption Standard (DES)** encryption algorithm written in Python. It demonstrates how DES performs encryption and decryption at the bit level, including permutations, key scheduling, Feistel rounds, and S-box substitutions.

The goal of this project is **educational** — to help students and cybersecurity learners understand how classical block ciphers work internally.

---

## ⚠️ Disclaimer

DES is considered **cryptographically insecure** by modern standards due to its short key length.

This implementation is intended **only for learning and academic purposes** and **must not be used in real-world security applications**.

---

## 🔐 What This Project Demonstrates

- Hexadecimal ↔ Binary conversions
- Initial and final permutations
- Key parity-bit dropping
- Key schedule generation
- Left circular shifts
- Expansion D-box
- S-box substitution
- Feistel network structure
- Encryption and decryption using reversed round keys

---

## 🧩 Algorithm Details

- **Block size:** 64 bits  
- **Key size:** 64 bits (56 bits effective)  
- **Rounds:** 16  
- **Cipher structure:** Feistel Network  

---

## 🧠 Project Structure

This project is implemented in a single Python script and includes:

- Conversion utilities (hex, binary, decimal)
- Permutation functions
- XOR logic
- DES tables:
  - Initial permutation
  - Expansion table
  - S-boxes
  - Straight permutation
  - Final permutation
- Full encryption and decryption process

---

## ▶️ Example Execution

### Input
```text
Plaintext:  0123456789ABCDEF
Key:        133457799BBCDFF1

