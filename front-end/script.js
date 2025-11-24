// Mapeamento de Títulos e Conteúdo
const pages = {
    'dashboard': {
        title: 'Dashboard',
        subtitle: 'Agenda do dia e métricas de pacientes atendidos.'
    },
    'cadastro': {
        title: 'Cadastro de Pacientes',
        subtitle: 'Insira as informações completas do novo paciente.'
    },
    'relatorios': {
        title: 'Relatórios de Gestão',
        subtitle: 'Acompanhe métricas e resultados da clínica.'
    }
};

// Variáveis globais para os elementos (serão inicializadas em initializeApp)
let sidebar, menuButton, navItems, pageTitle, pageSubtitle, cadastroForm, feedbackMessage;

// Variáveis do Calendário
let calendarContainer, monthYearDisplay, prevMonthButton, nextMonthButton, appointmentsTitle, appointmentsDetail;
let currentCalendarDate; // Data que o calendário está visualizando (mantém o mês e ano)

// Dados simulados de Consultas (Formato: 'YYYY-MM-DD')
const simulatedAppointments = {
    // Consultas de exemplo para o mês de Novembro de 2025
    '2025-11-05': [{ time: '09:00', patient: 'Ana Paula Costa' }, { time: '14:30', patient: 'Bruno Mendes' }],
    '2025-11-10': [{ time: '11:00', patient: 'Carla Dias' }],
    '2025-11-24': [{ time: '08:30', patient: 'Eduardo Felipe' }, { time: '13:00', patient: 'Gabriela Lima' }, { time: '16:45', patient: 'Heitor Vasconcelos' }],
    '2025-11-28': [{ time: '10:00', patient: 'Igor Zanchetta' }]
};

const monthNames = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

// Função para formatar uma data para a chave do objeto de consultas (YYYY-MM-DD)
function formatDateKey(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
}

// Função para exibir os detalhes da consulta
function showAppointments(date) {
    const key = formatDateKey(date);
    const appointments = simulatedAppointments[key] || [];

    appointmentsTitle.textContent = `Consultas para ${String(date.getDate()).padStart(2, '0')}/${String(date.getMonth() + 1).padStart(2, '0')}/${date.getFullYear()}`;
    appointmentsDetail.innerHTML = ''; // Limpa o conteúdo anterior

    if (appointments.length === 0) {
        appointmentsDetail.innerHTML = '<p class="text-secondary">Nenhuma consulta agendada para este dia.</p>';
        return;
    }

    appointments.forEach(appt => {
        const item = document.createElement('div');
        item.classList.add('appointment-item');
        item.innerHTML = `
                    <div class="time">${appt.time}</div>
                    <div class="patient">Paciente: ${appt.patient}</div>
                `;
        appointmentsDetail.appendChild(item);
    });
}

