(() => {
  'use strict';

  const STORAGE_KEY = 'circle-6lesson-v1';
  const MAX_POSTS = 50;
  const MAX_COMMENTS = 30;
  const categories = new Set(['life', 'design', 'code']);
  const postList = document.querySelector('#post-list');
  const composer = document.querySelector('#composer-form');
  const postText = document.querySelector('#post-text');
  const searchInput = document.querySelector('#search-input');
  const profileName = document.querySelector('#profile-name');
  const profileBio = document.querySelector('#profile-bio');
  const toast = document.querySelector('#toast');
  const records = new Map();
  const filters = { view: 'feed', feed: 'all', category: null };
  let toastTimer;
  let storageWarningShown = false;

  if (!postList || !composer || !postText) return;

  const validText = (value, limit) => typeof value === 'string'
    && value.trim().length > 0 && value.length <= limit;
  const validId = (id) => typeof id === 'string' && /^[a-zA-Z0-9_-]{1,80}$/.test(id);
  const numberFrom = (value) => Math.max(0, Number.parseInt(value, 10) || 0);

  function notify(message) {
    clearTimeout(toastTimer);
    toast.textContent = message;
    toast.classList.add('is-visible');
    toastTimer = setTimeout(() => {
      toast.classList.remove('is-visible');
      toast.textContent = '';
    }, 4200);
  }

  function readState() {
    const fallback = { posts: [], interactions: {}, profile: null, joined: false };
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      // Account for JSON escaping at the maximum post/comment counts.
      if (!raw || raw.length > 6000000) return fallback;
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) return fallback;
      const seen = new Set();
      const posts = Array.isArray(parsed.posts) ? parsed.posts.filter((post) => {
        if (!post || !validId(post.id) || !post.id.startsWith('user-')
          || seen.has(post.id) || !validText(post.text, 1500)
          || !categories.has(post.category) || !Number.isFinite(post.createdAt)
          || post.createdAt <= 0 || post.createdAt > Date.now() + 60000) return false;
        seen.add(post.id);
        return true;
      }).slice(0, MAX_POSTS).map(({ id, text, category, createdAt }) => ({ id, text, category, createdAt })) : [];
      const profile = parsed.profile && validText(parsed.profile.name, 40)
        && validText(parsed.profile.bio, 180)
        ? { name: parsed.profile.name.trim(), bio: parsed.profile.bio.trim() } : null;
      return {
        posts,
        interactions: parsed.interactions && typeof parsed.interactions === 'object'
          && !Array.isArray(parsed.interactions) ? parsed.interactions : {},
        profile,
        joined: parsed.joined === true,
      };
    } catch {
      return fallback;
    }
  }

  const state = readState();

  function persist() {
    const interactions = {};
    for (const [id, record] of records) {
      interactions[id] = { liked: record.liked, saved: record.saved, comments: record.comments };
    }
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ ...state, interactions }));
    } catch {
      if (!storageWarningShown) {
        storageWarningShown = true;
        setTimeout(() => notify('Хранилище браузера недоступно. Изменения сохранятся до перезагрузки страницы.'), 800);
      }
    }
  }

  function currentName() {
    return profileName.textContent.trim() || 'John Smith';
  }

  function renderComments(record) {
    const list = record.element.querySelector('.comments-list');
    list.replaceChildren();
    for (const comment of record.comments) {
      const item = document.createElement('div');
      item.className = 'comment-item';
      const author = document.createElement('strong');
      author.textContent = currentName();
      author.dataset.profileName = '';
      const body = document.createElement('p');
      body.className = 'comment-body';
      body.textContent = comment;
      item.append(author, body);
      list.append(item);
    }
    record.element.querySelector('.comment-count').textContent = record.baseComments + record.comments.length;
  }

  function renderActions(record) {
    const { element, liked, saved, baseLikes } = record;
    element.dataset.liked = String(liked);
    element.dataset.saved = String(saved);
    element.dataset.likes = String(baseLikes + Number(liked));
    element.querySelector('.like-count').textContent = baseLikes + Number(liked);
    const likeButton = element.querySelector('[data-action="like"]');
    likeButton.setAttribute('aria-pressed', String(liked));
    likeButton.setAttribute('aria-label', liked ? 'Убрать отметку «Нравится»' : 'Нравится');
    const saveButton = element.querySelector('[data-action="save"]');
    saveButton.setAttribute('aria-pressed', String(saved));
    saveButton.setAttribute('aria-label', saved ? 'Удалить из сохранённого' : 'Сохранить публикацию');
    saveButton.title = saved ? 'Удалить из сохранённого' : 'Сохранить публикацию';
  }

  function registerPost(element, order) {
    const id = element.dataset.id;
    if (!validId(id) || records.has(id)) return;
    element.id = `post-${id}`;
    const saved = Object.prototype.hasOwnProperty.call(state.interactions, id)
      ? state.interactions[id] : null;
    const record = {
      element,
      order,
      baseLikes: numberFrom(element.dataset.likes),
      baseComments: numberFrom(element.querySelector('.comment-count').textContent),
      liked: saved?.liked === true,
      saved: saved?.saved === true,
      comments: Array.isArray(saved?.comments)
        ? saved.comments.filter((comment) => validText(comment, 500)).slice(0, MAX_COMMENTS) : [],
    };
    records.set(id, record);
    const panel = element.querySelector('.comments-panel');
    panel.id = `comments-${id}`;
    const commentButton = element.querySelector('[data-action="comments"]');
    commentButton.setAttribute('aria-controls', panel.id);
    commentButton.setAttribute('aria-expanded', 'false');
    renderActions(record);
    renderComments(record);
  }

  function createPost(post, order) {
    const element = document.querySelector('#post-template').content.firstElementChild.cloneNode(true);
    element.dataset.id = post.id;
    element.dataset.category = post.category;
    element.dataset.following = 'true';
    element.dataset.likes = '0';
    element.dataset.liked = 'false';
    element.dataset.saved = 'false';
    const name = element.querySelector('.post-author-name');
    name.textContent = currentName();
    name.dataset.profileName = '';
    element.querySelector('.post-copy').textContent = post.text;
    element.querySelector('.like-count').textContent = '0';
    element.querySelector('.comment-count').textContent = '0';
    const time = element.querySelector('.post-time');
    time.textContent = Date.now() - post.createdAt < 60000 ? 'Только что'
      : new Intl.DateTimeFormat('ru', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }).format(post.createdAt);
    time.setAttribute('datetime', new Date(post.createdAt).toISOString());
    const tag = element.querySelector('[data-post-category]');
    if (tag) tag.textContent = { design: 'Дизайн', code: 'Разработка', life: 'Жизнь' }[post.category];
    postList.prepend(element);
    registerPost(element, order);
    return element;
  }

  function updateCounts() {
    document.querySelector('#profile-post-count').textContent = String(24 + state.posts.length);
    document.querySelector('#saved-count').textContent = String([...records.values()].filter((record) => record.saved).length);
  }

  function applyFilters() {
    const query = searchInput.value.trim().toLocaleLowerCase('ru');
    const sorted = [...records.values()].sort((a, b) => filters.feed === 'popular'
      ? (b.baseLikes + Number(b.liked)) - (a.baseLikes + Number(a.liked)) || a.order - b.order
      : a.order - b.order);
    let visibleCount = 0;
    for (const record of sorted) {
      const { element } = record;
      const searchable = `${element.querySelector('.post-author-name').textContent} ${element.querySelector('.post-copy').textContent}`.toLocaleLowerCase('ru');
      const visible = (filters.view !== 'saved' || record.saved)
        && (filters.feed !== 'following' || element.dataset.following === 'true')
        && (!filters.category || filters.category === element.dataset.category)
        && (!query || searchable.includes(query));
      element.hidden = !visible;
      if (visible) visibleCount += 1;
      postList.append(element);
    }
    document.querySelector('#empty-state').hidden = visibleCount !== 0;
    document.querySelector('#feed-title').textContent = filters.view === 'saved' ? 'Сохранённое' : 'Лента сообщества';
    document.querySelectorAll('[data-view]').forEach((button) => {
      const active = button.dataset.view === filters.view;
      button.classList.toggle('is-active', active);
      if (active) button.setAttribute('aria-current', 'page');
      else button.removeAttribute('aria-current');
    });
    document.querySelectorAll('.feed-filter').forEach((button) => {
      const active = button.dataset.filter === filters.feed;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    document.querySelectorAll('[data-topic]').forEach((button) => {
      button.setAttribute('aria-pressed', String(button.dataset.topic === filters.category));
    });
    updateCounts();
  }

  function clearFilters() {
    filters.view = 'feed';
    filters.feed = 'all';
    filters.category = null;
    searchInput.value = '';
    applyFilters();
  }

  function scrollTo(element) {
    element.scrollIntoView({ block: 'center', behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }

  function openDialog(dialog) {
    if (!dialog.open) dialog.showModal();
  }

  function applyProfile() {
    if (state.profile) {
      profileName.textContent = state.profile.name;
      profileBio.textContent = state.profile.bio;
    }
    document.querySelector('#greeting-name').textContent = currentName().split(/\s+/)[0];
    document.querySelectorAll('[data-profile-name]').forEach((node) => { node.textContent = currentName(); });
  }

  function updateComposer() {
    document.querySelector('#character-count').textContent = `${postText.value.length} / 1500`;
    document.querySelector('#publish-button').disabled = postText.value.trim().length === 0;
    postText.setCustomValidity('');
  }

  applyProfile();
  postList.querySelectorAll('.post-card').forEach((element, index) => registerPost(element, index));
  state.posts.forEach((post, index) => createPost(post, -state.posts.length + index));
  applyFilters();
  updateComposer();

  postText.addEventListener('input', updateComposer);
  composer.addEventListener('submit', (event) => {
    event.preventDefault();
    const text = postText.value.trim();
    if (!validText(text, 1500)) {
      postText.setCustomValidity('Напишите от 1 до 1500 символов.');
      postText.reportValidity();
      return;
    }
    if (state.posts.length >= MAX_POSTS) {
      notify('В этой демоверсии можно сохранить до 50 публикаций.');
      return;
    }
    const category = document.querySelector('#post-category').value;
    const post = {
      id: `user-${Date.now()}-${Math.random().toString(36).slice(2, 10)}`,
      text,
      category: categories.has(category) ? category : 'life',
      createdAt: Date.now(),
    };
    state.posts.unshift(post);
    const element = createPost(post, Math.min(0, ...[...records.values()].map((record) => record.order)) - 1);
    postText.value = '';
    updateComposer();
    clearFilters();
    persist();
    notify('Публикация добавлена в вашу ленту.');
    scrollTo(element);
  });

  postList.addEventListener('click', async (event) => {
    const button = event.target.closest('button[data-action]');
    if (!button) return;
    const record = records.get(button.closest('.post-card')?.dataset.id);
    if (!record) return;
    const action = button.dataset.action;
    if (action === 'like' || action === 'save') {
      const property = action === 'like' ? 'liked' : 'saved';
      record[property] = !record[property];
      renderActions(record);
      applyFilters();
      persist();
      if (action === 'save') notify(record.saved ? 'Публикация сохранена.' : 'Публикация удалена из сохранённого.');
    } else if (action === 'comments') {
      const panel = record.element.querySelector('.comments-panel');
      panel.hidden = !panel.hidden;
      button.setAttribute('aria-expanded', String(!panel.hidden));
      if (!panel.hidden) panel.querySelector('input').focus();
    } else if (action === 'share') {
      const url = new URL(window.location.href);
      url.hash = `post-${record.element.dataset.id}`;
      try {
        if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
        await navigator.clipboard.writeText(url.href);
        notify('Ссылка скопирована. Локальные публикации доступны в этом браузере.');
      } catch {
        const input = document.querySelector('#share-link');
        input.value = url.href;
        openDialog(document.querySelector('#share-dialog'));
        input.focus();
        input.select();
      }
    }
  });

  postList.addEventListener('submit', (event) => {
    const form = event.target.closest('.comment-form');
    if (!form) return;
    event.preventDefault();
    const record = records.get(form.closest('.post-card').dataset.id);
    const input = form.elements.namedItem('comment');
    const comment = input.value.trim();
    if (!validText(comment, 500)) {
      notify('Напишите комментарий: от 1 до 500 символов.');
      input.focus();
      return;
    }
    if (record.comments.length >= MAX_COMMENTS) {
      notify('В демоверсии доступно до 30 комментариев к публикации.');
      return;
    }
    record.comments.push(comment);
    input.value = '';
    renderComments(record);
    persist();
    notify('Комментарий добавлен.');
    input.focus();
  });

  searchInput.addEventListener('input', applyFilters);
  document.querySelectorAll('.feed-filter').forEach((button) => button.addEventListener('click', () => {
    filters.feed = button.dataset.filter;
    applyFilters();
  }));
  document.querySelectorAll('[data-view]').forEach((button) => button.addEventListener('click', () => {
    filters.view = button.dataset.view;
    filters.feed = 'all';
    filters.category = null;
    searchInput.value = '';
    applyFilters();
    scrollTo(document.querySelector('#feed-title'));
  }));
  document.querySelectorAll('[data-topic]').forEach((button) => button.addEventListener('click', () => {
    filters.category = filters.category === button.dataset.topic ? null : button.dataset.topic;
    applyFilters();
    scrollTo(document.querySelector('#feed-title'));
  }));
  document.querySelector('#clear-filters').addEventListener('click', clearFilters);
  document.querySelectorAll('[data-compose]').forEach((button) => button.addEventListener('click', () => {
    scrollTo(composer);
    postText.focus({ preventScroll: true });
  }));

  document.querySelectorAll('[data-edit-profile]').forEach((button) => button.addEventListener('click', () => {
    document.querySelector('#edit-name').value = currentName();
    document.querySelector('#edit-bio').value = profileBio.textContent.trim();
    openDialog(document.querySelector('#profile-dialog'));
  }));
  document.querySelector('#profile-form').addEventListener('submit', (event) => {
    event.preventDefault();
    const name = document.querySelector('#edit-name').value.trim();
    const bio = document.querySelector('#edit-bio').value.trim();
    if (!validText(name, 40) || !validText(bio, 180)) {
      notify('Укажите имя и короткое описание профиля.');
      return;
    }
    state.profile = { name, bio };
    applyProfile();
    applyFilters();
    persist();
    document.querySelector('#profile-dialog').close();
    notify('Профиль обновлён.');
  });

  document.querySelectorAll('[data-story]').forEach((button) => button.addEventListener('click', () => {
    document.querySelector('#story-title').textContent = button.dataset.story;
    document.querySelector('#story-description').textContent = button.dataset.description;
    openDialog(document.querySelector('#story-dialog'));
  }));
  document.querySelectorAll('[data-close-dialog]').forEach((button) => button.addEventListener('click', () => {
    button.closest('dialog').close();
  }));
  document.querySelectorAll('dialog').forEach((dialog) => dialog.addEventListener('click', (event) => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right
      || event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  }));

  const joinButton = document.querySelector('#event-join');
  function renderEvent() {
    joinButton.textContent = state.joined ? 'Вы участвуете' : 'Участвовать';
    joinButton.setAttribute('aria-pressed', String(state.joined));
  }
  joinButton.addEventListener('click', () => {
    state.joined = !state.joined;
    renderEvent();
    persist();
    notify(state.joined ? 'Участие отмечено в этом браузере.' : 'Отметка об участии снята.');
  });
  renderEvent();

  function revealLinkedPost() {
    const id = window.location.hash.startsWith('#post-') ? window.location.hash.slice(6) : '';
    const record = records.get(id);
    if (!record) return;
    clearFilters();
    requestAnimationFrame(() => scrollTo(record.element));
  }
  window.addEventListener('hashchange', revealLinkedPost);
  revealLinkedPost();
})();
