from notas import CHROMATIC_SCALE, TOM, SEMITOM, Note


class Acorde:
    def __init__(self, notes=[]) -> None:
        self.notes = notes
    
    def makeChord(self, note:str='C', thetrad=False) -> None:
        if(self.notes is None):
            idx_note = CHROMATIC_SCALE.index(note)
            self.notes.append(idx_note)
            self.notes.append(idx_note+4)

