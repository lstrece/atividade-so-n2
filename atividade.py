import ctypes

# Carregar a DLL
atividade_dll = ctypes.CDLL('./atividade.dll')

# Definir o tipo de retorno e os tipos de argumentos da função
atividade_dll.soma.restype = ctypes.c_int
atividade_dll.soma.argtypes = [ctypes.c_int, ctypes.c_int]

# Chamar a função
resultado = atividade_dll.soma(10, 37)
print(f"Resultado da soma: {resultado}")
