<body>
    <h1>Automação de Cadastro de Produtos</h1>
    <p>Este projeto é um script em Python que automatiza o processo de cadastro de produtos em um sistema web. Ele utiliza a biblioteca <code>pyautogui</code> para simular ações do usuário (como cliques e digitação) e <code>pandas</code> para ler dados de um arquivo CSV. O script abre o navegador Chrome, acessa um site específico, faz login e preenche um formulário com informações de produtos lidas do CSV.</p>

  <h2>Funcionalidades</h2>
    <ul>
        <li><strong>Abertura do navegador</strong>: Abre o Chrome e navega para a página de login do sistema.</li>
        <li><strong>Login automático</strong>: Insere credenciais (email e senha) e faz login.</li>
        <li><strong>Leitura de dados</strong>: Carrega produtos de um arquivo CSV (<code>produtos.csv</code>).</li>
        <li><strong>Cadastro de produtos</strong>: Para cada linha do CSV, preenche os campos do formulário (código, marca, tipo, categoria, preço unitário, custo e observações) e submete.</li>
        <li><strong>Navegação</strong>: Rola a página após cada cadastro para continuar.</li>
    </ul>

  <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Python</strong>: Linguagem principal do script.</li>
        <li><strong>pyautogui</strong>: Para automação de interface gráfica (cliques, digitação e pressionamento de teclas).</li>
        <li><strong>pandas</strong>: Para leitura e manipulação do arquivo CSV.</li>
        <li><strong>time</strong>: Para pausas entre ações, garantindo que o navegador responda.</li>
    </ul>

  <h2>Pré-requisitos</h2>
    <ul>
        <li><strong>Python 3.x</strong> instalado.</li>
        <li>Bibliotecas necessárias: <code>pyautogui</code>, <code>pandas</code> e <code>time</code> (esta última é nativa).</li>
        <li>Arquivo CSV chamado <code>produtos.csv</code> com as colunas: <code>codigo</code>, <code>marca</code>, <code>tipo</code>, <code>categoria</code>, <code>preco_unitario</code>, <code>custo</code>, <code>obs</code>.</li>
        <li>Navegador Chrome instalado.</li>
        <li>Resolução de tela compatível (o script usa coordenadas específicas de mouse; ajuste se necessário).</li>
    </ul>

  <h2>Instalação e Como Usar</h2>
    <ol>
        <li><strong>Clone ou baixe o repositório</strong>:
            <pre><code>git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo</code></pre>
        </li>
        <li><strong>Instale as dependências</strong>:
            <pre><code>pip install pyautogui pandas</code></pre>
        </li>
        <li><strong>Prepare o arquivo CSV</strong>:
            <ul>
                <li>Coloque o arquivo <code>produtos.csv</code> no diretório do projeto (ou ajuste o caminho no código).</li>
                <li>Exemplo de estrutura do CSV:
                    <pre><code>codigo,marca,tipo,categoria,preco_unitario,custo,obs
001,Marca A,Tipo 1,1,10.50,8.00,Observação opcional
002,Marca B,Tipo 2,2,15.00,12.00,</code></pre>
                </li>
            </ul>
        </li>
        <li><strong>Execute o script</strong>:
            <ul>
                <li>Certifique-se de que o navegador não esteja em tela cheia e que a página esteja visível.</li>
                <li>Rode o comando:
                    <pre><code>python nome-do-script.py</code></pre>
                </li>
                <li>O script irá abrir o Chrome, fazer login e começar a cadastrar os produtos automaticamente.</li>
            </ul>
        </li>
    </ol>

  <h3>Avisos Importantes</h3>
    <ul>
        <li><strong>Coordenadas de mouse</strong>: As posições (x, y) são específicas para uma resolução de tela. Se o layout da página mudar ou sua tela for diferente, você precisará ajustar os valores usando <code>pyautogui.position()</code> para capturar novas coordenadas.</li>
        <li><strong>Segurança</strong>: Este script simula ações humanas, então use com cuidado. Evite rodá-lo em ambientes sensíveis ou com dados reais sem permissão.</li>
        <li><strong>Compatibilidade</strong>: Testado em Windows (devido aos caminhos no código). Para outros SO, ajuste os caminhos e comandos (ex.: <code>pyautogui.press("win")</code> pode não funcionar no Linux/Mac).</li>
        <li><strong>Pausas</strong>: O script inclui pausas (<code>time.sleep</code> e <code>pyautogui.PAUSE</code>) para evitar erros, mas ajuste conforme a velocidade da sua máquina/internet.</li>
    </ul>

  <h2>Estrutura do Projeto</h2>
    <ul>
        <li><code>script.py</code>: Arquivo principal com o código de automação.</li>
        <li><code>produtos.csv</code>: Arquivo de exemplo com dados dos produtos (não incluído; crie o seu).</li>
        <li><code>README.md</code>: Este arquivo de documentação.</li>
    </ul>

  <h2>Contribuição</h2>
    <p>Contribuições são bem-vindas! Se você quiser melhorar o script (ex.: adicionar validações, suporte a múltiplos navegadores ou tornar as coordenadas dinâmicas), faça um fork e envie um Pull Request.</p>

  <h2>Licença</h2>
    <p>Este projeto é de uso pessoal/educacional. Não há licença específica; sinta-se à vontade para usar e modificar.</p>

  <h2>Contato</h2>
    <ul>
        <li>Autor: [Seu Nome ou Usuário]</li>
        <li>Email: jrsilvablk@gmail.com (do código)</li>
        <li>GitHub: <a href="https://github.com/jrsilva-dev">Meu Perfil</a></li>
    </ul>
    <p>Se tiver dúvidas ou precisar de ajustes, abra uma issue no repositório!</p>
</body>
</html>
