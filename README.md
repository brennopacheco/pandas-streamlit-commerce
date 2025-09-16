# 📊 Projeto de Análise e Simulação de Compras  

Este projeto utiliza **Python + Streamlit + Pandas** para simular e analisar dados de compras, permitindo a visualização interativa de relatórios, dashboards e tabelas dinâmicas.  

## 🚀 Funcionalidades  

- **Geração de dados simulados**  
  - `gera_dataset.py` cria datasets de compras, lojas e produtos com informações realistas.  

- **Adição de novas compras**  
  - `adicionando_linhas.py` permite inserir novas compras em tempo real via interface Streamlit.  

- **Visualização interativa**  
  - `visualizando.py` exibe o dataset completo.  
  - `selecionando_colunas.py` permite selecionar colunas e aplicar filtros.  

- **Análise de dados**  
  - `tabela_dinamica.py` gera tabelas dinâmicas personalizadas para análise de métricas como preço e comissão.  
  - `volume_dados.py` apresenta métricas de vendas por período, loja e vendedor.  

## 📂 Estrutura do Projeto  

├── datasets/ # Arquivos gerados pelo script gera_dataset.py  
│ ├── compras.csv  
│ ├── lojas.csv  
│ ├── produtos.csv  
├── adicionando_linhas.py # Adiciona novas compras via Streamlit  
├── gera_dataset.py # Gera datasets simulados  
├── requirements.txt # Dependências do projeto  
├── selecionando_colunas.py # Filtros e seleção de colunas  
├── tabela_dinamica.py # Análise com tabelas dinâmicas  
├── visualizando.py # Exibe dataset completo  
├── volume_dados.py # Dashboard de métricas  


## 🛠️ Tecnologias  

- Python 3.12+  
- [Streamlit](https://streamlit.io/)  
- Pandas  
- NumPy  
- OpenPyXL  
- Names (para geração de nomes aleatórios)  

## 📦 Instalação  

Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
````

## Crie e ative um ambiente virtual (opcional):
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows


## Instale as dependências:
````pip install -r requirements.txt````


▶️ Como Executar

- Gerar os datasets iniciais
````python gera_dataset.py````

- Rodar qualquer aplicação Streamlit
````streamlit run volume_dados.py````
ou
````streamlit run tabela_dinamica.py````

- Acesse no navegador:
````http://localhost:8501````


📊 Exemplos de Uso

Visualizar todas as compras:
````streamlit run visualizando.py````


Inserir novas compras:
````streamlit run adicionando_linhas.py````


Gerar relatórios dinâmicos:
````streamlit run tabela_dinamica.py````



👨‍🏫 Autor e Créditos
Este código foi desenvolvido pelo Professor Rodrigo Macedo e faz parte do curso:  
👉 [Análise de Dados com Python e Pandas (Udemy)](https://www.udemy.com/course/analise-de-dados-com-python-e-pandas/learn/lecture/47766333#overview)
