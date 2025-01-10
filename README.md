# Calculadora Científica com Tkinter

Este projeto é uma calculadora científica desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. A calculadora suporta operações matemáticas básicas e avançadas, incluindo funções trigonométricas, logarítmicas e operações com constantes como π (pi) e **e** (número de Euler).

## Funcionalidades

- Operações básicas: soma, subtração, multiplicação e divisão.
- Operações avançadas:
  - Seno, cosseno e tangente (em graus).
  - Logaritmo comum (base 10) e logaritmo natural (ln).
  - Potenciação e raiz quadrada.
  - Alternância de sinal (+/-).
  - Porcentagem.
- Suporte a parênteses para controle da precedência de operações.
- Constantes matemáticas: π (pi) e **e** (número de Euler).
- Botão "C" para limpar a entrada.
- Botão "=" para calcular o resultado.

## Estrutura do Código

O código é composto por uma classe `Calculator`, que gerencia a interface gráfica e a lógica de cálculo. As principais partes incluem:

1. **Criação da Interface Gráfica**:
   - Entrada de texto (`tk.Entry`) para exibir a expressão e o resultado.
   - Botões organizados em uma grade (`tk.Button`) para representar os números, operadores e funções.

2. **Manipulação de Eventos**:
   - Cada botão tem um comportamento associado que é gerenciado pelo método `handle_button_click`.

3. **Operações Especiais**:
   - O cálculo de funções trigonométricas (seno, cosseno e tangente) utiliza graus.
   - O botão "^" permite a entrada de expoentes.
   - Tratamento de erros durante os cálculos para evitar falhas no programa.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina (versão 3.6 ou superior).
2. Salve o código em um arquivo chamado `calculadora.py`.
3. Execute o arquivo no terminal com o comando:

   ```bash
   python calculadora.py
