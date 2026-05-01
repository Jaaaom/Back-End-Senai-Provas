from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Models.base import Base


class Missao(Base):
    __tablename__ = 'missoes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    descricao = Column(String(400), nullable=False)
    recompensa_xp = Column(Integer)
    status = Column(String(50), default="pendente")

    heroi_id = Column(Integer, ForeignKey('herois.id'))
    heroi = relationship("Heroi", back_populates="missoes")

    def concluir(self):
        self.status = "concluida"

    def resumo(self):
        return f"ID Missão: {self.id} | Status: [{self.status}] | Título: {self.titulo} | XP: {self.recompensa_xp} | ID do Herói Responsável: {self.heroi_id}"