import { writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { browserSession } from './browser.mjs';

const browser = await browserSession();
const results = { pages: [], errors: browser.errors };
try {
  for (const viewport of [{ name: 'desktop', width: 1440, height: 1000 }, { name: 'tablet', width: 900, height: 1000 }, { name: 'mobile', width: 390, height: 844 }, { name: 'mobile-small', width: 320, height: 740 }]) {
    await browser.cdp('Emulation.setDeviceMetricsOverride', { width: viewport.width, height: viewport.height, deviceScaleFactor: 1, mobile: viewport.width < 600 });
    await browser.navigate();
    await browser.evaluate('document.fonts.ready');
    await new Promise(resolve => setTimeout(resolve, 350));
    const layout = await browser.evaluate(`(() => {
      const viewportWidth = document.documentElement.clientWidth;
      return {
        title: document.title,
        viewportWidth,
        scrollWidth: document.documentElement.scrollWidth,
        overflow: document.documentElement.scrollWidth > viewportWidth,
        outside: [...document.querySelectorAll('body *')].filter(element => {
          const rect = element.getBoundingClientRect();
          const style = getComputedStyle(element);
          return style.display !== 'none' && style.visibility !== 'hidden' && rect.width > 0 && (rect.right > viewportWidth + 1 || rect.left < -1);
        }).map(element => ({ tag: element.tagName, class: element.className, width: element.getBoundingClientRect().width })).slice(0, 15),
        brokenImages: [...document.images].filter(image => !image.complete || image.naturalWidth === 0).map(image => image.getAttribute('src')),
        heading: document.querySelector('h1')?.textContent,
        controls: [...document.querySelectorAll('button, input, select, textarea')].filter(element => element.getBoundingClientRect().width > 0).map(element => ({ tag: element.tagName, id: element.id, type: element.type, label: element.getAttribute('aria-label') || element.textContent?.trim() || element.placeholder, action: element.dataset.action }))
      };
    })()`);
    results.pages.push({ viewport, ...layout });
    const screenshot = await browser.cdp('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
    await writeFile(resolve(browser.temporary, `${viewport.name}.png`), Buffer.from(screenshot.data, 'base64'));
  }
  await writeFile(resolve(browser.temporary, 'results.json'), JSON.stringify(results, null, 2));
  console.log(JSON.stringify(results, null, 2));
} finally { await browser.close(); }
