from fpdf import FPDF


class cert():
    def __init__(self, name):
        self._cert = FPDF()
        self._cert.add_page()
        self._cert.set_font("helvetica", "B", 50)
        self._cert.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._cert.image("shirtificate.png", w=self._cert.epw)

        self._cert.set_font_size(30)
        self._cert.set_text_color(255,255,255)
        self._cert.text(x=47.5, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self._cert.output(name)

def main():
    yourname = input("Name: ")
    shirtificate = cert(yourname)
    shirtificate.save("shirtificate.pdf")

if __name__ == "__main__":
    main()