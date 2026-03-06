from repositories.rubro_repositori import rubro_repositori

class RubroService:

    def listar(self, db):
        return rubro_repositori.get_all(db)

    def crear(self, db, data):
        return rubro_repositori.create(db, data)

    def eliminar(self, db, id):
        return rubro_repositori.delete(db, id)


rubro_service = RubroService()