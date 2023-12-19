class cancion:
    def __init__(self, artista, album, imagen, ruta):
        self.artista = artista
        self.album = album
        self.imagen = imagen
        self.ruta = ruta


    def getartista(self):
        return self.artista
    def getalbum(self):
        return self.album
    def getimagen(self):
        return self.imagen
    def getruta(self):
        return self.ruta
    
    def setartista(self, artista):
        self.artista = artista
    def setalbum(self, album):
        self.album = album
    def setimagen(self, imagen):
        self.imagen = imagen
    def setruta(self, ruta):
        self.ruta = ruta
    
    def __repr__(self):
        return f"{self.artista},{self.album},{self.imagen},{self.ruta}"