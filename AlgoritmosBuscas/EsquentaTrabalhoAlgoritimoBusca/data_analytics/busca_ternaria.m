% Tempo
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000];
Tempo_busca_ternaria = [1.030000566970557e-05, 4.2000028770416975e-06, 1.5400000847876072e-05, 1.6999998479150236e-05, 3.670000296551734e-05, 3.989999822806567e-05, 4.719999560620636e-05, 5.4899996030144393e-05, 5.869999586138874e-05, 6.350000330712646e-05, 7.349999214056879e-05, 7.429999823216349e-05, 8.360001083929092e-05];

% Plotar o gráfico de tempo de execução para busca_ternaria
figure;
semilogx(N, Tempo_busca_ternaria, '-o', 'LineWidth', 2);
xlabel('Tamanho do Conjunto de Dados (N)', 'FontSize', 14); % Aumente o tamanho da fonte
ylabel('Tempo de Execução (segundos)', 'FontSize', 14); % Aumente o tamanho da fonte
title('Tempo de Execução', 'FontSize', 16); % Aumente o tamanho da fonte
set(gca, 'XTick', N); % Defina os valores de N como marcas no eixo x
set(gca, 'XScale', 'log'); % Configure a escala do eixo x para logaritmo
xlim([min(N), max(N)]); % Defina os limites do eixo x

% Aumente o tamanho da fonte no gráfico
set(gca, 'FontSize', 12);

% Remova as grades
grid off;


% Memória
N = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 500000, 1000000, 5000000, 10000000, 100000000];
Memoria_busca_ternaria = [64, 0, 156, 156, 188, 188, 188, 188, 188, 188, 188, 188, 188];

% Plotar o gráfico de memória utilizada para busca_ternaria
figure;
semilogx(N, Memoria_busca_ternaria, '-o', 'LineWidth', 2);
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
