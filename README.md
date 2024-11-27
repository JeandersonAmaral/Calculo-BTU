
# Dimensionar Ar Condicionado

- Projeto desenvolvido para a disciplina de Fenomenos do transporte do curso de Eng. de Software | UniVassouras.
- Professora: Ana Carolina

## Alunos
- Tássia Nascimento | 202212166
- Mateus Chagas | 202212170
- José Renan Marins|202211065
- Jeanderson Amaral | 202211161
- Tamyres Lopes | 202211177

## Funcionalidades Principais
- Cadastro de ambientes com dimensões e características térmicas.
- Adição de camadas de materiais para cálculo de resistência térmica.
- Cálculo de fluxo de calor, resistência total e BTUs necessários para climatização.
- Listagem e edição de ambientes cadastrados.

## Tecnologias Utilizadas
- **Python 3.9+**
- **Django 4.2**
- **SQLite** (banco de dados padrão para desenvolvimento)
- **TailwindCSS** (estilização do front-end)

## Estrutura do Projeto
- **`calculos_ar_condicionado/`**: Aplicativo principal com lógica para cálculos térmicos.
  - **`models.py`**: Define os modelos `Ambiente` e `Camada` com métodos para cálculos térmicos.
  - **`views.py`**: Implementa as funcionalidades de criação, edição e listagem de ambientes.
  - **`templates/`**: Contém páginas HTML estilizadas com TailwindCSS.
  - **`static/`**: Scripts JavaScript para formulários dinâmicos.

## Configuração Inicial
1. Clone o repositório:
   ```bash
   git clone https://github.com/JeandersonAmaral/Calculo-BTU
   cd projeto-ar-condicionado
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. Configure o banco de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```

## Uso
### Cadastro de Ambiente
1. Acesse a página inicial do projeto.
2. Clique em "Novo Ambiente".
3. Preencha as informações do ambiente e adicione camadas.
4. Salve para calcular automaticamente resistência térmica e BTUs.

### Listagem e Edição
- Veja todos os ambientes cadastrados na página principal.
- Clique em "Editar" para modificar um ambiente existente.

## Estrutura dos Cálculos
### Variáveis Principais
#### No modelo `Ambiente`
- **`comprimento`, `largura`, `altura`**: Dimensões do ambiente, usadas para calcular área e volume.
- **`temperatura_interna`, `temperatura_externa`**: Temperaturas para calcular o fluxo de calor.
- **`quantidade_de_pessoas`, `quantidade_de_lampadas`, `quantidade_de_eletronicos`**: Quantidade de fontes de calor que contribuem para o cálculo de BTUs.
- **Métodos**:
  - `pessoas()`: Calor gerado por pessoas (800 unidades por pessoa).
  - `lampadas()`: Calor gerado por lâmpadas (100 unidades por lâmpada).
  - `eletronicos()`: Calor gerado por eletrônicos (1000 unidades por aparelho).
  - `fluxo_de_calor()`: Baseado na diferença de temperatura e resistência térmica.
  - `btus()`: Converte o fluxo de calor total em BTUs.

#### No modelo `Camada`
- **`material`**: Nome do material isolante.
- **`espessura`**: Espessura da camada, usada no cálculo da resistência térmica.
- **`condutividade`**: Propriedade térmica do material, usada no cálculo de resistência.
- **Métodos**:
  - `calcular_resistencia()`: Calcula a resistência térmica de uma camada.

### Cálculos
- **Fluxo de Calor**: 
  - Fórmula: \( 	ext{Fluxo de Calor} = rac{	ext{Área} 	imes (	ext{Temp. Externa} - 	ext{Temp. Interna})}{	ext{Resistência Total}} \)
- **BTUs**: Conversão direta do fluxo de calor total para determinar a capacidade do ar condicionado:
  - \( 	ext{BTUs} = 	ext{Fluxo de Calor Total} 	imes 3.96 \)

## Contribuição
1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Envie um pull request com as alterações.

## Licença
Projeto sob [licença MIT](LICENSE).
