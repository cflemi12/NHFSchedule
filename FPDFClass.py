""""
Wrapper class for the FPDF.
Enables use of HTML. 
@author Chase Fleming
4/23/17
"""

from fpdf import FPDF

title = "Schedule"


class PDF(FPDF):
    def header(self):
        # logo
        self.image("Images/ACE_logo_Bee.jpg", 10, 13, 40)
        self.image("Images/ACE_logo_Bee.jpg", 160, 13, 40)
        self.set_font('Helvetica', '', 32)
        # Calculate width of title and position
        w = self.get_string_width(title) + 10
        self.set_x((210 - w) / 2)
        # Colors
        self.set_text_color(12, 12, 12)
        # Title
        self.cell(w, 39, title, 0, 1, 'C', 0)
        # Line break
        self.ln(1)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Helvetica', 'I', 6)
        # Text color in gray
        self.set_text_color(128)
        # Give border
        self.set_line_width(1)
        # Page number
        self.cell(0, 10, "National History Bee", 0, 0, 'C')

    def schedule_name(self, name):
        # Arial 12
        self.set_font('Helvetica', 'B', 22)
        # Title
        w = self.get_string_width(name) + 10
        self.set_x((210 - w) / 2)
        self.set_line_width(1.25)
        self.cell(w, 15, name, 1, 1, 'C', 0)
        # Line break
        self.ln(10)

    def schedule_body(self, schedule):
        # add schedule to pdf
        # something to do with
        self.set_margins(10, 10)
        self.set_line_width(.75)
        self.set_font('Helvetica', '', 16)
        for spot in schedule:
            self.cell(95, 20, spot[0], align="C", border=1)
            self.cell(95, 20, spot[1], align="C", border=1)
            self.ln(20)

    def print_schedule(self, name, schedule):
        self.add_page()
        self.schedule_name(name)
        self.schedule_body(schedule)
