# Indonesian Sentence Structure Checker

This project is a Python-based application that uses a Finite Automaton (FA) to recognize and parse Indonesian sentence structures. The program identifies different components of a sentence, checks the validity of the structure, and determines if the sentence is logical. The application is built with Tkinter for a graphical user interface (GUI).

## Project Structure

### TokenRecognizerFA Class

The `TokenRecognizerFA` class is responsible for building and managing the Finite Automaton. It recognizes different parts of a sentence, such as subjects, predicates, objects, and adverbials.

- **Attributes**:
  - `states`: Dictionary representing the states of the FA.
  - `final_states`: Dictionary storing the final states for each token category (S, P, O, K).

- **Methods**:
  - `__init__()`: Initializes the FA and builds it with predefined words.
  - `build_fa()`: Defines words for subjects, predicates, objects, and adverbials and adds them to the FA.
  - `add_word_to_fa(word, category)`: Adds a word to the FA under the specified category.
  - `recognize_token(token)`: Recognizes a token and returns its category.
  - `recognize_sequence(words)`: Recognizes a sequence of words and returns a list of categorized tokens.

### Parser Class

The `Parser` class utilizes the `TokenRecognizerFA` to parse sentences and check their validity and logical structure.

- **Attributes**:
  - `token_recognizer`: An instance of `TokenRecognizerFA`.
  - `stack`: List to hold the structure of the recognized tokens.
  - `tokens`: List to hold the actual tokens.

- **Methods**:
  - `__init__(token_recognizer)`: Initializes the parser with a token recognizer.
  - `parse(sentence)`: Parses a given sentence, checks its structure, and determines if it is logical.
  - `is_valid_structure()`: Checks if the recognized tokens form a valid sentence structure.
  - `is_logical_sentence()`: Checks if the recognized tokens form a logical sentence.

### GUI

The graphical user interface (GUI) is built using Tkinter. It allows users to input a sentence and check its structure and logic.

- **Functions**:
  - `check_sentence()`: Retrieves the sentence from the entry, parses it, and displays the results.
  - `show_landing_page()`: Displays the landing page with project details.
  - `main_page_pack()`: Packs the main page components.

