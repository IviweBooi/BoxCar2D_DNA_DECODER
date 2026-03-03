import base64
import zlib


def decode_car_code_to_dna(car_code: str) -> str:
    """
    Converts a compressed BoxCar share code into a synthetic DNA sequence.

    Pipeline:
    1. Base64 decode
    2. zlib decompress
    3. Convert decompressed bytes to binary
    4. Map 2-bit binary pairs to DNA bases (ATCG order)
    """

    try:
        # Step 1: Base64 decode
        compressed_bytes = base64.b64decode(car_code)

        # Step 2: Decompress using zlib
        decompressed_bytes = zlib.decompress(compressed_bytes)

    except Exception as e:
        print("Error during decoding or decompression:", e)
        return None

    # Step 3: Convert bytes to continuous binary string
    binary_stream = ''.join(f'{byte:08b}' for byte in decompressed_bytes)

    # Step 4: Define 2-bit → nucleotide mapping (ATCG order)
    binary_to_nucleotide = {
        "00": "A",
        "01": "T",
        "10": "C",
        "11": "G"
    }

    # Step 5: Convert binary stream into DNA sequence
    dna_sequence = ''.join(
        binary_to_nucleotide[binary_stream[i:i+2]]
        for i in range(0, len(binary_stream), 2)
    )

    return dna_sequence


def save_sequence_to_fasta(filename: str, header: str, sequence: str):
    """
    Appends a DNA sequence to a FASTA file.
    """
    with open(filename, "a") as fasta_file:
        fasta_file.write(f">{header}\n")
        fasta_file.write(sequence + "\n")


# -------------------------
# Program Execution
# -------------------------

raw_input_code = input("Paste the raw compressed car code here:\n")

dna_sequence = decode_car_code_to_dna(raw_input_code.strip())

if dna_sequence:
    print("\nDNA sequence generated successfully.")
    print(f"Sequence length: {len(dna_sequence)} bases")

    save_option = input("Do you want to save this sequence to FASTA? (y/n): ")

    if save_option.lower() == "y":
        header_name = input("Enter sequence header name (e.g., Car_Original): ")
        save_sequence_to_fasta("car_genomes.fasta", header_name, dna_sequence)
        print("Sequence saved to car_genomes.fasta")