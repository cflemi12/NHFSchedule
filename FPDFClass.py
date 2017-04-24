""""
Wrapper class for the FPDF.
Enables use of HTML. 
@author Chase Fleming
4/23/17
"""

from fpdf import FPDF

title = "National History Fair Schedule"


class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calculate width of title and position
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colors of frame, background and text
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Thickness of frame (1 mm)
        self.set_line_width(1)
        # Title
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Line break
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 6)
        # Text color in gray
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, "National History Fair", 0, 0, 'C')

    def schedule_name(self, name):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 6, name, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def schedule_body(self, schedule):
        # add schedule to pdf
        # something to do with
        pass

    def print_schedule(self, name, schedule):
        self.add_page()
        self.schedule_name(name)
        self.schedule_body(schedule)
