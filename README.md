
# Analema Solar

Este repositório contém um script Python que gera e plota o **analema solar**, ou seja, a curva em forma de “8” que o Sol forma no céu ao longo de um ano quando observado no mesmo horário todos os dias.

O analema é resultado da combinação entre a **inclinação do eixo da Terra** e a **variação da velocidade orbital** ao longo do ano.

---

## 📌 Visão Geral

O script calcula:

- **Equação do Tempo (Equation of Time)** — desvio temporal entre o tempo solar real e o tempo solar médio, causado pela órbita elíptica da Terra.
- **Declinação Solar (Solar Declination)** — ângulo entre os raios solares e o plano do equador terrestre ao longo do ano.

Com esses valores, o gráfico do analema é construído e exibido com cores representando o dia do ano.

---

## 🧪 Pré-requisitos

Antes de rodar o script, é necessário ter as seguintes bibliotecas Python instaladas:

```bash
pip install numpy matplotlib
````

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/vitor-souza-ime/analema.git
```

2. Acesse a pasta:

```bash
cd analema
```

3. Execute o script:

```bash
python main.py
```

Isso abrirá uma janela com o gráfico do analema solar.

---

## 📊 O que o Gráfico Mostra

* Eixo X: **Equação do Tempo** (minutos)
* Eixo Y: **Declinação Solar** (graus)
* Cada ponto representa um dia do ano, colorido de acordo com o número do dia.

O formato em “8” do analema aparece por causa da combinação da variação da velocidade orbital da Terra e da sua inclinação axial.

---

## 🧠 Porque o Analema Importa

O analema revela como o tempo solar verdadeiro difere do tempo solar médio ao longo do ano. Ele explica, por exemplo:

* Por que o meio-dia solar não bate com o relógio
* Por que os dias mais longos e curtos não ocorrem exatamente nos solstícios

---

## 🛠️ Estrutura do Projeto

```
analema/
│─ main.py                # Script principal para gerar o gráfico do analema
│─ README.md              # Documentação do projeto
```

---

## 📌 Possíveis Extensões

Você pode expandir esse projeto para:

✔ Gerar animações do analema para diferentes latitudes
✔ Salvar os dados em CSV
✔ Criar uma interface gráfica interativa
✔ Plotar analemas para diferentes horas locais

---

## 📝 Licença

Este projeto está disponível sob a **Licença MIT**.
Sinta-se livre para usar e modificar conforme sua necessidade!

---

## ✨ Autor

Vitor Souza — *Projeto pessoal de visualização astronômica*

