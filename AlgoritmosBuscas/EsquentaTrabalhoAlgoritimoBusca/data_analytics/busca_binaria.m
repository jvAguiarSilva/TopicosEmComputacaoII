% Tempo
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000];
Tempo_busca_binaria = [1.1900003300979733e-05, 7.700000423938036e-06, 1.069999416358769e-05, 1.2199991033412516e-05, 4.710000939667225e-05, 5.77000027988106e-05, 4.980000085197389e-05, 0.00010689999908208847, 7.809999806340784e-05, 7.069999992381781e-05, 0.00014670001110062003, 9.049999061971903e-05, 0.00017109999316744506];

% Plotar o gráfico de custo de tempo para busca_binaria_main
figure;
semilogx(N, Tempo_busca_binaria, '-o', 'LineWidth', 2);
xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Tempo de Execução (segundos)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Custo de Tempo', 'FontSize', 16); % Aumente o tamanho da fonte
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
set(gca, 'XScale', 'log'); % Configure a escala do eixo x para logaritmo
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Aumente o tamanho da fonte no gráfico
set(gca, 'FontSize', 12);

% Remova as grades
grid off;



% Memória
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000];
Memoria_busca_binaria = [64, 0, 96, 160, 288, 352, 480, 544, 672, 736, 928, 992, 1184];

% Plotar o gráfico de custo de memória para busca_binaria_main
figure;
semilogx(N, Memoria_busca_binaria, '-o', 'LineWidth', 2);
xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Memória Utilizada (bytes)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Custo de Memória', 'FontSize', 16); % Aumente o tamanho da fonte
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
set(gca, 'XScale', 'log'); % Configure a escala do eixo x para logaritmo
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Aumente o tamanho da fonte no gráfico
set(gca, 'FontSize', 12);

% Remova as grades
grid off;

