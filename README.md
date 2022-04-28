# etl_dados_historicos_B3

Projeto de ETL criado para uso dos dados históricos fornecidos pela B3

Os arquivos fornecidos são em formato txt sem separador.

- Ao executar o script o mesmo irá pegar todos os arquivos TXT do diretório [data]
- Irá fazer o ETL e retornará um novo arquivo em formato CSV concatenando todos os arquivos TXT.

[Dados_historicos_B3](https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/cotacoes-historicas/).

[Layout_dados](https://www.b3.com.br/data/files/33/67/B9/50/D84057102C784E47AC094EA8/SeriesHistoricas_Layout.pdf).

## Tecnologias 📚

- Python 3.8.x
- Pandas

## Requisitos ✋

- Jupyter Notebook ou Jupyter Lab
- Python

## Instalação 💽

Realizar o Download dos dados Historicos de acordo com os anos de sua escolha é fornecido 1 arquivo para cada Ano.
Descompactar os arquivos dentro da pasta [data]

## Rodando a aplicação 🛸

Acesso o [Jupyter Notebook](http://localhost:8889/)
Acesso o [Jupyter Lab](http://localhost:8888/)

ou diretamente pelo python

```sh
python etl.py
```
