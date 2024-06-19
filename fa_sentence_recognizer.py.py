import tkinter as tk
from tkinter import messagebox

class TokenRecognizerFA:
    def __init__(self):
        self.states = {}
        self.final_states = {
            'S': [],
            'P': [],
            'O': [],
            'K': []
        }
        self.build_fa()

    def build_fa(self):
        self.subjects = ["saya", "kamu", "dia", "kami", "mereka"]
        self.predicates = ["makan", "minum", "tidur", "bermain", "belajar"]
        self.objects = ["nasi", "air", "bola", "buku", "meja"]
        self.adverbials = ["di rumah", "di sekolah", "di lapangan", "di kantor", "di taman"]

        for category, words in [('S', self.subjects), ('P', self.predicates), ('O', self.objects), ('K', self.adverbials)]:
            for word in words:
                self.add_word_to_fa(word, category)

    def add_word_to_fa(self, word, category):
        current_state = 'q0'
        for char in word:
            next_state = f'q{len(self.states) + 1}'
            if current_state not in self.states:
                self.states[current_state] = {}
            if char not in self.states[current_state]:
                self.states[current_state][char] = next_state
            current_state = self.states[current_state][char]
        self.final_states[category].append(current_state)

    def recognize_token(self, token):
        current_state = 'q0'
        for char in token:
            if current_state in self.states and char in self.states[current_state]:
                current_state = self.states[current_state][char]
            else:
                return "unknown"

        for category, states in self.final_states.items():
            if current_state in states:
                return category

        return "unknown"

    def recognize_sequence(self, words):
        recognized_sequence = []
        i = 0
        while i < len(words):
            if i + 1 < len(words) and f"{words[i]} {words[i+1]}" in self.adverbials:
                token = f"{words[i]} {words[i+1]}"
                token_type = self.recognize_token(token)
                if token_type != "unknown":
                    recognized_sequence.append((token, token_type))
                    i += 2
                    continue
            token = words[i]
            token_type = self.recognize_token(token)
            if token_type == "unknown":
                return None
            recognized_sequence.append((token, token_type))
            i += 1
        return recognized_sequence

