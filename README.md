# README - Conversão de Notas

## Descrição

Este programa realiza a conversão de notas numéricas em conceitos, conforme o sistema de avaliação utilizado por uma professora do Ensino Médio. As notas são convertidas de acordo com uma tabela específica, onde cada nota numérica é mapeada para uma letra (A, B, C, D ou E).

## Tabela de Conversão

| Nota Numérica | Conceito |
|---------------|----------|
| 0             | E        |
| 1 a 35       | D        |
| 36 a 60      | C        |
| 61 a 85      | B        |
| 86 a 100      | A        |

## Entrada

A entrada consiste em um único número inteiro \(N\) (0 ≤ N ≤ 100), representando a nota do aluno no sistema numérico. O usuário deve inserir a nota diretamente.

## Saída

A saída é uma única letra representando o conceito correspondente à nota dada. O programa deve imprimir a letra em maiúsculas (A, B, C, D ou E).

## Exemplos de Entrada e Saída

| Exemplo de Entrada | Exemplo de Saída |
|--------------------|------------------|
| 0                  | E                |
| 12                 | D                |
| 45                 | C                |
| 75                 | B                |
| 90                 | A                |
| 100                | A                |

## Como Executar

1. Certifique-se de ter o Python 3.9 instalado em sua máquina.
2. Salve o código em um arquivo chamado `conversao_notas.py`.
3. Execute o programa no terminal ou prompt de comando:

   ```bash
   python conversao_notas.py
   ```

4. Insira a nota quando solicitado e pressione Enter.

## Observações

- O programa não aceita notas fora do intervalo de 0 a 100.
- O conceito 'E' é atribuído exclusivamente para a nota 0.
- As notas devem ser inseridas como inteiros.
