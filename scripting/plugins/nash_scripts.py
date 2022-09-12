import pcbnew
import re
import datetime


class text_by_date( pcbnew.ActionPlugin ):
    def defaults( self ):
        self.name = "Add date on PCB"
        self.category = "Modify PCB"
        self.description = "Automaticaly add date on an existing PCB"

    def Run( self ):
        pcb = pcbnew.GetBoard()
        for draw in pcb.m_Drawings:
            if draw.GetClass() == 'PTEXT':
                txt = re.sub( "\$date\$ [0-9]{4}-[0-9]{2}-[0-9]{2}",
                                 "$date$", draw.GetText() )
                if txt == "$date$":
                    draw.SetText( "$date$ %s"%datetime.date.today() )

class rip_up( pcbnew.ActionPlugin ):
    def defaults( self ):
        self.name = "Rip Up All Traces"
        self.category = "Modify PCB"
        self.description = "Rip up all traces on the PCB"

    def Run( self ):
        pcb = pcbnew.GetBoard()
        tracks = pcb.GetTracks()
        for t in tracks:
            pcb.Delete(t)

text_by_date().register()
rip_up().register()
