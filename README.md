# 🛰️ Asteroids Game em Python

Projeto de jogo **Asteroids** desenvolvido em **Python** com **Pygame**, baseado no curso:

- 🔗 [Build Asteroids in Python – Boot.dev](https://www.boot.dev/courses/build-asteroids-python)

Este repositório acompanha a implementação proposta no curso, com adaptações pessoais no código e na organização do projeto.

---

## 🚀 Tecnologias Utilizadas

- 🐍 **Python 3**
- 🎮 **Pygame**
- 📝 **Boot.dev** (como guia de aprendizado)

---

## 🎯 Funcionalidades Principais

- Controle da nave com teclado (rotação e movimento)
- Sistema de tiros com cooldown (limite de disparos por segundo)
- Asteroides com movimento baseado em vetores (`pygame.math.Vector2`)
- Detecção de colisões usando círculos ([CircleShape](cci:2://file:///c:/Users/anasb/GIT/asteroids-game/circleshape.py:3:0-25:53)):
  - Nave × asteroides → evento `player_hit`
  - Tiro × asteroides → evento `asteroid_shot`
- Asteroides que se dividem em pedaços menores (`asteroid_split`)
- Registro de estado e eventos do jogo em arquivos `.jsonl` via [logger.py](cci:7://file:///c:/Users/anasb/GIT/asteroids-game/logger.py:0:0-0:0)

---

## ▶️ Como Rodar o Projeto

1. Clone o repositório:

   ```bash
   git clone [https://github.com/SEU-USUARIO/asteroids-game.git](https://github.com/SEU-USUARIO/asteroids-game.git)
   cd asteroids-game
2. Crie e ative um ambiente virtual:
bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows (PowerShell / CMD)
.venv\Scripts\activate
Instale as dependências (se existir requirements.txt):
bash
pip install -r requirements.txt
Execute o jogo:
bash
python main.py

## 🕹️ Controles
A / D → girar a nave
W / S → acelerar / ré
SPACE → atirar
Fechar a janela → sair do jogo

## 🧠 Sobre o Curso
Este projeto foi desenvolvido com base no curso da Boot.dev:

“Build Asteroids in Python” – https://www.boot.dev/courses/build-asteroids-python*

Principais conceitos praticados:

Programação orientada a objetos em Python
Uso de vetores com pygame.math.Vector2
Game loop (atualização 
update
 e desenho 
draw
)
Grupos de sprites do Pygame (pygame.sprite.Group)
Detecção de colisão simples baseada em círculos
🏷️ Tags / Keywords
python
pygame
game-dev
asteroids
boot.dev
2d-game
tutorial
learning-project
arcade
space-shooter
## 📜 Licença
Projeto criado para fins de estudo.
Sinta-se à vontade para clonar, modificar e usar como base para seus próprios experimentos com desenvolvimento de jogos em Python.