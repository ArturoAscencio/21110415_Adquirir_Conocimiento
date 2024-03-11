# -*- coding: utf-8 -*-
import unicodedata

class Chatbot:
    def __init__(self):
        self.database = {
            "¿Cómo estás?": "Estoy bien, gracias por preguntar.",
            "¿Cuál es tu nombre?": "Mi nombre es Chatbot pro.",
            # Puedes agregar más preguntas y respuestas aquí
        }

    def remover_acentos(self, texto):
        return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

    def responder(self, pregunta):
        pregunta_normalizada = self.remover_acentos(pregunta.lower().strip())
        
        for pregunta_bd in self.database:
            pregunta_bd_normalizada = self.remover_acentos(pregunta_bd.lower().strip())
            if pregunta_normalizada in pregunta_bd_normalizada:
                return self.database[pregunta_bd]

        respuesta = input("Lo siento, no tengo una respuesta para eso. ¿Cuál sería la respuesta adecuada? ")
        self.database[pregunta] = respuesta
        return "Entendido, he aprendido algo nuevo."
    
    def ver_base_datos(self):
        print("Base de datos actual:")
        for pregunta, respuesta in self.database.items():
            print(f"Pregunta: {pregunta} - Respuesta: {respuesta}")

def main():
    chatbot = Chatbot()
    print("¡Hola! Soy un chatbot sencillito. Puedes preguntarme lo que quieras y si no tengo respuesta para eso aprendere cual es esa respuesta.")

    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break
        respuesta = chatbot.responder(entrada)
        print("Chatbot:", respuesta)
        
        # Ver la base de datos
        chatbot.ver_base_datos()

if __name__ == "__main__":
    main()
