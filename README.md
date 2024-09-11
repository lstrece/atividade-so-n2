# Atividade Sistemas Operacionais

## Descrição
 A atividade consiste em criar um programa em uma linguagem, exportar esse código para DLL e, então, importá-lo em outra linguagem.

 Para realizar essa atividade, foram utilizadas as linguagem C++, como a liguagem de origem da DLL, Python como a linguagem para importar a DLL e o prompt de comando do Visual Studio para exportar em DLL.

## Passo a passo
1. **Programa em C++**  
    - Escreva um programa em C++ com uma ou mais funções que serão exportadas em DLL. A seguir, o código utilizado:
    ```
    #include <windows.h>

    extern "C" __declspec(dllexport) int soma(int a, int b) {
        return a + b;
    }
    ```
2. **Exportar para DLL**
    - No menu de pesquisa do Windows, digite **x64 Native Tools Command Prompt for VS**. Utilizando esse prompt, a DLL será gerada para arquitetura 64 bits.

    - Vá até a pasta onde está o código em C++ com o seguinte comando:
    ```
    cd C:\caminho\da\sua\pasta
    ```

    - Utilize o seguinte comando para exportar o código C++ para DLL:
    ```
    cl /LD seu_arquivo.cpp /Fe:seu_arquivo.dll
    ```
3 **Importar em Python**
    - Escreva um programa em python que importe as funções da DLL. Para o código em C++ anterior, foi utilizado o seguinte código Python:
    ```
    import ctypes

    # Carregar a DLL
    atividade_dll = ctypes.CDLL('./atividade.dll')

    # Definir o tipo de retorno e os tipos de argumentos da função
    atividade_dll.soma.restype = ctypes.c_int
    atividade_dll.soma.argtypes = [ctypes.c_int, ctypes.c_int]

    # Chamar a função
    resultado = atividade_dll.soma(10, 37)
    print(f"Resultado da soma: {resultado}")
    ```