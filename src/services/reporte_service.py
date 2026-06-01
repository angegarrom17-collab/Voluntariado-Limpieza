TIPOS_REPORTE = ("basura_total", "promedio_basura", "conteo_animales", "residuos_por_tipo")

class ReporteService:
    def calcular_total_basura(self, lista_basura: list) -> float:
        pesos = [b.pesoKilos for b in lista_basura]
        return sum(pesos)

    def calcular_promedio_basura(self, lista_basura: list) -> float:
        if len(lista_basura) == 0:
            return 0.0
        total = self.calcular_total_basura(lista_basura)
        return total / len(lista_basura)

    def contar_animales(self, lista_animales: list) -> int:
        return len(lista_animales)

    def obtener_residuos_por_tipo(self, lista_basura: list) -> dict:
        resultados: dict = {}
        for basura in lista_basura:
            tipo = basura.tipoResiduo
            if tipo not in resultados:
                resultados[tipo] = 0.0
            resultados[tipo] += basura.pesoKilos
        return resultados

    def obtener_estadisticas_animales(self, lista_animales: list) -> dict:
        estados_vistos: set = set()
        conteo: dict = {}

        for animal in lista_animales:
            estado = animal.estado
            estados_vistos.add(estado)
            conteo[estado] = conteo.get(estado, 0) + 1

        return {
            "conteo_por_estado": conteo,
            "estados_presentes": list(estados_vistos),
            "total": len(lista_animales)
        }

    def tipos_reporte_disponibles(self) -> tuple:
        return TIPOS_REPORTE