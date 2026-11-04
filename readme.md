## 1° Etapa - Modelagem da matriz de pesos
- 6 primeiros números: 510230
- Parametrizaão do com base no RA:
    - D1: 5
    - D2: 1
    - D3: 0
    - D4: 2
    - D5: 3
    - D6: 0

- O destino decidido com base em D6, sendo um número par, é S7


### Tabela de Pesos calculados com base no RA:

| Aresta | Ramal | Fórmula do Peso w(e) | Resultado |
|--------|-------|----------------------|-----------|
| e1 | (S0, S1) | w1 = 10 + (0 mod 5)  | 10 |
| e2 | (S0, S2) | w2 = 15 + (3 mod 7) | 18 |
| e3 | (S1, S2) | w3 = 8 + (2 mod 4) | 10 |
| e4 | (S1, S3) | w4 = 12 + (0 mod 6) | 12 |
| e5 | (S2, S4) | w5 = 14 + (1 mod 5) | 15 |
| e6 | (S2, S5) | w6 = 9 + (5 mod 6) | 14 |
| e7 | (S3, S4) | w7 = 7 + ((3 + D6) mod 5) | 10 |
| e8 | (S3, S6) | w8 = 11 + ((2 + D5) mod 6) | 16 |
| e9 | (S4, S5) | w9 = 6 + ((0 + D4) mod 4) | 8 |
| e10 | (S4, S7) | w10 = 16 + ((1 + D3) mod 7) | 17 |
| e11 | (S5, S7) | w11 = 18 + ((5 + D2) mod 8) | 24 |
| e12 | (S6, S7) | w12 = 9 + ((3 + D1) mod 5) | 12 |
| e13 | (S1, S4) | w13 = 20 + (0 mod 4) | 20 |


### Matrix de peso 8x8:
| | S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 |
|----|----|----|----|----|----|----|----|----|
| S0 | 0 | 10 | 18 | ∞ | ∞ | ∞ | ∞ | ∞ |
| S1 | 10 | 0 | 10 | 12 | 20 | ∞ | ∞ | ∞ |
| S2 | 18 | 10 | 0 | ∞ | 15 | 14 | ∞ | ∞ |
| S3 | ∞ | 12 | ∞ | 0 | 10 | ∞ | 16 | ∞ |
| S4 | ∞ | 20 | 15 | 10 | 0 | 8 | ∞ | 17 |
| S5 | ∞ | ∞ | 14 | ∞ | 8 | 0 | ∞ | 24 |
| S6 | ∞ | ∞ | ∞ | 16 | ∞ | ∞ | 0 | 12 |
| S7 | ∞ | ∞ | ∞ | ∞ | 17 | 24 | 12 | 0 |

### Simétria esparsidade:

| | S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 |
|----|----|----|----|----|----|----|----|----|
| S0 | - | Conectado | Conectado | ∞ | ∞ | ∞ | ∞ | ∞ |
| S1 | Conctado | - | Conectado | Conectado | Conectado | ∞ | ∞ | ∞ |
| S2 | Conectado | Conectado | - | ∞ | Conectado | Conectado | ∞ | ∞ |
| S3 | ∞ | Conectado | ∞ | - | Conectado | ∞ | Conectado | ∞ |
| S4 | ∞ | Conectado | Conectado | Conectado | - | Conectado | ∞ | Conectado |
| S5 | ∞ | ∞ | Conectado | ∞ | Conectado | - | ∞ | Conectado |
| S6 | ∞ | ∞ | ∞ | Conectado | ∞ | ∞ | - | Conectado |
| S7 | ∞ | ∞ | ∞ | ∞ | Conectado | Conectado | Conectado | - |

