# 🎮 Jogo de Adivinhação em Python

Este projeto é um **jogo de adivinhação de números** desenvolvido em Python, com foco na aplicação de conceitos de **Programação Orientada a Objetos (POO)** como:

- Abstração  
- Encapsulamento  
- Herança  
- Polimorfismo  

---

## 📌 Como funciona

O jogo escolhe um número aleatório entre **1 e 100**, e o jogador deve tentar adivinhar dentro de um número limitado de tentativas, dependendo da dificuldade escolhida.

### 🎯 Níveis de dificuldade:
- **Fácil** → 15 tentativas  
- **Médio** → 10 tentativas  
- **Difícil** → 5 tentativas  

---

## 🧠 Funcionalidades

- Sistema de jogador com nome e pontuação  
- Sistema de ranking (placar geral)  
- Tratamento de erros (entrada inválida)  
- Pontuação baseada no desempenho  
- Suporte a múltiplos jogadores  
- Código modular e reutilizável  

---

## 🏗️ Estrutura do Código

### 🔹 `GameBase` (Classe Abstrata)
Define o modelo base para qualquer jogo:
- `iniciar()`
- `jogar()`

---

### 🔹 `Player`
Representa o jogador:
- Nome (privado)
- Pontuação (privada)
- Métodos para acessar e adicionar pontos

---

### 🔹 `RankingSistema`
Responsável por:
- Armazenar jogadores
- Ordenar por pontuação
- Exibir o ranking geral

---

### 🔹 `GuessGame`
Classe principal do jogo:
- Gera número aleatório
- Controla tentativas
- Define dificuldade
- Calcula pontuação

---

### 🔹 `rodar_partida`
Função que executa o jogo usando **polimorfismo**

---

### 🔹 `main`
Controla o fluxo do programa:
- Criação de jogadores
- Execução das partidas
- Exibição do ranking
- Loop do jogo

---

python jogo.py

---


## ⚙️ Como executar

1. Certifique-se de ter o Python instalado (3.x)
2. Salve o código em um arquivo, por exemplo:

---

## 🧮 Sistema de Pontuação

A pontuação é calculada com base nas tentativas restantes:

---

Quanto mais rápido acertar, mais pontos você ganha!

---

## 💡 Conceitos aplicados

- **Abstração:** Classe `GameBase`
- **Encapsulamento:** atributos privados em `Player`
- **Herança:** `GuessGame` herda de `GameBase`
- **Polimorfismo:** função `rodar_partida()`
- **Funções lambda:** ordenação do ranking

---

## 🚀 Possíveis melhorias

- Interface gráfica (Tkinter ou PyQt)
- Salvar ranking em arquivo (JSON ou banco de dados)
- Multiplayer online
- Sistema de níveis progressivos

---

## 👨‍💻 Autor

Projeto desenvolvido para fins de estudo em **Ciência da Computação**.
