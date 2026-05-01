from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Models.base import Base


class Heroi(Base):
    __tablename__ = 'herois'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    classe = Column(String(100), nullable=False)
    nivel = Column(Integer)
    pontos_experiencia = Column(Integer)

    missoes = relationship("Missao", back_populates="heroi", cascade="all, delete")

    def ganhar_experiencia(self, xp):
        self.pontos_experiencia += xp
        self.subir_nivel()

    def subir_nivel(self):
        while self.pontos_experiencia >= 100:
            self.pontos_experiencia -= 100
            self.nivel += 1

    def resumo(self):
        return f"ID {self.id} | Herói: {self.nome} | Classe: {self.classe} | Nível: {self.nivel} | XP: {self.pontos_experiencia}"