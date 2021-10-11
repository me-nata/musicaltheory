CHROMATIC_SCALE = (
    'C', 'C#',
    'D', 'D#',
    'E',  'F',
    'F#', 'G',
    'G#', 'A',
    'A#', 'B',
    'C', 'C#',
    'D', 'D#',
    'E',  'F',
)

SEMITOM = 1
TOM     = 2
MAJOR_SCALE = [TOM, TOM, SEMITOM, TOM, TOM, TOM, SEMITOM]
MINOR_SCALE = [TOM, SEMITOM, TOM, TOM, SEMITOM, TOM, TOM]

class Note:
    def __init__(self, note:str = 'C', octave:int = 4) -> None:
        self.note   = CHROMATIC_SCALE.index(note)
        self.octave = octave