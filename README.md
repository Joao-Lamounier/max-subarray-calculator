# Documentação para o Projeto - Algoritmo de Subarray Máximo por Divisão e Conquista

## Introdução

O código fornecido implementa uma solução para o problema clássico do subarray máximo em um array unidimensional. A abordagem utilizada é baseada no paradigma de divisão e conquista, que divide o problema em subproblemas menores, resolve-os recursivamente e, em seguida, combina suas soluções para obter a solução global.

## Funções Principais

### 1. Função `set_sum`

Esta função é responsável por calcular a soma de um subarray específico. Ela percorre o subarray definido pelos parâmetros `start`, `end` e `step`, calculando a soma dos elementos.

- `start`: Índice de início do subarray.
- `end`: Índice de término do subarray.
- `step`: Passo de iteração para percorrer o subarray.
- `arr`: Array de entrada.

### 2. Função `max_subarray_divide_conquer`

Esta é a função principal que implementa o algoritmo de divisão e conquista para encontrar o subarray máximo. Ela divide o array na metade, resolve recursivamente os subarrays esquerdo e direito, e depois combina as soluções.

- `arr`: Array de entrada.
- `low`: Índice de início do subarray.
- `high`: Índice de término do subarray.

## Paradigma de Divisão e Conquista

O algoritmo segue a abordagem clássica de divisão e conquista:

1. **Divisão:** O array é dividido ao meio, criando dois subarrays menores.
2. **Conquista:** Os subarrays são resolvidos recursivamente para encontrar a solução ótima.
3. **Combinação:** As soluções dos subarrays são combinadas para encontrar a solução global.

## Detalhes da Implementação

- **Divisão:**
  - O array é dividido ao meio no ponto médio (`mid`).
  
- **Conquista:**
  - Duas chamadas recursivas são feitas para os subarrays esquerdo e direito.
  
- **Combinação:**
  - A solução do subarray máximo pode ser:
    - O máximo encontrado no subarray esquerdo.
    - O máximo encontrado no subarray direito.
    - A soma máxima que atravessa o ponto médio (`cross_max`).
##Conclusão
O algoritmo de subarray máximo por divisão e conquista oferece uma abordagem eficiente para resolver esse problema clássico. No entanto, é importante notar que, em termos de complexidade de tempo, a solução ainda é O(n log n), onde n é o tamanho do array.
