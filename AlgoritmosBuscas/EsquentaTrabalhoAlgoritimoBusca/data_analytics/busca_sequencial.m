% Tempo
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000];
Tempo_v1 = [20300, 12000, 408800, 1489800, 3464900, 5116300, 29057800, 53667400, 260720000, 735215400, 3121597300, 5553537900, 54775155900];
Tempo_v2 = [10700, 8100, 9500, 20100, 16800, 14200, 15300, 16100, 15900, 20800, 17700, 66600, 36200];

% Plotar o gráfico de linha de tempo de execução para v1 e v2
figure;
semilogx(N, Tempo_v1, '-o', 'LineWidth', 2, 'DisplayName', 'busca\_sequencial\_v1');
hold on;
semilogx(N, Tempo_v2, '-o', 'LineWidth', 2, 'DisplayName', 'busca\_sequencial\_v2');

xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Tempo de Execução (nanossegundos)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Tempo de Execução', 'FontSize', 16); % Aumente o tamanho da fonte
legend('Location', 'northwest');
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Remova as grades
grid off;

% Aumente o tamanho da fonte nas legendas e no eixo
set(gca, 'FontSize', 12);
legend('FontSize', 12);

% Memória
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000];
Memoria_v1 = [176, 112, 188, 188, 188, 188, 188, 188, 188, 188, 188, 188, 188];
Memoria_v2 = [112, 112, 188, 188, 188, 188, 188, 188, 188, 188, 188, 188, 188];

% Plotar o gráfico de memória utilizada para v1 e v2
figure;
semilogx(N, Memoria_v1, '-o', 'LineWidth', 2, 'DisplayName', 'busca\_sequencial\_v1');
hold on;
semilogx(N, Memoria_v2, '-o', 'LineWidth', 2, 'DisplayName', 'busca\_sequencial\_v2');
xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Memória Utilizada (bytes)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Memória Utilizada', 'FontSize', 16); % Aumente o tamanho da fonte
legend('Location', 'northwest');
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
set(gca, 'XScale', 'log'); % Configure a escala do eixo x para logaritmo
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Aumente o tamanho da fonte no gráfico
set(gca, 'FontSize', 12);

% Remova as grades
grid off;
