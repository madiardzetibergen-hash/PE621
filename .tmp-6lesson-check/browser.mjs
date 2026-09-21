import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import { readFile, mkdir } from 'node:fs/promises';
import { resolve, extname, sep } from 'node:path';

export async function browserSession() {
  const workspace = resolve('.');
  const temporary = resolve('.tmp-6lesson-check');
  await mkdir(temporary, { recursive: true });
  const mime = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.svg': 'image/svg+xml', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.woff2': 'font/woff2' };
  const http = createServer(async (request, response) => {
    const pathname = decodeURIComponent(new URL(request.url, 'http://localhost').pathname);
    const filepath = resolve(workspace, '.' + (pathname === '/' ? '/frontend/6lesson/index.html' : pathname));
    if (!filepath.startsWith(workspace + sep)) { response.writeHead(403).end(); return; }
    if (pathname === '/favicon.ico') { response.writeHead(204).end(); return; }
    try { response.writeHead(200, { 'content-type': mime[extname(filepath)] || 'application/octet-stream' }).end(await readFile(filepath)); }
    catch { response.writeHead(404).end('Not found'); }
  });
  await new Promise(resolve => http.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${http.address().port}`;
  const process = spawn('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe', [
    '--headless=new', '--remote-debugging-port=0', '--no-first-run', '--no-default-browser-check',
    '--disable-background-networking', '--disable-component-update', '--disable-sync',
    '--disable-features=Translate,OptimizationHints,MediaRouter', '--disable-extensions',
    `--user-data-dir=${resolve(temporary, 'chrome-profile')}`, 'about:blank',
  ], { windowsHide: true, stdio: ['ignore', 'ignore', 'pipe'] });
  let websocket;
  try {
    const debuggerUrl = await new Promise((resolve, reject) => {
      let stderr = '';
      const timeout = setTimeout(() => reject(new Error('Chrome startup timeout: ' + stderr)), 20000);
      process.once('error', error => { clearTimeout(timeout); reject(error); });
      process.stderr.on('data', data => { stderr += data.toString(); const found = stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/); if (found) { clearTimeout(timeout); resolve(found[1]); } });
      process.once('exit', code => { clearTimeout(timeout); reject(new Error('Chrome exited with ' + code + ': ' + stderr)); });
    });
    websocket = new WebSocket(debuggerUrl);
    await new Promise((resolve, reject) => { websocket.addEventListener('open', resolve, { once: true }); websocket.addEventListener('error', reject, { once: true }); });
    let id = 0;
    const pending = new Map();
    const listeners = new Map();
    websocket.addEventListener('message', event => {
      const message = JSON.parse(event.data);
      if (message.id && pending.has(message.id)) {
        const callback = pending.get(message.id); pending.delete(message.id); clearTimeout(callback.timeout);
        if (message.error) callback.reject(new Error(JSON.stringify(message.error))); else callback.resolve(message.result);
      } else if (message.method) {
        for (const callback of listeners.get(message.method) || []) callback(message.params);
      }
    });
    const command = (method, params = {}, sessionId) => new Promise((resolve, reject) => {
      const messageId = ++id;
      const timeout = setTimeout(() => { pending.delete(messageId); reject(new Error('CDP timed out: ' + method)); }, 20000);
      pending.set(messageId, { resolve, reject, timeout });
      websocket.send(JSON.stringify({ id: messageId, method, params, ...(sessionId ? { sessionId } : {}) }));
    });
    const { targetId } = await command('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await command('Target.attachToTarget', { targetId, flatten: true });
    const cdp = (method, params) => command(method, params, sessionId);
    const on = (method, callback) => { if (!listeners.has(method)) listeners.set(method, []); listeners.get(method).push(callback); };
    await Promise.all([cdp('Runtime.enable'), cdp('Page.enable'), cdp('Log.enable'), cdp('Network.enable')]);
    const errors = [];
    on('Runtime.exceptionThrown', event => errors.push({ type: 'exception', message: event.exceptionDetails.exception?.description || event.exceptionDetails.text }));
    on('Runtime.consoleAPICalled', event => { if (event.type === 'error') errors.push({ type: 'console', message: event.args.map(arg => arg.value || arg.description).join(' ') }); });
    on('Log.entryAdded', event => { if (event.entry.level === 'error') errors.push({ type: 'log', message: event.entry.text }); });
    on('Network.loadingFailed', event => errors.push({ type: 'network', message: event.errorText }));
    const evaluate = async expression => {
      const result = await cdp('Runtime.evaluate', { expression, awaitPromise: true, returnByValue: true });
      if (result.exceptionDetails) throw new Error(result.exceptionDetails.exception?.description || result.exceptionDetails.text);
      return result.result.value;
    };
    const navigate = async (path = '/frontend/6lesson/index.html') => {
      await cdp('Page.navigate', { url: base + path });
      await new Promise(resolve => setTimeout(resolve, 250));
      await evaluate('new Promise(resolve => document.readyState === "complete" ? resolve() : window.addEventListener("load", resolve, { once: true }))');
    };
    const close = async () => {
      await command('Browser.close').catch(() => {});
      websocket.close();
      http.closeAllConnections();
      await new Promise(resolve => http.close(resolve));
      if (process.exitCode === null) process.kill();
    };
    return { cdp, on, evaluate, navigate, close, errors, temporary, base };
  } catch (error) {
    websocket?.close(); process.kill(); http.closeAllConnections(); http.close(); throw error;
  }
}

if (process.argv.includes('--smoke')) {
  const browser = await browserSession();
  try { await browser.navigate(); console.log(JSON.stringify({ title: await browser.evaluate('document.title'), errors: browser.errors })); }
  finally { await browser.close(); }
}
