for i in range(8, 15):
    text = """from questions import Q{0}


class Q{1}(Q{0}):

    def __init__(self):
        super().__init__()

    def __{1}_fill_combo_boxes(self):
        pass

    def __{1}_connect_signals(self):
        pass
    """.format(i - 1, i)

    with open(f"_{i-3}_q_{i}.py", "w") as f:
        f.write(text)
