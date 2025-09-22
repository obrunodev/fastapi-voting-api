FastAPI Movie Voting API
Bem-vindo ao projeto! Este guia servirá como um checklist para você implementar as funcionalidades da API, passo a passo, aplicando os conceitos discutidos.

Checklist de Implementação
Fase 1: Configuração e Fundamentos
[ ] Configurar o ambiente de desenvolvimento com Docker e Docker Compose.

[ ] Criar a estrutura básica do projeto com FastAPI.

[ ] Conectar a API ao banco de dados PostgreSQL usando o ORM SQLAlchemy.

[ ] Implementar o padrão Singleton para a conexão com o banco de dados, garantindo que a aplicação tenha apenas uma única instância de sessão de banco de dados.

Fase 2: Autenticação e Modelagem
[ ] Modelar a tabela de Users e a tabela de Movies.

[ ] Modelar a tabela de Votes para registrar o voto de cada usuário.

[ ] Implementar os endpoints de registro (/signup) e login (/token) com geração de JWT.

[ ] Usar injeção de dependências para validar o token JWT em rotas protegidas.

Fase 3: Funcionalidades Principais
[ ] Criar um endpoint para listar todos os filmes.

[ ] Criar o endpoint de votação (/vote/{movie_id}). A lógica deve garantir que o usuário vote apenas uma vez por mês.

[ ] Usar async def e await nas operações que interagem com o banco de dados para garantir o assincronismo.

[ ] Adicionar um endpoint para listar os filmes mais votados, usando uma query otimizada para o PostgreSQL.

Fase 4: Padrões de Projeto e Otimização
[ ] Implementar a Background Task no endpoint de votação para enviar uma notificação (simulada) de "voto registrado com sucesso".

[ ] Adicionar cache (simulado) para o endpoint de filmes mais votados. Por exemplo, armazenar os resultados em uma variável global por 5 minutos antes de recalcular.

[ ] Refatorar queries complexas no PostgreSQL usando EXPLAIN ANALYZE e adicionar índices para garantir a performance.

[ ] Aplicar o padrão Adapter para simular a comunicação com uma API externa que lista os filmes. Crie uma classe intermediária que "traduza" o formato de dados da API externa para o formato que sua aplicação espera.

[ ] Implementar o padrão Factory para lidar com a criação de diferentes tipos de notificações (e-mail, SMS, etc.). A lógica de criação de cada tipo de notificação deve ser centralizada em uma única função ou classe.

[ ] Aplicar o padrão Observer para atualizar os resultados do ranking de filmes em tempo real. Crie um sistema onde o objeto de voto notifique os "observadores" (que podem ser os endpoints de resultados ou o serviço de cache) para que os dados sejam atualizados automaticamente.
