import re

class Vocab:
    path_to_vocab = "borjas_vocabulary.txt"
    my_name = "Borya Tarovik"

    def __init__(self):
        self.whose_replicas = []
        self.replicas = []

    def preprocess_dialog(self, text="", they_name="Katya Bakalova"):
        replicas_idx = []
        self.whose_replicas = []
        self.replicas = []
        with open('dialog.txt', 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if line.startswith(self.my_name):
                    replicas_idx.append(i)
                    self.whose_replicas.append(1)
                if line.startswith(they_name):
                    replicas_idx.append(i)
                    self.whose_replicas.append(2)
            for i in range(len(replicas_idx)-1):
                str_from = replicas_idx[i] + 1
                str_to = replicas_idx[i+1]
                replica = "".join(lines[str_from:str_to])
                self.replicas.append(replica)
            assert( len(self.replicas)+1 == len(self.whose_replicas) )

    def create_vocab(self):
        plain_text = "".join(self.replicas)
        words = re.findall(r"[\w']+", plain_text)
        words_dict = dict()
        words_idx_dict = dict()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            if word not in words_dict:
                words_dict[word] = 1
        for i, word in enumerate(words_dict.keys()):
            words_idx_dict[word] = i


def main():
    print("Create vocabulary for VK chatbot")
    vocab = Vocab()
    vocab.preprocess_dialog()
    vocab.create_vocab()


if __name__ == '__main__':
    main()