class Parser:
    def __init__(self, token_recognizer):
        self.token_recognizer = token_recognizer
        self.stack = []
        self.tokens = []

        # Valid combinations for logical sentences
        self.valid_combinations = {
            # Subyek - Predikat - Obyek
            ("saya", "makan", "nasi"), ("saya", "minum", "air"), ("saya", "bermain", "bola"), ("saya", "belajar", "buku"),
            ("dia", "makan", "nasi"), ("dia", "minum", "air"), ("dia", "bermain", "bola"), ("dia", "belajar", "buku"),
            ("kami", "makan", "nasi"), ("kami", "minum", "air"), ("kami", "bermain", "bola"), ("kami", "belajar", "buku"),
            ("mereka", "makan", "nasi"), ("mereka", "minum", "air"), ("mereka", "bermain", "bola"), ("mereka", "belajar", "buku"),
            ("kamu", "makan", "nasi"), ("kamu", "minum", "air"), ("kamu", "bermain", "bola"), ("kamu", "belajar", "buku"),
            # Subyek - Predikat
            ("saya", "tidur", ""), ("dia", "tidur", ""), ("kami", "tidur", ""), ("kamu", "tidur", ""), ("mereka", "tidur", ""),
            # Subyek - Predikat - Obyek - Keterangan
            ("saya", "makan", "nasi di rumah"), ("saya", "makan", "nasi di sekolah"), ("saya", "makan", "nasi di lapangan"),
            ("saya", "makan", "nasi di kantor"), ("saya", "makan", "nasi di taman"),
            ("saya", "minum", "air di rumah"), ("saya", "minum", "air di sekolah"), ("saya", "minum", "air di lapangan"),
            ("saya", "minum", "air di kantor"), ("saya", "minum", "air di taman"),
            ("dia", "makan", "nasi di rumah"), ("dia", "makan", "nasi di sekolah"), ("dia", "makan", "nasi di lapangan"),
            ("dia", "makan", "nasi di kantor"), ("dia", "makan", "nasi di taman"),
            ("dia", "minum", "air di rumah"), ("dia", "minum", "air di sekolah"), ("dia", "minum", "air di lapangan"),
            ("dia", "minum", "air di kantor"), ("dia", "minum", "air di taman"),
            ("kami", "bermain", "bola di rumah"), ("kami", "bermain", "bola di sekolah"), ("kami", "bermain", "bola di lapangan"),
            ("kami", "bermain", "bola di kantor"), ("kami", "bermain", "bola di taman"),
            ("mereka", "bermain", "bola di rumah"), ("mereka", "bermain", "bola di sekolah"), ("mereka", "bermain", "bola di lapangan"),
            ("mereka", "bermain", "bola di kantor"), ("mereka", "bermain", "bola di taman"),
            ("kamu", "belajar", "buku di rumah"), ("kamu", "belajar", "buku di sekolah"), ("kamu", "belajar", "buku di lapangan"),
            ("kamu", "belajar", "buku di kantor"), ("kamu", "belajar", "buku di taman"),
            # Subyek - Predikat - Keterangan
            ("saya", "tidur", "di rumah"), ("saya", "tidur", "di sekolah"), ("saya", "tidur", "di lapangan"),
            ("saya", "tidur", "di kantor"), ("saya", "tidur", "di taman"),
            ("dia", "tidur", "di rumah"), ("dia", "tidur", "di sekolah"), ("dia", "tidur", "di lapangan"),
            ("dia", "tidur", "di kantor"), ("dia", "tidur", "di taman"),
            ("kami", "tidur", "di rumah"), ("kami", "tidur", "di sekolah"), ("kami", "tidur", "di lapangan"),
            ("kami", "tidur", "di kantor"), ("kami", "tidur", "di taman"),
            ("kamu", "tidur", "di rumah"), ("kamu", "tidur", "di sekolah"), ("kamu", "tidur", "di lapangan"),
            ("kamu", "tidur", "di kantor"), ("kamu", "tidur", "di taman"),
            ("mereka", "tidur", "di rumah"), ("mereka", "tidur", "di sekolah"), ("mereka", "tidur", "di lapangan"),
            ("mereka", "tidur", "di kantor"), ("mereka", "tidur", "di taman"),
            # Subyek - Predikat tanpa Obyek tapi dengan Keterangan
            ("saya", "belajar", "di rumah"), ("saya", "belajar", "di sekolah"), ("saya", "belajar", "di lapangan"),
            ("saya", "belajar", "di kantor"), ("saya", "belajar", "di taman"),
            ("dia", "belajar", "di rumah"), ("dia", "belajar", "di sekolah"), ("dia", "belajar", "di lapangan"),
            ("dia", "belajar", "di kantor"), ("dia", "belajar", "di taman"),
            ("kami", "belajar", "di rumah"), ("kami", "belajar", "di sekolah"), ("kami", "belajar", "di lapangan"),
            ("kami", "belajar", "di kantor"), ("kami", "belajar", "di taman"),
            ("kamu", "belajar", "di rumah"), ("kamu", "belajar", "di sekolah"), ("kamu", "belajar", "di lapangan"),
            ("kamu", "belajar", "di kantor"), ("kamu", "belajar", "di taman"),
            ("mereka", "belajar", "di rumah"), ("mereka", "belajar", "di sekolah"), ("mereka", "belajar", "di lapangan"),
            ("mereka", "belajar", "di kantor"), ("mereka", "belajar", "di taman")
        }

    def parse(self, sentence):
        self.stack = []
        self.tokens = []
        words = sentence.split()
        recognized_sequence = self.token_recognizer.recognize_sequence(words)
        if not recognized_sequence:
            print("Unrecognized sequence")
            return False, False
        
        for word, token_type in recognized_sequence:
            self.stack.append(token_type)
            self.tokens.append(word)
            print(f"Recognized {word} as {token_type}")

        print(f"Token stack: {self.stack}")
        is_valid_structure = self.is_valid_structure()
        is_logical = self.is_logical_sentence() if is_valid_structure else False
        return is_valid_structure, is_logical

    def is_valid_structure(self):
        # Valid structures: S-P-O-K, S-P-K, S-P-O, S-P
        valid_structures = [
            ["S", "P", "O", "K"],
            ["S", "P", "K"],
            ["S", "P", "O"],
            ["S", "P"]
        ]
        
        print(f"Checking structure: {self.stack} against {valid_structures}")
        return self.stack in valid_structures

    def is_logical_sentence(self):
        subject = predicate = obj = keterangan = ""
        if "S" in self.stack:
            subject = self.tokens[self.stack.index("S")]
        if "P" in self.stack:
            predicate = self.tokens[self.stack.index("P")]
        if "O" in self.stack:
            obj = self.tokens[self.stack.index("O")]
        if "K" in self.stack:
            keterangan = self.tokens[self.stack.index("K")]

        print(f"Checking logic for: ({subject}, {predicate}, {obj}, {keterangan})")
        if (subject, predicate, obj) in self.valid_combinations:
            return True
        if (subject, predicate, f"{obj} {keterangan}") in self.valid_combinations:
            return True
        if (subject, predicate, keterangan) in self.valid_combinations:
            return True
        if obj == "" and keterangan != "" and (subject, predicate, keterangan.strip()) in self.valid_combinations:
            return True
        return False

