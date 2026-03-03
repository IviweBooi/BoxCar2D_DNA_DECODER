# BoxCar2D DNA Encoder

## Project Overview

This project converts the compressed genetic representation of a **BoxCar2D** car into a synthetic DNA sequence. The DNA sequences can be saved in **FASTA** format for further analysis or sequence alignment using tools like **MEGA**.  

The main goals of the project are:

1. Decode a BoxCar2D car code.
2. Convert it into a binary representation.
3. Map the binary to nucleotides (A, T, C, G) using a 2-bit encoding.
4. Save sequences in FASTA format.
5. Compare sequences to observe differences between original and mutated cars.

---

## Requirements

- Python 3.8+  
- Libraries: `base64`, `zlib` (both included in standard Python library)  
- Optional: MEGA software for visual sequence alignment

---

## How to Run

1. **Open the project folder in VS Code** or your preferred Python editor.  
2. Open `encoder.py`.  
3. Run the script
4. When prompted, **paste the raw compressed car code**:

5. The script will generate the DNA sequence and display the length.  

6. If you choose to save:

- Enter `y` when prompted
- Give a header name (e.g., `Car_Original` or `Car_Mutated`)  
- The sequence will be appended to `car_genomes.fasta`

7. Repeat the process for a mutated car to save multiple sequences in the same FASTA file.

---

## Functions in `encoder.py`

| Function | Description |
|----------|-------------|
| `decode_car_code_to_dna(car_code)` | Converts a Base64 + zlib compressed BoxCar code to a DNA sequence using 2-bit mapping (00→A, 01→T, 10→C, 11→G) |
| `save_sequence_to_fasta(filename, header, sequence)` | Appends a DNA sequence to a FASTA file with the given header |
| `compare_dna_sequences(seq1, seq2)` | Optional: compares two DNA sequences and prints the nucleotide differences |