## Instructions to Run the Program

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/indonesian-sentence-structure-checker.git
    cd indonesian-sentence-structure-checker
    ```

2. **Install Required Libraries**:
    Make sure you have Tkinter installed. Tkinter is usually included with Python, but you can install it using:
    ```bash
    sudo apt-get install python3-tk
    ```

3. **Run the Program**:
    ```bash
    python main.py
    ```

4. **Use the Application**:
    - The application will open a GUI window.
    - The landing page provides project information and a button to start.
    - Enter a sentence in the input field and click "Periksa" to check the sentence structure and logic.
    - The results will be displayed in a message box.

## Example Sentences

Here are some example sentences you can try:
- "saya makan nasi"
- "kamu minum air di rumah"
- "dia bermain bola di lapangan"

## Contributors

- Nathan Dava Arkananta (1301223297)
- Umar Khairur Rahman (1301223410)
- Ariyuga Rizky Wahyudi (1301223440)

Feel free to contribute to this project by submitting issues or pull requests. We welcome any suggestions or improvements.

---

# Pemeriksa Struktur Kalimat Bahasa Indonesia

Proyek ini adalah aplikasi berbasis Python yang menggunakan Automata Hingga (FA) untuk mengenali dan menganalisis struktur kalimat dalam bahasa Indonesia. Program ini mengidentifikasi berbagai komponen kalimat, memeriksa validitas struktur, dan menentukan apakah kalimat tersebut logis. Aplikasi ini dibangun dengan Tkinter untuk antarmuka pengguna grafis (GUI).

## Struktur Proyek

### Kelas TokenRecognizerFA

Kelas `TokenRecognizerFA` bertanggung jawab untuk membangun dan mengelola Automata Hingga. Kelas ini mengenali berbagai bagian dari kalimat, seperti subjek, predikat, objek, dan keterangan.

- **Atribut**:
  - `states`: Kamus yang mewakili keadaan dari FA.
  - `final_states`: Kamus yang menyimpan keadaan akhir untuk setiap kategori token (S, P, O, K).

- **Metode**:
  - `__init__()`: Menginisialisasi FA dan membangunnya dengan kata-kata yang telah ditentukan.
  - `build_fa()`: Mendefinisikan kata-kata untuk subjek, predikat, objek, dan keterangan dan menambahkannya ke FA.
  - `add_word_to_fa(word, category)`: Menambahkan kata ke FA di bawah kategori yang ditentukan.
  - `recognize_token(token)`: Mengenali token dan mengembalikan kategorinya.
  - `recognize_sequence(words)`: Mengenali urutan kata dan mengembalikan daftar token yang dikategorikan.

### Kelas Parser

Kelas `Parser` menggunakan `TokenRecognizerFA` untuk menganalisis kalimat dan memeriksa validitas serta struktur logisnya.

- **Atribut**:
  - `token_recognizer`: Sebuah instance dari `TokenRecognizerFA`.
  - `stack`: Daftar untuk menyimpan struktur dari token yang dikenali.
  - `tokens`: Daftar untuk menyimpan token yang sebenarnya.

- **Metode**:
  - `__init__(token_recognizer)`: Menginisialisasi parser dengan pengenal token.
  - `parse(sentence)`: Menganalisis kalimat yang diberikan, memeriksa strukturnya, dan menentukan apakah kalimat tersebut logis.
  - `is_valid_structure()`: Memeriksa apakah token yang dikenali membentuk struktur kalimat yang valid.
  - `is_logical_sentence()`: Memeriksa apakah token yang dikenali membentuk kalimat yang logis.

### GUI

Antarmuka pengguna grafis (GUI) dibangun menggunakan Tkinter. Ini memungkinkan pengguna untuk memasukkan kalimat dan memeriksa struktur serta logikanya.

- **Fungsi**:
  - `check_sentence()`: Mengambil kalimat dari entri, menganalisisnya, dan menampilkan hasilnya.
  - `show_landing_page()`: Menampilkan halaman pembuka dengan detail proyek.
  - `main_page_pack()`: Mengatur komponen halaman utama.

## Instruksi Menjalankan Program

1. **Kloning Repository**:
    ```bash
    git clone https://github.com/yourusername/indonesian-sentence-structure-checker.git
    cd indonesian-sentence-structure-checker
    ```

2. **Instalasi Perpustakaan yang Diperlukan**:
    Pastikan Anda telah menginstal Tkinter. Tkinter biasanya sudah termasuk dalam Python, tetapi Anda dapat menginstalnya menggunakan:
    ```bash
    sudo apt-get install python3-tk
    ```

3. **Jalankan Program**:
    ```bash
    python fa_sentence_recognizer.py.py
    ```

4. **Gunakan Aplikasi**:
    - Aplikasi akan membuka jendela GUI.
    - Halaman pembuka menyediakan informasi proyek dan tombol untuk memulai.
    - Masukkan kalimat di bidang input dan klik "Periksa" untuk memeriksa struktur dan logika kalimat.
    - Hasilnya akan ditampilkan di kotak pesan.

## Contoh Kalimat

Berikut adalah beberapa contoh kalimat yang dapat Anda coba:
- "saya makan nasi"
- "kamu minum air di rumah"
- "dia bermain bola di lapangan"

## Kontributor

- Nathan Dava Arkananta (1301223297)
- Umar Khairur Rahman (1301223410)
- Ariyuga Rizky Wahyudi (1301223440)

Silakan berkontribusi pada proyek ini dengan mengajukan masalah atau permintaan penarikan. Kami menerima saran atau perbaikan apa pun.
