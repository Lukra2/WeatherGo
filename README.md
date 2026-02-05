# 🌦️ WeatherGO

WeatherGO é uma aplicação web que permite consultar condições meteorológicas em tempo real de forma simples, rápida e intuitiva. O projeto foi desenvolvido com foco em aprendizado prático de desenvolvimento full stack, utilizando **Python com FastAPI no backend**, renderização dinâmica com **Jinja2**, e construção da interface com **HTML, CSS e JavaScript**, integrando dados externos através da **API OpenWeatherMap**.

---

## 🔗 [Acesse o projeto](https://weathergo.lukra.work)

## 🚀 Demonstração

> Consulte informações meteorológicas como temperatura, umidade, clima atual e outras métricas de qualquer cidade suportada pela OpenWeatherMap.

---

## 🧰 Tecnologias Utilizadas

### 🔙 Backend
- **Python**
- **FastAPI**
- **Jinja2 (Template Engine)**
- **Library Requests (para consumo da API externa)**

### 🔜 Frontend
- **HTML5**
- **CSS3**
- **JavaScript**

### 🌐 Integrações
- **OpenWeatherMap API** – Fornece dados meteorológicos em tempo real

---

## 📂 Estrutura do Projeto

WeatherGO/
│
├── app/
│ ├── main.py # Inicialização da aplicação FastAPI
│ ├── routes/ # Rotas da aplicação
│ ├── templates/ # Templates HTML (Jinja2)
│ └── static/ # CSS, JavaScript e assets
│
├── requirements.txt
├── requirements-lock.txt
└── README.md


---

## ⚙️ Funcionalidades

- 🔍 Busca de clima por cidade
- 🌡️ Exibição de temperatura atual
- ☁️ Informações sobre condição climática
- 💧 Dados de umidade e outros indicadores
- 📄 Renderização dinâmica das páginas usando templates
- ⚡ Respostas rápidas utilizando FastAPI

---

## 🔌 Integração com OpenWeatherMap

O WeatherGO consome dados meteorológicos através da API pública da OpenWeatherMap.

Para utilizar o projeto, é necessário obter uma chave de API gratuita:

👉 https://openweathermap.org/api

---

## 🛠️ Instalação e Execução

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/lukra2/weathergo.git
cd weathergo
```
### 2️⃣ Crie um ambiente virtual
```bash
python -m venv venv
```
### Ativação:

Windows:

```bash
venv\Scripts\activate
```
Linux / Mac:
```bash
source venv/bin/activate
```
### 3️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```
### 4️⃣ Configure a API Key
Crie uma variável de ambiente:
```bash
OPENWEATHER_TOKEN=SuaChaveAqui
```
Ou configure diretamente no projeto (não recomendado para produção).

### 5️⃣ Execute o servidor
```bash
uvicorn app.main:app --reload
```
Acesse no navegador:

http://127.0.0.1:8000

## 📚 Objetivos do Projeto
Este projeto foi desenvolvido para:

Praticar desenvolvimento backend com FastAPI

Aplicar conceitos de segurança com Environment Variables e CORS

Explorar renderização server-side com Jinja2

Integrar APIs externas

Trabalhar organização e arquitetura de projetos web

Desenvolver habilidades full stack

## 🔮 Melhorias Futuras
📱 Responsividade aprimorada

🌎 Detecção automática de localização

📊 Exibição de mais informações climáticas

🎨 Melhorias visuais e animações

## 👨‍💻 Autor
Desenvolvido por Lucas Américo

GitHub: https://github.com/lukra2

LinkedIn: https://www.linkedin.com/in/lucas-américo-14016732a/

Portfólio: Em desenvolvimento

## 📄 Licença
Este projeto está sob a licença MIT.
Sinta-se livre para usar, estudar e modificar.

---