import logging

logging.basicConfig(level=logging.INFO, filename="registro.log",
                    format="%(asctime)s - %(levelname)s - %(message)s")

print("Digite a palavra ou frase para verificar se é um palíndromo: ")
palavra = input()
palavralimpa = palavra.lower()
logging.info(palavralimpa)

palavrainvertida = (palavralimpa[::-1])

if palavralimpa == palavrainvertida:
    logging.info("É um palíndromo")

else:
    logging.info("Não é um palíndromo")
