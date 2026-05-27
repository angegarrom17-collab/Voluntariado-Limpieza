class ReporteService:

    def calcular_total_basura(self, lista_basura):
        # Suma total de basura recolectada
        total = 0
        for basura in lista_basura:
            total += basura.pesoKilos
        return total

    def calcular_promedio_basura(self, lista_basura):
        # Promedio por registros
        if len(lista_basura) == 0:
            return 0

        total = self.calcular_total_basura(lista_basura)
        return total / len(lista_basura)

    def contar_animales(self, lista_animales):
        # Cantidad de animales afectados registrados
        return len(lista_animales)

    def obtener_residuos_por_tipo(self, lista_basura):
        # Agrupa residuos por tipo
        resultados = {}

        for basura in lista_basura:
            tipo = basura.tipoResiduo

            if tipo not in resultados:
                resultados[tipo] = 0

            resultados[tipo] += basura.pesoKilos

        return resultados