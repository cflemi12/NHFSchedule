""""
Wrapper class for the FPDF.
Enables use of HTML. 
@author Chase Fleming
4/23/17
"""

from fpdf import FPDF
from operator import itemgetter

title = "Schedule"

def converter(interval):
    times = {110.0: "10:00 am", 110.5: "10:30 am", 111.0: "11:00 am", 111.5: "11:30 am", 112.0: "12:00 pm",
             112.5: "12:30 pm", 113.0: "1:00 pm", 113.5: "1:30 pm", 114.0: "2:00 pm", 114.5: "2:30 pm",
             115.0: "3:00 pm", 115.5: "3:30 pm", 116.0: "4:00 pm", 116.5: "4:30 pm", 117.0: "5:00 pm",
             117.5: "5:30 pm", 118.0: "6:00 pm", 118.5: "6:30 pm", 119.0: "7:00 pm", 119.5: "7:30 pm",
             120.0: "8:00 pm", 120.5: "8:30 pm", 121.0: "9:00 pm", 121.5: "9:30 pm", 122.0: "10:00 pm",
             210.0: "10:00 am", 210.5: "10:30 am", 211.0: "11:00 am", 211.5: "11:30 am", 212.0: "12:00 pm",
             212.5: "12:30 pm", 213.0: "1:00 pm", 213.5: "1:30 pm", 214.0: "2:00 pm", 214.5: "2:30 pm",
             215.0: "3:00 pm", 215.5: "3:30 pm", 216.0: "4:00 pm", 216.5: "4:30 pm", 217.0: "5:00 pm",
             217.5: "5:30 pm", 218.0: "6:00 pm", 218.5: "6:30 pm", 219.0: "7:00 pm", 219.5: "7:30 pm",
             220.0: "8:00 pm", 220.5: "8:30 pm", 221.0: "9:00 pm", 221.5: "9:30 pm", 222.0: "10:00 pm",
             109.0: "9:00 am", 109.5: "9:30 am", 209: "9:00 am", 209.5: "9:30 am"}
    datestring = ""
    day = str(interval[0][0])[0]
    if day == "1":
        datestring += "Friday"
    else:
        datestring += "Saturday"
    time1 = times[interval[0][0]]
    time2 = times[interval[0][1]]
    time3 = time1 + " to " + time2
    datestring = datestring + " " + time3
    return datestring




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

    def schedule_name(self, name, id, seed):
        # Arial 12
        self.set_font('Helvetica', 'B', 22)
        # Title
        w = self.get_string_width(name) + 10
        self.set_x((210 - w) / 2)
        self.set_line_width(1.25)
        self.cell(w, 15, name, 1, 1, 'C', 0)
        # Fill id
        w = self.get_string_width(str(id)) + 10
        self.set_x((210 - w) / 2)
        self.set_line_width(1.25)
        val = seed.upper() + "-" + str(id).upper()
        self.cell(w, 15, val, 1, 1, 'C', 0)
        # Line break
        self.ln(10)


    def schedule_body(self, schedule):
        # add schedule to pdf
        # something to do with
        self.set_margins(10, 10)
        self.set_line_width(.75)
        self.set_font('Helvetica', '', 12)
        for spot in sorted(schedule, key=itemgetter(1)):
            time = converter(spot[1])
            print spot[2]
            place = "Room N"
            if spot[2] is not None:
                place = spot[2]
            self.cell(82, 20, spot[0], align="C", border=1)
            self.cell(82, 20, time, align="C", border=1)
            self.cell(25, 20, place, align="C", border=1)
            self.ln(20)

    def print_schedule(self, name, schedule, id, seed):
        self.add_page()
        self.schedule_name(name, id, seed)
        self.schedule_body(schedule)