// Função para gerar o calendário
function renderCalendar(date = new Date()) {
    // Define o primeiro dia do mês que será renderizado
    currentCalendarDate = new Date(date.getFullYear(), date.getMonth(), 1);

    const year = currentCalendarDate.getFullYear();
    const month = currentCalendarDate.getMonth();
    const today = new Date();

    // Atualiza o cabeçalho do calendário
    monthYearDisplay.textContent = `${monthNames[month]} ${year}`;

    // Limpa os dias anteriores, mantendo os dias da semana (os 7 primeiros filhos)
    while (calendarContainer.children.length > 7) {
        calendarContainer.removeChild(calendarContainer.lastChild);
    }

    // Determina o dia da semana do primeiro dia do mês (0 = Domingo, 1 = Segunda...)
    const firstDayOfWeek = currentCalendarDate.getDay();
    // Determina o último dia do mês
    const lastDayOfMonth = new Date(year, month + 1, 0).getDate();

    // 1. Preenche os espaços vazios (dias do mês anterior)
    for (let i = 0; i < firstDayOfWeek; i++) {
        const dayDiv = document.createElement('div');
        dayDiv.classList.add('calendar-day', 'empty');
        calendarContainer.appendChild(dayDiv);
    }

    // 2. Preenche os dias do mês atual
    for (let day = 1; day <= lastDayOfMonth; day++) {
        const dayDiv = document.createElement('div');
        const currentDate = new Date(year, month, day);
        const dayKey = formatDateKey(currentDate);

        dayDiv.textContent = day;
        dayDiv.classList.add('calendar-day');
        dayDiv.dataset.date = dayKey; // Armazena a data completa

        // Verifica se é o dia de hoje
        if (day === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
            dayDiv.classList.add('today');
        }

        // Verifica se há consultas simuladas para este dia
        if (simulatedAppointments[dayKey]) {
            dayDiv.classList.add('has-appointment');
            dayDiv.innerHTML += '<span class="appointment-dot"></span>'; // Adiciona a bolinha
        }

        // Adiciona o listener para mostrar os detalhes das consultas ao clicar
        dayDiv.addEventListener('click', () => {
            // Remove classe de "selecionado" de todos
            document.querySelectorAll('.calendar-day.selected').forEach(d => d.classList.remove('selected'));
            // Adiciona classe de "selecionado" ao clicado
            dayDiv.classList.add('selected');
            showAppointments(currentDate);
        });

        calendarContainer.appendChild(dayDiv);
    }

    // Mostra os agendamentos para o dia de hoje por padrão, se for o mês atual
    if (month === today.getMonth() && year === today.getFullYear()) {
        showAppointments(today);
        // Marca o dia atual como selecionado (se ele tiver consultas)
        const todayElement = document.querySelector(`.calendar-day.today`);
        if (todayElement) {
            todayElement.classList.add('selected');
        }
    } else {
        // Se não for o mês atual, limpa a lista de detalhes
        appointmentsTitle.textContent = `Consultas para ${monthNames[month]} ${year}`;
        appointmentsDetail.innerHTML = '<p class="text-secondary">Nenhuma data selecionada para ver agendamentos.</p>';
    }
}


// Função para alternar a visibilidade da Sidebar (mobile)
function toggleSidebar() {
    sidebar.classList.toggle('sidebar-open');
}

// Função para trocar o conteúdo da página
function switchPage(pageName) {

    // 1. Atualiza Título e Subtítulo
    pageTitle.textContent = pages[pageName].title;
    pageSubtitle.textContent = pages[pageName].subtitle;

    // 2. Esconde todos os conteúdos
    document.querySelectorAll('.page-content').forEach(content => {
        content.classList.add('hidden');
    });

    // 3. Mostra o conteúdo da página selecionada
    document.getElementById(`${pageName}-content`).classList.remove('hidden');

    // 4. Atualiza o estado ativo na navegação
    navItems.forEach(item => {
        item.classList.remove('active');

        if (item.dataset.page === pageName) {
            item.classList.add('active');
        }
    });

    // 5. Fecha a sidebar em mobile após a seleção (para telas menores que 1024px)
    if (window.innerWidth < 1024) {
        sidebar.classList.remove('sidebar-open');
    }
}

