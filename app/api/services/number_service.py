class NumberService:
    @staticmethod
    def convert_to_words(n: int) -> str:        
        unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
        if 0 <= n <= 9:
            return unidades[n]
        return "Número fuera de rango (0-9)"