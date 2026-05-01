#from Models.base import Base, banco, session
from Models.herois import Heroi
from Models.missao import Missao
from Models.database import criar_tabelas, get_session

def inicializar():
    criar_tabelas()

def criar_missao(titulo: str, descricao: str, recompensa_xp: int, heroi_id: int) -> Missao:
    s = get_session()
    try:
        missao = Missao(titulo = titulo, descricao = descricao, recompensa_xp = recompensa_xp , heroi_id = heroi_id )
        s.add(missao)
        s.commit()
        s.refresh(missao)
        return missao
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()

def concluir_missao(missao_id: int) -> Missao:
    s = get_session()
    try:
        missao = s.query(Missao).filter_by(id=missao_id).first()
        if not missao:
            return False
        
        #s.delete(missao)

        if not missao:
            print("Missão não encontrada !!!!")
            return
        
        if missao.status == "Concluida":
            print("Missão já concluída.")
        else:
            missao.concluir()

        missao.heroi.ganhar_experiencia(missao.recompensa_xp)
        s.commit()
        return True
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()

def listar_missao()-> list[Missao]:
    s = get_session()
    try:
        return s.query(Missao).all()
    finally:
        s.close()

