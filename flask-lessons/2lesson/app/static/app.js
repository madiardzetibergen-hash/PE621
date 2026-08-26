// Пример данных (в реальном проекте данные будут приходить с API)
const mockProducts = [
  { id: 101, name: "Беспроводные наушники", price: "4 500 ₸", description: "Отличный звук и шумоподавление до 20 часов работы." },
  { id: 102, name: "Смарт-часы", price: "12 000 ₸", description: "Мониторинг пульса, сна и всех видов тренировок." },
  { id: 103, name: "Механическая клавиатура", price: "8 900 ₸", description: "RGB подсветка и надежные переключатели." }
];

const appContent = document.getElementById('app-content');
const logo = document.getElementById('logo');
const navHome = document.getElementById('nav-home');

// Главный роутер: отслеживает изменение URL/Hash
function route() {
  const hash = window.location.hash; // Например: "#product/101"

  if (hash.startsWith('#product/')) {
    // Извлекаем динамический ID из URL
    const productId = parseInt(hash.split('/')[1]);
    renderProductDetail(productId);
  } else {
    // По умолчанию показываем каталог
    renderProductList();
  }
}

// Рендер каталога товаров
function renderProductList() {
  appContent.innerHTML = `
    <h2>Каталог товаров</h2>
    <div class="products-grid">
      ${mockProducts.map(product => `
        <div class="product-card">
          <div>
            <h3>${product.name}</h3>
            <p style="color: #888; font-size: 0.85rem; margin-top: 4px;">ID: #${product.id}</p>
            <p style="margin-top: 10px; font-weight: bold; color: #2c3e50;">${product.price}</p>
          </div>
          <!-- Динамический переход по ID через data-id или hash -->
          <button class="btn-view" data-id="${product.id}">Смотреть продукт</button>
        </div>
      `).join('')}
    </div>
  `;

  // Навешиваем слушатели событий на кнопки "Смотреть продукт"
  document.querySelectorAll('.btn-view').forEach(button => {
    button.addEventListener('click', (e) => {
      const id = e.target.getAttribute('data-id');
      // Меняем hash, что автоматически вызовет функцию route()
      window.location.hash = `product/${id}`;
    });
  });
}

// Рендер страницы отдельного товара
function renderProductDetail(id) {
  // Находим товар по dynamic ID
  const product = mockProducts.find(p => p.id === id);

  if (!product) {
    appContent.innerHTML = `
      <div class="detail-card">
        <h2>Товар не найден</h2>
        <button class="back-btn" id="btn-back">← Вернуться к каталогу</button>
      </div>
    `;
  } else {
    appContent.innerHTML = `
      <div class="detail-card">
        <button class="back-btn" id="btn-back">← Назад в каталог</button>
        <h2>${product.name}</h2>
        <p style="color: #777; margin: 8px 0;">Артикул / ID: <strong>#${product.id}</strong></p>
        <h3 style="color: #28a745; margin-bottom: 15px;">${product.price}</h3>
        <p style="line-height: 1.6;">${product.description}</p>
      </div>
    `;
  }

  // Кнопка возврата
  document.getElementById('btn-back').addEventListener('click', () => {
    window.location.hash = '';
  });
}

// Обработка кликов по логотипу и меню
logo.addEventListener('click', (e) => {
  e.preventDefault();
  window.location.hash = '';
});

navHome.addEventListener('click', (e) => {
  e.preventDefault();
  window.location.hash = '';
});

// Слушаем изменения URL (нажатия Назад/Вперед в браузере)
window.addEventListener('hashchange', route);

// Инициализация при первой загрузке страницы
window.addEventListener('DOMContentLoaded', route);