# Initialize Token Recognizer FA
token_recognizer = TokenRecognizerFA()

# Initialize Parser
parser = Parser(token_recognizer)

def check_sentence():
    sentence = entry.get()
    is_valid_structure, is_logical = parser.parse(sentence)
    result_structure = "Valid" if is_valid_structure else "Tidak Valid"
    result_logic = "Logis" if is_logical else "Tidak Logis"
    recognized_words = " ".join(f"{word} ({token})" for word, token in zip(parser.tokens, parser.stack))
    structure = " - ".join(parser.stack)
    messagebox.showinfo("Hasil Pengecekan", f"Kalimat: '{sentence}'\nStruktur: {result_structure}\nLogika: {result_logic}\nRecognized words: {recognized_words}\nStructure: {structure}")

def show_landing_page():
    landing_page = tk.Toplevel(root)
    landing_page.title("Tugas Besar Teori Bahasa dan Automata")
    tk.Label(landing_page, text="Tugas Besar Teori Bahasa dan Automata", font=("Arial", 24, "bold"), fg="#333", bg="#f7f7f7", width=50, height=2, relief="solid", borderwidth=2, anchor="center").pack(pady=20)
    tk.Label(landing_page, text="Dibuat oleh:", font=("Arial", 18), fg="#666", bg="#f7f7f7", width=50, height=2, relief="solid", borderwidth=2, anchor="center").pack(pady=10)
    tk.Label(landing_page, text="Nathan Dava Arkananta (1301223297)", font=("Arial", 14), fg="#333", bg="#f7f7f7", width=50, height=2, relief="solid", borderwidth=2, anchor="center").pack(pady=2)
    tk.Label(landing_page, text="Umar Khairur Rahman (1301223410)", font=("Arial", 14), fg="#333", bg="#f7f7f7", width=50, height=2, relief="solid", borderwidth=2, anchor="center").pack(pady=2)
    tk.Label(landing_page, text="Ariyuga Rizky Wahyudi (1301223440)", font=("Arial", 14), fg="#333", bg="#f7f7f7", width=50, height=2, relief="solid", borderwidth=2, anchor="center").pack(pady=2)
    tk.Button(landing_page, text="Mulai", font=("Arial", 14, "bold"), fg="#fff", bg="#337ab7", width=20, height=2, relief="solid", borderwidth=2, command=lambda: [landing_page.destroy(), main_page.pack()]).pack(pady=10)

def main_page_pack():
    main_page.pack()

# Initialize GUI
root = tk.Tk()
root.title("Pemeriksa Struktur Kalimat Bahasa Indonesia")

# Show Landing Page
show_landing_page()

# Create Main Page
main_page = tk.Frame(root, bg="#f7f7f7")
main_page.pack_forget()

tk.Label(main_page, text="Masukkan Kalimat:", font=("Arial", 18), fg="#333", bg="#f7f7f7").pack(pady=10)
entry = tk.Entry(main_page, width=50, font=("Arial", 14), fg="#333", bg="#fff", relief="solid", borderwidth=2)
entry.pack(pady=10)

check_button = tk.Button(main_page, text="Periksa", font=("Arial", 14, "bold"), fg="#fff", bg="#337ab7", width=20, height=2, relief="solid", borderwidth=2, command=check_sentence)
check_button.pack(pady=10)

# Run the GUI event loop
root.mainloop()