from notas import Note

CHROMATIC_SCALE = (
    'C', 'C#',
    'D', 'D#',
    'E',  'F',
    'F#', 'G',
    'G#', 'A',
    'A#', 'B',
    'C'
)

SEMITOM = 1
TOM     = 2
MAJOR_SCALE = [TOM, TOM, SEMITOM, TOM, TOM, TOM, SEMITOM]
MINOR_SCALE = [TOM, SEMITOM, TOM, TOM, SEMITOM, TOM, TOM]


class Scale:
    def __init__(self, scale=MAJOR_SCALE) -> None:
        
    
    def show_scale_of(self, note):
