% Tempo
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000];
Tempo_busca_quadratica = [432100, 1081700, 353784800, 1651474200, 9585991600, 38227505000, 938509268800, 3765410517000];

% Converta o tempo de execução de nanossegundos para minutos
Tempo_busca_quadratica_minutos = Tempo_busca_quadratica / (60e6);

% Plotar o gráfico de linha de tempo de execução para busca_quadratica
figure;
semilogx(N, Tempo_busca_quadratica_minutos, '-o', 'LineWidth', 2);
xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Tempo de Execução (minutos)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Tempo de Execução', 'FontSize', 16); % Aumente o tamanho da fonte
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
set(gca, 'XScale', 'log'); % Configure a escala do eixo x para logaritmo
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Aumente o tamanho da fonte no gráfico
set(gca, 'FontSize', 12);

% Remova as grades
grid off;


% Memória
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000];
Memoria_busca_quadratica = [208, 144, 284, 284, 284, 284, 284, 284];

% Plotar o gráfico de memória utilizada para busca_quadratica
figure;
semilogx(N, Memoria_busca_quadratica, '-o', 'LineWidth', 2);
xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Memória Utilizada (bytes)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Memória Utilizada', 'FontSize', 16); % Aumente o tamanho da fonte
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
set(gca, 'XScale', 'log'); % Configure a escala do eixo x para logaritmo
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Aumente o tamanho da fonte no gráfico
set(gca, 'FontSize', 12);

% Remova as grades
grid off;

