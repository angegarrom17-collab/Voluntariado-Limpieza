class ReporteService:
    def calcular_total_basura(self, lista_basura):
        return sum(item.pesoKilos for item in lista_basura)

    def calcular_promedio_basura(self, lista_basura):
        con_peso = [i for i in lista_basura if i.pesoKilos > 0]
        return sum(i.pesoKilos for i in con_peso) / len(con_peso) if con_peso else 0.0

    def contar_animales(self, lista_animales):
        return len(lista_animales)

    def obtener_residuos_por_tipo(self, lista_basura):
        res = {}
        for item in lista_basura:
            tipo = item.tipoResiduo if item.tipoResiduo else "Desconocido"
            res[tipo] = res.get(tipo, 0.0) + item.pesoKilos
        return res