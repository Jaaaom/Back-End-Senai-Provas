#from Models.base import Base
from Models.herois import Heroi
from Models.missao import Missao
from Models.database import criar_tabelas, get_session

def inicializar():
    criar_tabelas()

# ─── CRUD Guida Controller ────────────────────────────────────────────────────────────

def registrar_heroi(nome: str, classe: str, nivel: int, xp: int) -> Heroi:
    s = get_session()
    try:
        heroi = Heroi(nome = nome, classe = classe, nivel = nivel , pontos_experiencia = xp )
        s.add(heroi)
        s.commit()
        s.refresh(heroi)
        return heroi
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()

def listar_herois()-> list[Heroi]:
    s = get_session()
    try:
        return s.query(Heroi).all()
    finally:
        s.close()

def buscar_heroi(heroi_id: int ) -> Heroi | None:
    s = get_session()
    try:
        return s.query(Heroi).filter_by(id=heroi_id).first()
    finally:
        s.close()
    

def remover_heroi(heroi_id: int)-> bool:
    s = get_session()
    try:
        usuario = s.query(Heroi).filter_by(id=heroi_id).first()
        if not usuario:
            return False
        
        s.delete(usuario)
        s.commit()
        return True
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


