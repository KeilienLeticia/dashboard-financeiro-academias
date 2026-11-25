# dCalendario - tabela calendário para Power BI (Obter dados > Script Python)
# Requer: pandas (pip install pandas matplotlib)
# Ajuste o período abaixo conforme as datas de fLancamentos / fOrcamento.
import pandas as pd

DATA_INICIO = "2026-01-01"
DATA_FIM = "2026-12-31"

MESES = ["jan", "fev", "mar", "abr", "mai", "jun",
         "jul", "ago", "set", "out", "nov", "dez"]
MESES_NOME = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]

datas = pd.date_range(DATA_INICIO, DATA_FIM, freq="D")
dCalendario = pd.DataFrame({"Data": datas})

dCalendario["Ano"] = dCalendario["Data"].dt.year
dCalendario["Nº Mês"] = dCalendario["Data"].dt.month
dCalendario["Mês"] = dCalendario["Nº Mês"].map(lambda m: MESES[m - 1])
dCalendario["Mês Nome"] = dCalendario["Nº Mês"].map(lambda m: MESES_NOME[m - 1])
dCalendario["Ano-Mês"] = dCalendario["Data"].dt.strftime("%Y-%m")
dCalendario["Mês/Ano"] = dCalendario["Mês"] + "/" + dCalendario["Ano"].astype(str)
dCalendario["Início do Mês"] = dCalendario["Data"].dt.to_period("M").dt.to_timestamp()
dCalendario["Trimestre"] = "T" + dCalendario["Data"].dt.quarter.astype(str)
dCalendario["Semestre"] = "S" + ((dCalendario["Nº Mês"] - 1) // 6 + 1).astype(str)
dCalendario["Dia"] = dCalendario["Data"].dt.day
dCalendario["Nº Dia Semana"] = dCalendario["Data"].dt.dayofweek + 1  # 1 = segunda
dCalendario["Dia Semana"] = dCalendario["Data"].dt.dayofweek.map(lambda d: DIAS[d])
dCalendario["Semana ISO"] = dCalendario["Data"].dt.isocalendar().week.astype(int)
dCalendario["Fim de Semana"] = dCalendario["Nº Dia Semana"] >= 6
dCalendario["Dia Útil"] = ~dCalendario["Fim de Semana"]