// Função de submissão do formulário
async function handleFormSubmit(e) {
    e.preventDefault(); // Ação chave: impede o recarregamento da página

    // Simulação da submissão:
    const form = document.getElementById('cadastro-form')
    const formData = new FormData(form)
    /*for (const item of formData.entries()){
        console.log('itens:', item)
    }*/

    const objDataForm = {
        nome: formData.get("nome"),
        endereco: formData.get("endereco"),
        telefone: formData.get("telefone"),
        email: formData.get("email"),
        data_nascimento: formData.get("dataNascimento"),
        data_primeira_consulta: formData.get("dataPrimeiraConsulta"),
        id_plano_saude: formData.get("id_plano_saude")
    }

    console.log('objDataForm', objDataForm)

    const API_ENDPOINT = 'http://127.0.0.1:8000/pacientes';

    try {
        const response = await fetch(
            API_ENDPOINT,
            {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(objDataForm)
            }
        )

        const result = await response.json()
        console.log(result)
        const nomeInput = document.getElementById('nome').value;

        // Limpamos o estado anterior da mensagem
        feedbackMessage.classList.remove('feedback-success');

        feedbackMessage.textContent = `✅ Cadastro de "${nomeInput}" efetuado com sucesso!`;
        feedbackMessage.classList.remove('hidden');
        feedbackMessage.classList.add('feedback-success');

    } catch (error) {
        const nomeInput = document.getElementById('nome').value;

        // Limpamos o estado anterior da mensagem
        feedbackMessage.classList.remove('feedback-error');

        feedbackMessage.textContent = `❗Error: "${error}" ao efetuar cadastro de ${nomeInput}❗`;
        feedbackMessage.classList.remove('hidden');
        feedbackMessage.classList.add('feedback-error');

    }

    // Limpa o formulário após a submissão simulada
    cadastroForm.reset();

    // Oculta a mensagem após 5 segundos
    setTimeout(() => {
        feedbackMessage.classList.add('hidden');
    }, 5000);
}

// Função para carregar total de pacientes
async function loadPacientes() {
    const paragrafo_total_pacientes = document.getElementById('total_pacientes')

    const API_ENDPOINT = 'http://127.0.0.1:8000/pacientes';
    try {
        const response = await fetch(API_ENDPOINT, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        })

        const result = await response.json()
        console.log(result.length)

        paragrafo_total_pacientes.textContent = result.length
    } catch (error) {
        paragrafo_total_pacientes.textContent = `${error}`
    }
}

// Função principal de inicialização
function initializeApp() {
    // 1. Inicializa todas as variáveis de elementos DOM
    sidebar = document.getElementById('sidebar');
    menuButton = document.getElementById('menu-button');
    navItems = document.querySelectorAll('.nav-item');
    pageTitle = document.getElementById('page-title');
    pageSubtitle = document.getElementById('page-subtitle');
    cadastroForm = document.getElementById('cadastro-form');
    feedbackMessage = document.getElementById('feedback-message');

    // Variáveis do Calendário
    calendarContainer = document.getElementById('calendar-days-container');
    monthYearDisplay = document.getElementById('current-month-year');
    prevMonthButton = document.getElementById('prev-month-button');
    nextMonthButton = document.getElementById('next-month-button');
    appointmentsTitle = document.getElementById('appointments-title');
    appointmentsDetail = document.getElementById('appointments-detail');

    // 2. Configuração do Calendário
    // Nota: O mês de Novembro de 2025 está configurado nos dados simulados
    renderCalendar(new Date(2025, 10, 24)); // Renderiza o mês de Novembro de 2025 por padrão para mostrar as consultas simuladas

    // Listener para o botão de Mês Anterior
    prevMonthButton.addEventListener('click', () => {
        // Volta um mês
        currentCalendarDate.setMonth(currentCalendarDate.getMonth() - 1);
        renderCalendar(currentCalendarDate);
    });

    // Listener para o botão de Próximo Mês
    nextMonthButton.addEventListener('click', () => {
        // Avança um mês
        currentCalendarDate.setMonth(currentCalendarDate.getMonth() + 1);
        renderCalendar(currentCalendarDate);
    });

    // 3. Anexa Listeners Gerais

    // Navegação (Sidebar)
    navItems.forEach(item => {
        item.addEventListener('click', function (e) {
            e.preventDefault();
            switchPage(this.dataset.page);
        });
    });

    // Botão de Menu (Mobile)
    menuButton.addEventListener('click', toggleSidebar);

    // Submissão do Formulário de Cadastro
    if (cadastroForm) {
        cadastroForm.addEventListener('submit', handleFormSubmit);
    }

    // chama a requisição que carrega os dados de pacientes
    loadPacientes();

    // Listener de redimensionamento para fechar a sidebar em desktop
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 1024) {
            sidebar.classList.remove('sidebar-open');
        }
    });

    // Inicia a página no estado default
    switchPage('dashboard');
}

document.addEventListener('DOMContentLoaded', initializeApp);