% Tempo
N = [100, 200, 1000];
Tempo_busca_cubica = [0.05364220000046771, 0.34266520000528544, 663.1564822];

% Converta o tempo de execução de segundos para minutos
Tempo_busca_cubica_minutos = Tempo_busca_cubica / 60;

% Plotar o gráfico de tempo de execução para busca_cubica
figure;
semilogx(N, Tempo_busca_cubica_minutos, '-o', 'LineWidth', 2);
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


% Memória gasta
N = [100, 200, 1000];
Memoria_busca_cubica = [208, 144, 316];

% Plotar o gráfico de memória utilizada para busca_cubica
figure;
semilogx(N, Memoria_busca_cubica, '-o', 'LineWidth', 2);
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

