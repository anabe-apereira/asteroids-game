# 🛰️ Asteroids Game em Python

Projeto do jogo **Asteroids** desenvolvido em **Python** com **Pygame**, baseado no curso:

- 🔗 [Build Asteroids in Python – Boot.dev](https://www.boot.dev/courses/build-asteroids-python)

Este repositório acompanha a implementação do curso, com adaptações pessoais no código e na estrutura do projeto.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3**
- 🎮 **Pygame**
- 📝 **Boot.dev** (como guia de aprendizado)

---

## 🎯 Funcionalidades Principais

- Controle da nave por teclado (rotação e movimento)
- Sistema de tiros com cooldown (limite de disparos por segundo)
- Asteroides com movimento vetorial (`pygame.math.Vector2`)
- Detecção de colisões usando círculos:
  - Nave × Asteroides → evento `player_hit`
  - Tiro × Asteroides → evento `asteroid_shot`
- Asteroides se dividem em partes menores (`asteroid_split`)
- Registro de estado/eventos do jogo em `.jsonl` via `logger.py`

---

## ▶️ Como Rodar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/asteroids-game.git
cd asteroids-game
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv

# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell / CMD)
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o jogo

```bash
python main.py
```

---

## 🕹️ Controles

| Tecla | Ação |
|-------|------|
| **A / D** | Girar a nave |
| **W / S** | Acelerar / Ré |
| **SPACE** | Atirar |
| **Fechar janela** | Sair do jogo |

---

## 🧠 Sobre o Curso

O projeto foi desenvolvido com base no curso:

**“Build Asteroids in Python” – Boot.dev**

Principais conceitos praticados:

- Programação orientada a objetos em Python  
- Uso de vetores com `pygame.math.Vector2`  
- Game loop (`update` e `draw`)  
- Sprites e grupos (`pygame.sprite.Group`)  
- Detecção de colisão com círculos  

---

## 🏷️ Tags / Keywords

`python` `pygame` `game-dev` `asteroids` `boot.dev` `2d-game`  
`tutorial` `learning-project` `arcade` `space-shooter`

---

## 📜 Licença

Projeto criado para fins de estudo.  
Sinta-se à vontade para clonar, modificar e usar como base para seus próprios experimentos com desenvolvimento de jogos em Python.
