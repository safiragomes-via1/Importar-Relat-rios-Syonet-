# Automação de Relatório — Syonet / ViasulRoute (Selenium)

Este projeto automatiza o login e a navegação no portal **Syonet/ViasulRoute** para abrir o relatório **`[ VENDAS ] - KPI - Fluxo de Loja - Diário`**, aplicar filtros específicos e preparar a visualização do dashboard, utilizando **Python + Selenium** e **webdriver-manager**.

> ⚠️ **Aviso**: Este script é apenas um exemplo educacional. Certifique-se de ter autorização para automatizar o portal e de seguir os **Termos de Uso** do sistema e as políticas internas da sua empresa. Não armazene credenciais em texto plano em repositórios públicos.

---

## ✨ O que o script faz

1. **Configura o Chrome** (desativa infobars, extensões, popups e inicia maximizado).
2. **Abre o portal** de login do Syonet/ViasulRoute.
3. **Realiza o login** (usuário/senha devem ser inseridos pelo usuário).
4. **Navega** até o menu **Gestão → Dashboard**.
5. **Entra no iFrame** do dashboard.
6. **Pesquisa** pelo relatório: **`[ VENDAS ] - KPI - Fluxo de Loja - Diário`**.
7. **Abre o relatório** e **aplica filtros**:
   - Tipo de venda: *venda direta*
   - Tipo de evento: desmarca **Todos**, marca **Novos web** e **Novos web Facebook**
   - Empresa: desmarca **Marcar Todos**, marca **Bajaj**
   - Período: do **1º dia do mês atual** até **hoje**
8. **Aplica o filtro** e aguarda a renderização.

---

## 🧩 Requisitos

- Python 3.9+
- Google Chrome instalado
- Pacotes Python:
  - `selenium`
  - `webdriver-manager`
  - `pandas` (opcional, já está importado)
  - (Opcional) `python-dotenv` para gerenciar variáveis de ambiente
- Um módulo `logger.py` com a função `logg()` (ou ajuste o código para o logger de sua preferência)

Instalação rápida:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows PowerShell

pip install -U pip
pip install selenium webdriver-manager pandas python-dotenv
```

> Se você não pretende usar `.env`, pode **remover** `python-dotenv` e apenas manter os demais.

---

## 📁 Estrutura sugerida do projeto

```
.
├─ src/
│  ├─ main.py              # Script principal (o seu código)
│  ├─ logger.py            # Seu utilitário de logging (ex.: retorna um objeto logger)
│  └─ requirements.txt     # Dependências (opcional)
├─ .env                    # Credenciais (NÃO COMMITAR em repositório público)
├─ README.md
└─ .gitignore
```

Exemplo de `.gitignore` (recomendado):

```
.venv/
__pycache__/
*.log
.env
chromedriver*
```

---

## 🔐 Configuração de credenciais

O código de exemplo preenche os campos de **usuário** e **senha** diretamente. Recomenda‑se **não** versionar credenciais. Duas opções:

### Opção A — Inserir manualmente (mais simples)
Edite as linhas do login e insira seu usuário e senha **localmente**:
```python
# Login no site
WebDriverWait(nav, 30).until(EC.visibility_of_element_located((By.XPATH, 'XPATH_USUARIO'))).send_keys('SEU_USUARIO')
nav.find_element(By.XPATH,'XPATH_SENHA').send_keys('SUA_SENHA')
```

### Opção B — Usar variáveis de ambiente (recomendado)
No seu `.env`:
```
SYONET_USER=seu_usuario
SYONET_PASS=sua_senha
```

No código (exemplo):
```python
from dotenv import load_dotenv
load_dotenv()
user = os.getenv("SYONET_USER")
pwd  = os.getenv("SYONET_PASS")
```

---

## ▶️ Como executar

1. Configure o ambiente (dependências e credenciais).
2. Garanta que o **Chrome** está instalado.
3. Rode o script:

```bash
python src/main.py
```

> O `webdriver-manager` cuidará do download/gestão do `chromedriver` compatível com sua versão do Chrome.

---

## 🧠 Notas sobre o código (trechos importantes)

- **Opções do Chrome**: desativa infobars, extensões e popups, e inicia maximizado.
  ```python
  options = Options()
  options.add_argument("disable-infobars")
  options.add_argument("--disable-extensions")
  options.add_argument("disable-popup-blocking")
  options.add_argument("start-maximized")
  ```

- **Driver com webdriver-manager**: evita baixar o ChromeDriver manualmente.
  ```python
  driver_path = ChromeDriverManager().install()
  service = Service(driver_path)
  nav = webdriver.Chrome(service=service, options=options)
  ```

- **Espera explícita (WebDriverWait)**: torna a automação mais estável ao aguardar elementos ficarem visíveis/clicáveis.
  ```python
  WebDriverWait(nav, 30).until(EC.visibility_of_element_located((By.XPATH, "XPATH")))
  ```

- **iFrame**: é necessário mudar o contexto antes de interagir com elementos dentro dele.
  ```python
  WebDriverWait(nav, 30).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div/iframe')))
  ```

- **Datas dinâmicas**: início do mês atual e data de hoje.
  ```python
  dataAtual = datetime.now().strftime("%d/%m/%Y")
  dataInicio = datetime.now().strftime("01/%m/%Y")
  ```

- **Logger**: o script usa `from logger import *` e `logg()`. Tenha um `logger.py` como:
  ```python
  # src/logger.py (exemplo simples)
  from loguru import logger

  def logg():
      logger.add("app.log", rotation="10 MB")
      return logger
  ```

---

## 🛠️ Dicas e ajustes comuns

- **Headless (rodar sem abrir janela do navegador)**:
  ```python
  options.add_argument("--headless=new")  # Chrome 109+
  options.add_argument("--window-size=1920,1080")
  ```

- **XPaths frágeis**: XPaths absolutos (ex.: `/html/body/...`) podem quebrar com mudanças no layout. Se possível, prefira seletores mais **estáveis** (por `id`, `name`, `data-testid` ou `//a[contains(., 'texto')]`).

- **Timeouts**: aumente o tempo do `WebDriverWait` ou adicione novas condições de espera se a página for lenta.

- **Erros de versão do Chrome/driver**: o `webdriver-manager` geralmente resolve, mas se falhar, atualize o Chrome ou limpe o cache do manager:
  ```bash
  pip install -U webdriver-manager
  ```

---

## 📦 requirements.txt (opcional)

```
selenium>=4.21.0
webdriver-manager>=4.0.1
pandas>=2.0.0
python-dotenv>=1.0.0
loguru>=0.7.2
```

Instale com:
```bash
pip install -r src/requirements.txt
```

---

## 🧪 Roadmap (ideias de melhoria)

- Exportar dados do relatório (após aplicar filtros) para CSV/Excel com `pandas`.
- Parametrizar filtros via **CLI** (`argparse`) ou **.env**.
- Implementar **tratamento de exceções** com screenshots automáticos em falhas.
- Pipeline **CI** (GitHub Actions) para lint/test.
- Rodar em contêiner **Docker** com Chrome headless.

---

## 📜 Licença

Defina a licença do projeto (ex.: MIT, Apache-2.0).

---

## 🖼️ Screenshot (opcional)

Inclua imagens do dashboard/relatório (sem dados sensíveis) para facilitar a compreensão dos passos.

---

## ❗ Termos de uso / Compliance

- Obtenha autorização para automatizar sistemas de terceiros.
- Respeite políticas de **privacidade** e **segurança**.
- **Nunca** exponha credenciais em repositórios públicos.
